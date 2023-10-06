import random
from PIL import Image, ImageDraw

# Constants for maze cell states
WALL = "#"
PATH = " "
START = "S"
END = "E"

# Function to generate a maze using Randomized Depth-First Search algorithm
def generate_randomized_dfs_maze(width, height):
    maze = [[WALL] * (2 * width + 1) for _ in range(2 * height + 1)]

    # Start-point
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    start_x = 2 * start_x + 1
    start_y = 2 * start_y + 1
    maze[start_y][start_x] = START

    stack = [(start_x, start_y)]
    while stack:
        current_x, current_y = stack[-1]

        neighbors = []
        if current_x > 2 and maze[current_y][current_x - 2] == WALL:
            neighbors.append((current_x - 2, current_y))
        if current_x < 2 * width - 2 and maze[current_y][current_x + 2] == WALL:
            neighbors.append((current_x + 2, current_y))
        if current_y > 2 and maze[current_y - 2][current_x] == WALL:
            neighbors.append((current_x, current_y - 2))
        if current_y < 2 * height - 2 and maze[current_y + 2][current_x] == WALL:
            neighbors.append((current_x, current_y + 2))

        if neighbors:
            next_x, next_y = random.choice(neighbors)
            maze[next_y][next_x] = PATH
            maze[current_y + (next_y - current_y) // 2][current_x + (next_x - current_x) // 2] = PATH

            stack.append((next_x, next_y))
        else:
            stack.pop()

    # End-point
    end_x, end_y = random.randint(0, width - 1), random.randint(0, height - 1)
    end_x = 2 * end_x + 1
    end_y = 2 * end_y + 1
    maze[end_y][end_x] = END

    return maze

# Function to generate a maze using Randomized Kruskal's algorithm
def generate_randomized_kruskal_maze(width, height):
    maze = [[WALL] * (2 * width + 1) for _ in range(2 * height + 1)]

    walls = []

    for y in range(height):
        for x in range(width):
            maze[2 * y + 1][2 * x + 1] = PATH

            if y > 0:
                walls.append(((x, y), (x, y - 1)))
            if y < height - 1:
                walls.append(((x, y), (x, y + 1)))

            if x > 0:
                walls.append(((x, y), (x - 1, y)))
            if x < width - 1:
                walls.append(((x, y), (x + 1, y)))

    def find_set(cell):
        for i, s in enumerate(sets):
            if cell in s:
                return i
        return None

    sets = [{(x, y)} for y in range(height) for x in range(width)]

    while walls:
        wall_index = random.randrange(len(walls))
        cell1, cell2 = walls[wall_index]
        set1_idx = find_set(cell1)
        set2_idx = find_set(cell2)

        if set1_idx is not None and set2_idx is not None and set1_idx != set2_idx:
            set1 = sets[set1_idx]
            set2 = sets[set2_idx]

            set1.update(set2)
            sets.pop(set2_idx)

            x1, y1 = cell1
            x2, y2 = cell2
            maze[y1 + y2 + 1][x1 + x2 + 1] = PATH

        walls.pop(wall_index)

    # Start-point
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    start_x = 2 * start_x + 1
    start_y = 2 * start_y + 1
    maze[start_y][start_x] = START

    # End-point
    end_x, end_y = random.randint(0, width - 1), random.randint(0, height - 1)
    end_x = 2 * end_x + 1
    end_y = 2 * end_y + 1
    maze[end_y][end_x] = END

    return maze

# Function to generate a maze image
def generate_maze_image(maze, file_name, cell_size=20):
    width = len(maze[0])
    height = len(maze)

    # Create an image
    image = Image.new("RGB", (width * cell_size, height * cell_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    for y in range(height):
        for x in range(width):
            if maze[y][x] == WALL:
                draw.rectangle(
                    (x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size),
                    fill=(0, 0, 0)
                )
            elif maze[y][x] == START:
                draw.rectangle(
                    (x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size),
                    fill=(0, 255, 0)
                )
            elif maze[y][x] == END:
                draw.rectangle(
                    (x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size),
                    fill=(255, 0, 0)
                )

    image.save(file_name)

# Main menu function
def main_menu():
    print("Maze Generation Menu:")
    print("1. Generate and Save Randomized Depth-First Search Maze")
    print("2. Generate and Save Randomized Kruskal's Maze")
    print("3. Quit")

    while True:
        choice = input("Enter your choice (1-3): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 3:
                return choice
        print("Invalid choice. Please enter a valid option (1-3).")

# Main function
def main():
    while True:
        choice = main_menu()

        if choice == 1:
            width = int(input("Enter the width of the DFS maze (default is 10): ") or 10)
            height = int(input("Enter the height of the DFS maze (default is 10): ") or 10)
            maze = generate_randomized_dfs_maze(width, height)
            maze_name = "maze_dfs.png"
        elif choice == 2:
            width = int(input("Enter the width of the Kruskal's maze (default is 10): ") or 10)
            height = int(input("Enter the height of the Kruskal's maze (default is 10): ") or 10)
            maze = generate_randomized_kruskal_maze(width, height)
            maze_name = "maze_kruskal.png"
        elif choice == 3:
            break

        cell_size = int(input("Enter the cell size for visualization (default is 20): ") or 20)
        generate_maze_image(maze, maze_name, cell_size)
        print(f"Maze saved as {maze_name}")

if __name__ == "__main__":
    main()

import random
from PIL import Image, ImageDraw

# Constants for maze cell states
WALL = "#"
PATH = " "
START = "S"
END = "E"
GREEN = "G"

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
    maze = [[WALL] * width for _ in range(height)]

    sets = {(x, y): {(x, y)} for y in range(height) for x in range(width)}

    def find_set(cell):
        for key, value in sets.items():
            if cell in value:
                return key

    def merge_sets(set1, set2):
        if set1 is not None and set2 is not None:
            sets[set1].update(sets[set2])
            for cell in sets[set2]:
                sets[cell] = sets[set1]
            del sets[set2]

    def in_different_sets(cell1, cell2):
        set1 = find_set(cell1)
        set2 = find_set(cell2)
        return set1 != set2

    walls = []
    for y in range(1, height, 2):
        for x in range(1, width, 2):
            walls.append((x, y))

    random.shuffle(walls)

    for wall in walls:
        x, y = wall

        cell1 = (x - 1, y)
        cell2 = (x + 1, y)

        if in_different_sets(cell1, cell2):
            maze[y][x] = PATH
            merge_sets(find_set(cell1), find_set(cell2))

    for y in range(height):
        for x in range(width):
            if maze[y][x] == PATH and random.random() < 0.2:
                maze[y][x] = WALL

    # Start-point
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    maze[start_y][start_x] = START

    # End-point
    end_x, end_y = random.randint(0, width - 1), random.randint(0, height - 1)
    maze[end_y][end_x] = END

    return maze

# Function to generate a maze using Randomized Prim's algorithm
def generate_randomized_prim_maze(width, height):
    maze = [[WALL] * (2 * width + 1) for _ in range(2 * height + 1)]

    #Start-point
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    start_x = 2 * start_x + 1
    start_y = 2 * start_y + 1
    maze[start_y][start_x] = GREEN

    frontier = [(start_x, start_y)]

    while frontier:
        current_x, current_y = random.choice(frontier)

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

            frontier.append((next_x, next_y))

        frontier.remove((current_x, current_y))

    # End-point
    end_x, end_y = random.randint(0, width - 1), random.randint(0, height - 1)
    end_x = 2 * end_x + 1
    end_y = 2 * end_y + 1
    maze[end_y][end_x] = END

    return maze

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
            elif maze[y][x] == GREEN:
                draw.rectangle(
                    (x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size),
                    fill=(0, 255, 0)
                )

    image.save(file_name)

def main_menu():
    print("Maze Generation Menu:")
    print("1. Generate and Save Randomized Depth-First Search Maze")
    print("2. Generate and Save Randomized Kruskal's Maze")
    print("3. Generate and Save Randomized Prim's Maze")
    print("4. Quit")

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                return choice
        print("Invalid choice. Please enter a valid option (1-4).")

def main():
    while True:
        choice = main_menu()

        if choice == 1:
            width = int(input("Enter the width of the maze (default is 10): ") or 10)
            height = int(input("Enter the height of the maze (default is 10): ") or 10)
            maze = generate_randomized_dfs_maze(width, height)
            maze_name = "maze_dfs.png"
        elif choice == 2:
            width = int(input("Enter the width of the maze (default is 10): ") or 10)
            height = int(input("Enter the height of the maze (default is 10): ") or 10)
            maze = generate_randomized_kruskal_maze(width, height)
            maze_name = "maze_kruskal.png"
        elif choice == 3:
            width = int(input("Enter the width of the maze (default is 10): ") or 10)
            height = int(input("Enter the height of the maze (default is 10): ") or 10)
            maze = generate_randomized_prim_maze(width, height)
            maze_name = "maze_prim.png"
        elif choice == 4:
            break

        cell_size = int(input("Enter the cell size for visualization (default is 20): ") or 20)
        generate_maze_image(maze, maze_name, cell_size)
        print(f"Maze saved as {maze_name}")

if __name__ == "__main__":
    main()

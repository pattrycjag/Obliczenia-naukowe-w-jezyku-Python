# EXERCISE 2.1 Create a long positive integer. Find the number of zeros. Hint: change the number to a string.
import random
print("Ex.2.1")
number = ''.join(str(random.randint(0, 9)) for _ in range(100))
zero_count = number.count('0')
print("Number: ", number)
print("Number of zeros: ", zero_count)

# EXERCISE 2.2 (BOOL)
print("Ex.2.2")
# x = 5 --> przypisanie zmiennej x wartości 5.
# x == 5 i 3 # 3 --> Wyrażenie logiczne x == 5 jest prawdziwe (ponieważ x ma wartość 5), a następnie wyrażenie 3 jest wykonywane i zwraca wartość 3.
# x == 4 i 3 # Fałsz --> Wyrażenie logiczne x == 4 jest fałszywe (ponieważ x ma wartość 5), więc całe wyrażenie jest fałszywe.
# 3 i x == 5 # Prawda --> Wyrażenie 3 jest prawdziwe, a wyrażenie logiczne x == 5 również jest prawdziwe, więc całe wyrażenie jest prawdziwe.
# 3 i x == 4 # Fałsz --> Wyrażenie 3 jest prawdziwe, ale wyrażenie logiczne x == 4 jest fałszywe, więc całe wyrażenie jest fałszywe.
x=isinstance(True, int) #--> Sprawdzamy, czy obiekt True jest instancją klasy int. Ponieważ wartość logiczna True jest równa 1, która jest typu int, więc wynik będzie True.
y=isinstance(True, bool) #--> Sprawdzamy, czy obiekt True jest instancją klasy bool. Ponieważ wartość logiczna True jest typu bool, wynik będzie True.
print(x,y)

# EXERCISE 2.3 (NUMBERS)
# Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum()].
print("Ex.2.3")
suma= sum(i*i for i in range(1, 2022, 2))
print("The sum of the numbers in the series is: ", suma)

# EXERCISE 2.4 (STR)
# (a) Find Unicode code points (int) for all characters of your name.
print("Ex.2.4a")
name = "Patrycja"
for char in name:
    code_point = ord(char)
    print(f"Character '{char}' has Unicode code point: {code_point}")

 # (b) Prepare the periodic table (ten elements) as a list
 # pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), ...].
 # Use pt to print a table (3 right + 20 left + 6 center + 10 right)
print("Ex.2.4b")
pt = [(1, "Hydrogen", "H", 1),
      (2, "Helium", "He", 4),
      (3, "Lithium", "Li", 7),
      (4, "Beryllium", "Be", 9),
      (5, "Boron", "B", 11),
      (6, "Carbon", "C", 12),
      (7, "Nitrogen", "N", 14),
      (8, "Oxygen", "O", 16),
      (9, "Fluorine", "F", 19),
      (10, "Neon", "Ne", 20)]
print("{:<3} {:<20} {:^6} {:>10}".format("No", "Element", "Symbol", "Weight"))
print("-" * 40)
for element in pt:
    print("{:<3} {:<20} {:^6} {:>10}".format(element[0], element[1], element[2], element[3]))

 # EXERCISE 2.5 (LIST)
 # Let S be a long string (many lines).
 # Find the number of black characters in S [not whitespace, see the method S.isspace()].
 # Find the number of words in S (a word is a sequence of black characters).
 # Find the longest word in S.
 # Sort words from S according to (1) the lexicographic order, (2) the length.

print("Ex.2.5")
S = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi molestie, arcu ac venenatis efficitur, ex magna maximus lacus, a sodales elit quam vitae justo. In facilisis hendrerit ex ut sodales. Sed a purus fringilla, pharetra elit eget, dignissim arcu. Maecenas id felis leo. Nullam eget orci eu sapien sagittis congue id et massa. Sed ut sollicitudin neque. Vivamus metus ante, ultrices vitae commodo sit amet, aliquet a massa. Etiam consequat tortor id elit finibus, in tincidunt lacus pulvinar. Sed quam quam, sodales vel vestibulum id, commodo sit amet sapien.'''

num_black_chars = sum(1 for c in S if not c.isspace())
print("Number of black characters in S:", num_black_chars)

words = S.split()
num_words = len(words)
print("Number of words in S:", num_words)

longest_word = max(words, key=len)
print("Longest word in S:", longest_word)

lex_sorted_words = sorted(words)
print("Words sorted by lexicographic order:", lex_sorted_words)

len_sorted_words = sorted(words, key=len)
print("Words sorted by length:", len_sorted_words)

 # EXERCISE 2.6 (TUPLE) Find and explain the results.
# t = (2, 4)   -->tworzenie tupli z dwoma liczbami 2 i 4
#  print(t[2])  --> pokaż trzeci wyraz tupli t - nie istnieje (Error)
#  t.append(6)  -->
#  a, b = t ; print(a, b)  -->

 # EXERCISE 2.7 (DICT) Create a dict for conversion of roman numerals (I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M) to arabic numbers. Use different methods.
print("Ex.2.7")
def roman_to_arabic(roman_numeral):
    roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic_symbols = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    arabic_numeral = 0
    i = 0
    for idx, r in enumerate(roman_symbols):
        while roman_numeral[i:i + len(r)] == r:
            arabic_numeral += arabic_symbols[idx]
            i += len(r)
    return arabic_numeral
roman_numeral = 'XVIII'
arabic_numeral = roman_to_arabic(roman_numeral)
print("Roman numeral:", roman_numeral, "Arabic numeral:", arabic_numeral)


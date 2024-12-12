# Basic Practice:
# Create a list of squares for numbers from 1 to 10
p1 = [x**2 for x in range(1,11)]
print(p1)

# Generate a list of even numbers between 1 and 20
p2 = [x for x in range(1,21) if x % 2 == 0]
print(p2)

# Convert a list of Celsius temperatures to Fahrenheit
temps = [2, 10, 27, 20, 18]
p3 = [temp * (9/5) + 32 for temp in temps]
print(p3)

# String Manipulation:
# Create a list of the lengths of words in a given sentence
sentence = "The ball is red and yellow."
p4 = [len(word) for word in sentence[:-1].split()]
print(p4)

# Extract all vowels from a given string
s = "thisisashowTHISISASHOW"
p5 = [char for char in s if char.lower() not in 'aeiou']
print(('').join(p5))

# Convert a list of mixed-case strings to all lowercase
l6 = ['hi', 'HELLO', 'ThisIs', 'A', 'sHoW']
p6 = [word.lower() for word in l6]
print(p6)

# Filtering Problems:
# From a list of numbers, create a new list with only numbers divisible by 3
l7 = [1, 2, 6, 5, 8, 32, 3]
p7 = [num for num in l7 if num % 3 == 0]
print(p7)

# Create a list of words that start with 'a' from a given list of words
l8 = ['apple', 'banana', 'pie', 'juice', 'area']
p8 = [word for word in l8 if word[0] == 'a']
print(p8)

# Filter out all negative numbers from a list
l9 = [-1, 0, 1, 2, 100, -100]
p9 = [x for x in l9 if x >= 0]
print(p9)

# More Complex:
# Create a list of tuples containing (number, square, cube) for numbers 1-5
p10 = [[x, x**2, x**3] for x in range(1,6)]
print(p10)

# Generate a list of all coordinates (x,y) where x and y range from 0 to 2
p11 = [(x,y) for x in range(0,3) for y in range(0,3)]
print(p11)

# Create a list of common elements between two given lists
l12a = ["shoe", "bow", "hook"]
l12b = ["toy", "shoe", "bow", "cap"]
p12 = [word_a for word_a in l12a for word_b in l12b if word_a == word_b]
print(p12)

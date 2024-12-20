# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
# Expected Output:

# Orginal String is  PYnative
# Printing only even index chars
# P
# n
# t
# v
try:
    string = input("STRING: ")
    for x in range(0, len(string), 2):
        print(string[x])
except Exception as e:
    print(f"Erro Genérico: {type(e)}\n{e}")

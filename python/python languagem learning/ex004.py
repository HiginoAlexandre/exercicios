# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

# For Example:

# remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
string = input("STRING: ")
try:
    quant_char = int(input("Quantidade de caracteres a ser eliminado: "))
    print(f"STRING com caracteres removidos: {string[quant_char:]}")
except ValueError:
    print("Erro: Você não digitou um numero correcto.")
except Exception as e:
    print(f"Erro genérico: {type(e)}\n{e}")
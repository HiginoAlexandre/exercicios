# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# Expected Output:

# Given list: [10, 20, 30, 40, 10]
# result is True

# numbers_y = [75, 65, 35, 75, 30]
# result is False

numero_x = [493,934,493]
numero_y = [493,934,492]
print(f"numero_x = {numero_x}")
if numero_x[0] == numero_x[-1]: print("Resultado é Verdadeiro")
else:print("Resultado é Falso")
print(f"numero_y = {numero_y}")
if numero_x[0] == numero_y[-1]: print("Resultado é Verdadeiro")
else:print("Resultado é Falso")
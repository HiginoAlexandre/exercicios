#Given two integer numbers, write a Python code to return
#their product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

try:
    n1 = int(input("numero1 = "))
    n2 = int(input("numero2 = "))
    if (n1 * n2 <= 1000):
        print(f"produto: {n1*n2}")
    else:
        print(f"soma: {n1+n2}")
except ValueError as e:
    print("O valor que você digitou não é um número")
except Exception as e:
    print(f"Erro genérico: {type(e)}\n{e}")
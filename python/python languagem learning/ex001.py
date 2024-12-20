#Given two integer numbers, write a Python code to return
#their product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

def product_sum():
    try:
        numero1 = int(input("numero1 = "))
        numero2 = int(input("numero2 = "))
    except ValueError as e:
        print("Erro: Você não digitou um numero correctamente")
    if numero1*numero2 <= 1_000: print(f"product: {numero1*numero2}")
    else: print(f"soma: {numero1+numero2}")

product_sum()
input()
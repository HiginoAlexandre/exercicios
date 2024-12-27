def  funcao():
    try:
        numero1 = int(input("numero1 = "))
        numero2 = int(input("numero2 = "))
    except ValueError as e:
        print("erro: você digitou um valor invalido ao invez de digitar um numero")
    if(numero1*numero2 <= 1000): return print(f"O resultado é {numero1*numero2}")
    else: return print(f"O resultado é {numero1+numero2}")
funcao()    

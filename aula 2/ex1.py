
print("Calculadora")
numero1 = float(input("escreva o numero 1: "))
numero2 = float(input("escreva o numero 2: "))
operador = input("escolha o operador (+ , - , / , *): ")
if operador == "+":
    resultado = numero1+numero2
    print(f"{numero1} + {numero2} = {resultado}")
elif operador == "-":
    resultado = numero1-numero2
    print(f"{numero1} - {numero2} = {resultado}")
elif operador == "/":
    resultado = numero1/numero2
    print(f"{numero1} / {numero2} = {resultado}")
elif operador == "*":
    resultado = numero1*numero2
    print(f"{numero1} * {numero2} = {resultado}")
else:
    print("operador invalido")
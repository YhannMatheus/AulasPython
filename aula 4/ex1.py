print("Calculadora")
numero1 = float(input("escreva o numero 1: "))
numero2 = float(input("escreva o numero 2: "))
operador = input("escolha o operador (+ , - , / , *): ")

def soma (numero1, numero2):
    resultado = numero1+numero2
    return resultado


def subtracao (numero1, numero2):
    resultado = numero1 - numero2
    return resultado


def multiplicacao (numero1, numero2):
    resultado = numero1*numero2
    return resultado


def divisao (numero1, numero2):
    resultado = numero1/numero2
    return resultado



if operador == "+":
    resultado = numero1+numero2
    print(soma(numero1,numero2))

elif operador == "-":
    resultado = numero1-numero2
    print(subtracao(numero1,numero2))

elif operador == "/":
    print(divisao(numero1,numero2))

elif operador == "*":
    print(multiplicacao(numero1,numero2))

else:
    print("operador invalido")
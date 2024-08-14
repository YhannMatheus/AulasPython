def eh_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

numero_usuario = int(input("Digite um número para verificar se é primo: "))

if eh_primo(numero_usuario):
    print(f"O número {numero_usuario} é primo.")
else:
    print(f"O número {numero_usuario} não é primo.")


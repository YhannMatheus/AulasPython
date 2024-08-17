aluno = {}

while True:
    print("\n1. Adicionar estudante")
    print("2. Adicionar nota")
    print("3. Exibir estudantes e notas")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do estudante: ")
        if nome in aluno:
            print("Estudante já cadastrado.")
        else:
            aluno[nome] = []
            print(f"{nome} foi adicionado.")

    elif opcao == "2":
        nome = input("Digite o nome do estudante para adicionar a nota: ")
        if nome in aluno:
            nota = float(input("Digite a nota: "))
            aluno[nome].append(nota)
            print(f"Nota {nota} foi adicionada para {nome}.")
        else:
            print("Estudante não encontrado.")
    
    elif opcao == "3":
        print("\nEstudantes e suas Notas:")
        for nome, notas in aluno.items():
            print(f"{nome}: {notas}")
    
    elif opcao == "4":
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
computadores = []

while True:
    print("\n=== INVENTÁRIO DE COMPUTADORES ===")
    print("1 - Cadastrar computador")
    print("2 - Listar computadores")
    print("3 - Buscar computador")
    print("4 - Remover computador")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do computador: ")
        setor = input("Setor: ")
        computadores.append({"nome": nome, "setor": setor})
        print("Computador cadastrado!")

    elif opcao == "2":
        if not computadores:
            print("Nenhum computador cadastrado.")
        else:
            for i, c in enumerate(computadores):
                print(f"{i} - {c['nome']} ({c['setor']})")

    elif opcao == "3":
        busca = input("Digite o nome ou setor: ")
        for c in computadores:
            if busca.lower() in c["nome"].lower() or busca.lower() in c["setor"].lower():
                print(f"{c['nome']} - {c['setor']}")

    elif opcao == "4":
        indice = int(input("Número do computador: "))
        if 0 <= indice < len(computadores):
            computadores.pop(indice)
            print("Computador removido.")
        else:
            print("Índice inválido.")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
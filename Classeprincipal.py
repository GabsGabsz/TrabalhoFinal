while True:
    print("----------- MENU ---------------")
    print("1. Informar o caminho da imagem")
    print("2. Escolher o filtro a ser aplicado")
    print("3. Listar arquivos de imagens do diretório corrente")
    print("4. SAIR")

    escolha = int(input("Digite a opção desejada: "))
    print("\n")

    if escolha == 1:
        # imagem = #chamar a função
        print(f"Caminho da imagem informado: {image}")
    elif escolha == 2:
        # filtro_escolha = #chamar a função
        if filtro_escolha:
            print(f"Filtro escolhido: {filtro_escolha}")
    elif escolha == 3:
        #chamar a função
        pass
    elif escolha == 4:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")

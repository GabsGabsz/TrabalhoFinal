import DownloadImg
while True:
    print("----------- MENU ---------------")
    print("1. Informar o caminho da imagem")
    print("2. Escolher o filtro a ser aplicado")
    print("3. Listar arquivos de imagens do diretório corrente")
    print("4. SAIR")

    escolha = int(input("Digite a opção desejada: "))
    print("\n")

    match escolha:
        # imagem = #chamar a função
        case 1:
          DownloadImg.main()
          break
        case 2:
        # filtro_escolha = #chamar a função
            if filtro_escolha:
                print(f"Filtro escolhido: {filtro_escolha}")
        case 3:
        #chamar a função
            pass
        case 4:
       # print("Encerrando o programa.")
            break
        

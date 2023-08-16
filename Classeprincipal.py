import DownloadImg
import os
from Imagem import Imagem
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
        case 2:
        # filtro_escolha = #chamar a função
            if filtro_escolha:
                print(f"Filtro escolhido: {filtro_escolha}")
        case 3:
        #chamar a função
            diretorio_imagens_salvas = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imagens_salvas")
            if os.path.exists(diretorio_imagens_salvas):
                Imagem.listar_imagens(diretorio_imagens_salvas)  # Chamar o método listar_imagens da classe Imagem
            else:
                print("Nenhum diretório de imagens salvas encontrado.")
            pass
        case 4:
       # print("Encerrando o programa.")
            break
        

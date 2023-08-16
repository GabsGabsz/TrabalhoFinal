import os
class Imagem:
    
    def __init__(self, nome,caminho):
        self.nome = nome
        self.caminho = caminho
        
        
    def __str__(self):
        return f"Imagem: {self.nome}, Caminho: {self.caminho}"
    
    @staticmethod
    def listar_imagens(diretorio):
        imagens_encontradas = []

        for filename in os.listdir(diretorio):
            if filename.lower().endswith(('.jpg', '.png')):
                imagens_encontradas.append(filename)

        if imagens_encontradas:
            print("Imagens encontradas no diretório:")
            for imagem in imagens_encontradas:
                print(imagem)
        else:
            print("Nenhuma imagem do tipo .jpg ou .png encontrada.")

    def exibir(self):
        from PIL import Image
        try:
            img = Image.open(self.caminho)
            img.show()
        except Exception as e:
            print("Erro ao exibir a imagem:", e)
    def exibirPath(self):
        print(self.caminho)
    pass
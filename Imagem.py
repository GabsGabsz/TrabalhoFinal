
class Imagem:
    
    def __init__(self, nome,caminho):
        self.nome = nome
        self.caminho = caminho
        print(self.caminho,caminho)
        
    def __str__(self):
        return f"Imagem: {self.nome}, Caminho: {self.caminho}"

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
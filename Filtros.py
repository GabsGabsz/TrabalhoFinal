import os
import Imagem
from PIL import Image,ImageFilter


def FiltrosMenu():
    while True:
        print("----------- MENU DE FILTROS ---------------")
        print("1. escala de cinza")
        print("2. Preto e Branco")
        print("3. Filtro Cartoon")
        print("4. Foto Negativa")
        print("5. Contorno")
        print("6. Blurred")
        print("7. sair")

        escolha = int(input("Digite a opção desejada: "))
        print("\n")

        match escolha:

            case 1:
                end_image = input("Digite o caminho da imagem: ")
                filtro_escala_cinza = GrayScaleFilter(end_image)
                cinza_aplicado = filtro_escala_cinza.apply_filter()
                img = Image.open(cinza_aplicado)
                img.show()

                pass
            case 2:
            
                pass

            case 3:
            
                pass
            
            case 4:
                end_image = input("Digite o caminho da imagem: ")
                filtro_negativo = NegativeFilter(end_image)
                negativo_aplicado = filtro_negativo.apply_filter()
                img = Image.open(negativo_aplicado)
                img.show()
                
            
                pass

            case 5:
                end_image = input("Digite o caminho da imagem: ")
                filtro_contorno = ContourFilter(end_image)
                contorno_aplicado = filtro_contorno.apply_filter()
                img = Image.open(contorno_aplicado)
                img.show()
            
                pass
            case 6:
                end_image = input("Digite o caminho da imagem: ")
                filtro_blur = BlurredFilter(end_image)
                blur_aplicado = filtro_blur.apply_filter()
                img = Image.open(blur_aplicado)
                img.show()
            
                pass

            case 7:

                break
    if __name__ == "__main__":
        FiltrosMenu()

class GrayScaleFilter:

    def __init__(self, image_path):
        self.image_path = image_path

    def apply_filter(self):
        # Abra a imagem
        img = Image.open(self.image_path)
        # Converta a imagem para escala de cinza
        grayscale_image = img.convert("L")
        # Salve a imagem filtrada no mesmo local que a original,
        # com um sufixo '_grayscale'
        new_image_path = f"{self.image_path.rsplit('.', 1)[0]}_grayscale.{self.image_path.rsplit('.', 1)[1]}"
        grayscale_image.save(new_image_path)
        # Retorne o caminho da imagem filtrada
        return new_image_path
    
class NegativeFilter:

    def __init__(self, image_path):
        self.image_path = image_path

    def apply_filter(self):
        img = Image.open(self.image_path)
        negative_image = Image.eval(img, lambda px: 255 - px)
        new_image_path = f"{self.image_path.rsplit('.', 1)[0]}_negative.{self.image_path.rsplit('.', 1)[1]}"
        negative_image.save(new_image_path)
        return new_image_path 


class ContourFilter:

    def __init__(self, image_path):
        self.image_path = image_path

    def apply_filter(self):
        img = Image.open(self.image_path)
        contour_image = img.filter(ImageFilter.CONTOUR)
        new_image_path = f"{self.image_path.rsplit('.', 1)[0]}_contour.{self.image_path.rsplit('.', 1)[1]}"
        contour_image.save(new_image_path)
        return new_image_path
    
class BlurredFilter:

    def __init__(self, image_path):
        self.image_path = image_path

    def apply_filter(self):
        img = Image.open(self.image_path)
        blurred_image = img.filter(ImageFilter.BLUR)
        new_image_path = f"{self.image_path.rsplit('.', 1)[0]}_blurred.{self.image_path.rsplit('.', 1)[1]}"
        blurred_image.save(new_image_path)
        return new_image_path

 
               
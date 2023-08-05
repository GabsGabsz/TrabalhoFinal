
import os
import requests
import Imagem
class ImageDownloader:
    def __init__(self, save_path):
        self.save_path = save_path
        self.allowed_extensions = ['.png', '.jpg']
        self.image_path = ""

    def download_image(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            if content_type.startswith('image'):
                extension = os.path.splitext(url)[1].lower()
                if extension in self.allowed_extensions:
                    image_name = os.path.basename(url)
                    self.image_path = os.path.join(self.save_path, image_name)
                    with open(self.image_path, 'wb') as f:
                        f.write(response.content)
                    
                    print(f"Imagem salva como: {self.image_path}")
                else:
                    print("Formato de imagem não suportado. Use .png ou .jpg")
            else:
                print("O URL fornecido não aponta para uma imagem.")
        else:
            print("Falha ao baixar a imagem. Verifique o URL fornecido.")
        return self.image_path
    
def  main():
    save_directory = r"D:\teste"
    downloader = ImageDownloader(save_directory)

    image_url = input("Digite o URL da imagem: ")
    caminho = downloader.download_image(image_url)
    nova_imagem = Imagem.Imagem("Nova imagem",caminho)
    nova_imagem.exibirPath()
    nova_imagem.exibir()

main()

import os
import requests
import Imagem
class ImageDownloader:
    def __init__(self, save_path):
        self.save_path = save_path
        self.allowed_extensions = ['.png', '.jpg']
        self.image_path = ""
    
    def verifica_Caminho(self, caminhoDownload):

        externalUrl=["https:","http:"]
        listaurl2 = caminhoDownload.split("//")
        if(listaurl2[0] not in externalUrl):
            print("Link interno")
            return True
        else:
            print("Link externo")
            return False
        

    def download_image(self, url):
        if( self.verifica_Caminho(url.strip())):
            return url
        
        try:   
            response = requests.get(url)
            response.raise_for_status()
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
            return self.image_path
        except requests.exceptions.RequestException as e:
            print("Erro ao fazer a solicitação HTTP:", e)
            return None
        except Exception as e:
            print("Erro não esperado:", e)
            return None
    
def  main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    save_directory = os.path.join(current_directory, "imagens_salvas")
    os.makedirs(save_directory, exist_ok=True)
    downloader = ImageDownloader(save_directory)
    image_url = input("Digite o URL da imagem: ")
    caminho = downloader.download_image(image_url)
    nova_imagem = Imagem.Imagem("Nova imagem",caminho)
    nova_imagem.exibir()

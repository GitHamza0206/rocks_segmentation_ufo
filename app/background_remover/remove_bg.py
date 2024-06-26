import requests
from io import BytesIO

class BackgroundRemover:
    def __init__(self,image_path=None):
        self.image_path = image_path
        self.api_key= "VJ5PaysdeSEuL4TvmdXKsxdS"

    def remove_background(self):
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(image_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': self.api_key},
        )
        if response.status_code == requests.codes.ok:
            print(response.content)
            with open('no-bg.png', 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)

    def resize_image(self, image, size=(1024, 1024)):
        return image.resize(size)

    def remove_bg(self, image, save_path='no-bg.png'):
        image = self.resize_image(image)
        buffer = BytesIO()
        image = image.convert('RGB')
        image.save(buffer, format='JPEG')
        image_bytes = buffer.getvalue()
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': image_bytes},
            data={'size': 'auto'},
            headers={'X-Api-Key': self.api_key},
        )
        if response.status_code == requests.codes.ok:
            return response.content
        else:
            print("Error:", response.status_code, response.text)
            return response.text

# Usage example
if __name__=="__main__":
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    image_path = os.path.join(parent_dir, 'samples/original/AkerBPSample2.jpeg')

    background_remover = BackgroundRemover(image_path)
    background_remover.remove_background()
    print("Background removed image saved as no-bg.png")
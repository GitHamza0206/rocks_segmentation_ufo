import requests

class BackgroundRemover:
    def __init__(self,image_path ):
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
            with open('no-bg.png', 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)

# Usage example
if __name__=="__main__":
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    image_path = os.path.join(parent_dir, 'samples/original/AkerBPSample2.jpeg')

    background_remover = BackgroundRemover(image_path)
    background_remover.remove_background()
    print("Background removed image saved as no-bg.png")
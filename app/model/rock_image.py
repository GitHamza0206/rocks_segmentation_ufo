import numpy as np
from PIL import Image

class RockImages:
    def __init__(self, image_path, background_removed_image_path=None, segmented_image_path=None):
        self.image_path = image_path
        self.background_removed_image_path = background_removed_image_path
        self.segmented_image_path = segmented_image_path

        self.image = self.get_numpy_image()

    def get_numpy_image(self):
        return np.array(Image.open(self.image_path))


    def get_dimensions(self):
        height, width, channels= self.image.shape
        return height, width 
    

if __name__ == "__main__":
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, '../samples/AkerBPSample9.png')
    rock_image = RockImages(image_path)
    print(rock_image.image_path)
    print(rock_image.image)
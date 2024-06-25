from PIL import Image
from landingai.predict import Predictor

class LandingAIInference:
    def __init__(self, image_path):
        self.image_path = image_path
        self.endpoint_id  = "956ce397-e8ca-495c-a2d3-5c2688c2cf1c"
        self.api_key = "land_sk_aWYXkMg9VBg0g9j2xNoxGTI4EyxT8cEzTpQ4Cqd6QcCCUdDVI4"
        self.predictor = Predictor(self.endpoint_id, api_key=self.api_key)

    def load_image(self):
        # Load your image
        image = Image.open(self.image_path)
        return image


    def run_inference(self, image):
        # Run inference
        image = self.load_image()
        predictions = self.predictor.predict(image)
        return predictions

if __name__ == "__main__":
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    image_path = os.path.join(parent_dir, 'samples/original/AkerBPSample2.jpeg')
    landingai_inference = LandingAIInference(image_path)
    print(landingai_inference.run_inference(image_path))
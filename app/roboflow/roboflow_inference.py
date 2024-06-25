from roboflow import Roboflow

rf = Roboflow(api_key="API_KEY")
project = rf.workspace().project("MODEL_ENDPOINT")
model = project.version(VERSION).model

# infer on a local image
print(model.predict("your_image.jpg").json())

# infer on an image hosted elsewhere
print(model.predict("URL_OF_YOUR_IMAGE").json())

# save an image annotated with your predictions
model.predict("your_image.jpg").save("prediction.jpg")
class RoboflowInference:
    def __init__(self, api_key, model_endpoint, version):
        self.rf = Roboflow(api_key=api_key)
        self.project = self.rf.workspace().project(model_endpoint)
        self.model = self.project.version(version).model

    def infer_local_image(self, image_path):
        return self.model.predict(image_path).json()

    def infer_remote_image(self, image_url):
        return self.model.predict(image_url).json()

    def save_annotated_image(self, image_path, output_path):
        self.model.predict(image_path).save(output_path)
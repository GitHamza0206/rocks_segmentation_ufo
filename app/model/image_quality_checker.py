
class ImageQualityChecker:
    def __init__(self, image: Image):
        self.image = image

    def is_good_quality(self) -> bool:
        return self.image.size > 1000
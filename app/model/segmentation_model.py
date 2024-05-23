from .__init__ import *

from segment_anything import sam_model_registry, SamPredictor
from .background_remover import unet_model
from .grain_analysis import GrainAnalysis
from .rock_image import RockImages

from huggingface_hub import hf_hub_download

class SegmentUFO:
    def __init__(self,image_path, object_dim_mm, object_dim_px):
        self.predictor, self.sam = self.initialize_segmentation_model()
        self.grain_analysis = GrainAnalysis()
        self.rock_image =  RockImages(image_path)
        self.model = unet_model()
        
        self.image = self.rock_image.image
        height, width = self.rock_image.get_dimensions()
        scale = object_dim_mm/object_dim_px
        self.scale = height*scale


    def initialize_segmentation_model(self):
        #sam_checkpoint = "sam_vit_h_4b8939.pth"
        #sam_checkpoint = hf_hub_download("ybelkada/segment-anything", "checkpoints/sam_vit_h_4b8939.pth")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sam_checkpoint = os.path.join(current_dir, '../weights/sam_vit_h_4b8939.pth')
        device = "cuda"
        model_type = "default"

        sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
        sam.to(device=device)
        predictor = SamPredictor(sam)
        
        return predictor, sam
    
    def segment_image(self):
        big_im = self.image
        model = self.model
        sam = self.sam 
        scale = self.scale

        big_im_pred = seg.predict_big_image(big_im, model, I=256)
        # decreasing the 'dbs_max_dist' parameter results in more SAM prompts (and longer processing times):
        labels, grains, coords = seg.label_grains(big_im, big_im_pred, dbs_max_dist=10.0)
        all_grains, labels, mask_all, grain_data, fig, ax = seg.sam_segmentation(sam, big_im, big_im_pred, coords, labels, min_area=50.0)
        grain_data = self.grain_analysis.update_grain_data(grain_data, scale)
        return all_grains, labels, mask_all, grain_data, fig, ax




if __name__=="__main__":
    import os 
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, '../samples/AkerBPSample9.png')
    segment_ufo = SegmentUFO(image_path, 10, 100)
    all_grains, labels, mask_all, grain_data, fig, ax = segment_ufo.segment_image()
    segment_ufo.grain_analysis.show_segmentation_result(segment_ufo.image, all_grains, labels, mask_all,grain_data,fig, ax)

    print("Segmentation completed successfully!")
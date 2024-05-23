        
if __name__ == '__main__':
    from huggingface_hub import hf_hub_download
    from .segmentation_model import SegmentUFO
    import os 
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, '../samples/AkerBPSample9.png')
    segment_ufo = SegmentUFO(image_path, 10, 100)
    p,s = segment_ufo.initialize_segmentation_model()
    print(p,s)


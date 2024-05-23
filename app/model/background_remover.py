from .__init__ import *

def unet_model():
    model = seg.Unet()
    model.compile(optimizer=Adam(), loss=seg.weighted_crossentropy, metrics=["accuracy"])
    model.load_weights('./checkpoints/seg_model')
    return model


if __name__ == '__main__':
    # Example usage
    print(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}))
    print('Hello, world!')


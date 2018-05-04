from PIL import Image
from cropImage import cropImage
import numpy as np

im = np.asarray(Image.open("/Users/halmawi/Downloads/og.png"))
bbox = [0,0,100,100]
im_new = cropImage(im,bbox)
img = Image.fromarray(im_new, 'RGB')
img.save("/Users/halmawi/Downloads/test.png")
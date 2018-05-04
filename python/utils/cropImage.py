import numpy as np
from scipy.misc import imresize
import math

def cropImage(im, bbox):
	w = bbox[2]-bbox[0]+1
	h = bbox[3]-bbox[1]+1
	im = np.stack([np.pad(im[:,:,c], ((h,),(w,)), mode='constant') for c in range(3)], axis=2)
	im1 = im[(bbox[0]+h):(bbox[0]+h*2),(bbox[1]+w):(bbox[1]+w*2),:]
	im1 = imresize(im1, (200, 200))
	return im1
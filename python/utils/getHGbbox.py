def getHGbbox(center, scale):
	ul = transform([1,1],center,scale,[256,256],1)
	br = transform([257,257],center,scale,[256,256],1)
    bbox = [ul[0], ul[1], br[0], br[1]]
    return bbox

def transform(pt,center, scale, res, invert):
	t = get_transform(center, scale, res)
	if invert == 1:
		t = np.linalg.inv(t)
	new_pt = [[pt[0]-1],[pt[1]-1],[1]]
	new_pt = 
	return new_pt

def get_transform(center,scale,res):
	h = 200*scale
	t = np.identity(3)
	t[0][0] = res[1]/h
	t[1][1] = res[0]/h
	t[0][2] = res[1]*(-1*center[0]/h + 0.5)
	t[1][2] = res[0]*(-1*center[1]/h + 0.5)
	t[2][2] = 1
	return t
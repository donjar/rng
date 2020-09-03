from PIL import Image
import numpy as np

def list_to_image(l, name="a.png", size=30):
    ls_unfl = [[[0, 0, 255] if i == 0 else [255, 255, 0]] * size for i in l]
    ls = [[x for s in ls_unfl for x in s]] * size
    img = Image.fromarray(np.array(ls, dtype=np.uint8), mode='RGB')
    img.save(name)

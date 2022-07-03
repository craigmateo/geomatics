##########################
### generate rgb image ###
##########################

from spectral import *
from _readfile import *

img = read(folder, hdrFile, imgFile)

#view = imshow(img,bands=(58,34,19),stretch=0.05,title="RGB Image")

save_rgb("rgb.jpg", img, bands=(30, 20, 10))
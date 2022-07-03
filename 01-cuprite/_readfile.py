#####################
### Read hsi file ###
#####################

import spectral.io.envi as envi

# directory and files containing spectral data
folder = "D:/Datasets/Terra_Cuprite/University of Waterloo/"
hdrFile = "20210821175814003001_mosaic_resample.hdr"
imgFile = "20210821175814003001_mosaic_resample.img"

def read(folder, hdr, img):
    img = envi.open(folder + hdr, folder + img)
    return img
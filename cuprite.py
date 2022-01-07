from spectral import *
import spectral.io.envi as envi
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import wx
spectral.settings.WX_GL_DEPTH_SIZE = 16

# directory containing spectral data
folder = "C:/GIS/University of Waterloo/"

img = envi.open(folder + '20210821175814003001_mosaic_resample.hdr',
                folder + '20210821175814003001_mosaic_resample.img')

# set the Water Vapor Band windows to NaN 
img.bands.centers[191:211]==np.nan
img.bands.centers[281:314]==np.nan
img.bands.centers[-10:]==np.nan

# print metadata contents
md = img.metadata
print('Metadata Contents:')
for item in md:
    print('\t',item)

print('description:',md['description'])
print('map info:',md['map info'])

#print(md['wavelength'])
print('Number of Bands:',len(md['wavelength']))

print('First 3 Band Center Wavelengths:',img.bands.centers[:3])
print('Last 3 Band Center Wavelengths:',img.bands.centers[-3:])

#view = imshow(img,bands=(58,34,19),stretch=0.05,title="RGB Image")
#save_rgb("rgb.jpg", img, bands=(30, 20, 10))

# view_cube -- blank canvas showing
#view_cube(img,bands=[29, 19, 9])
#input("Press Enter to continue...")

bands = np.genfromtxt('C:/GIS/University of Waterloo/bands.csv', delimiter=',')

# get spectral signiture for a specific pixel

pixel_y = 500
pixel_x = 200

pixel = img[
    pixel_y:pixel_y+1,
    pixel_x:pixel_x+1,
    :]

print("Shape: ", img.shape)
print("Datatype: ", img.dtype)
print(pixel)


pixel_squeezed = np.squeeze(pixel)

plt.plot(bands, pixel_squeezed)
plt.title('Spectral Footprint\n(Pixel {},{})'.format(
    pixel_x, pixel_y))
plt.xlabel('Wavelength')
plt.ylabel('Reflectance')
#plt.show()

# k-means clustering
""" valid_band_range = [i for j in (range(0,191), range(212, 281), range(315,415)) for i in j] #remove water vapor bands
img_subset = img.read_subimage(range(400,600),range(400,600),bands=valid_band_range) #subset image by area and bands
(m,c) = kmeans(img_subset,5,50)  """
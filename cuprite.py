from spectral import *
import spectral.io.envi as envi
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import wx
spectral.settings.WX_GL_DEPTH_SIZE = 16
import os
from scipy.spatial.distance import directed_hausdorff
import similaritymeasures

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

#print(lib.names[:5])

bands = np.genfromtxt('C:/GIS/University of Waterloo/bands.csv', delimiter=',')

import os

# get spectral signiture for a specific pixel
pixel_y = 500
pixel_x = 200

#print(type(img))
pixel = img[
            pixel_y:pixel_y+1,
            pixel_x:pixel_x+1,
            :]

pixel_squeezed = np.squeeze(pixel)

dumimage =img[
            0:,
            0:,
            0:0]

plt.imshow(dumimage, interpolation='nearest')
plt.show()


print(type(dumimage))

Q = np.array([bands,pixel_squeezed]).T

# ecostress data
minname = ""
minsim = 10000

""" directory = os.fsencode("ecospeclib")
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if "spectrum" in filename:
        x = []
        y = []  
        with open("ecospeclib/"+filename) as f:
            data = f.read()
            data = data.split('\n')
            name = data[0].split(':')
            name = name[1]
            print(name)
            data = data[21:]
            for point in data:
                point = point.split('\t')
                if len(point)>1:
                    xi = float(point[0].strip())
                    yi = float(point[1].strip())
                    if xi > 2 and xi <= 2.5:
                        x.append(xi*1000)
                        y.append(yi)
            P = np.array([x,y]).T
            #similarity
            #dh, ind1, ind2 = directed_hausdorff(P, Q)
            #df = similaritymeasures.frechet_dist(P, Q)
            #dtw, d = similaritymeasures.dtw(P, Q)
            pcm = similaritymeasures.pcm(P, Q)
            #area = similaritymeasures.area_between_two_curves(P, Q)
            #cl = similaritymeasures.curve_length_measure(P, Q)
            # all methods will return 0.0 when P and Q are the same
            # partial curve mapping
            if pcm < minsim:
                minsim=pcm
                minname=name """

print("################")
#print(minname)

""" plt.plot(x, y)
plt.title(name)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflectance (percent)')
plt.savefig(name)
plt.show()
plt.clf() """
        
plt.plot(bands, pixel_squeezed)
plt.title('Spectral Footprint\n(Pixel {},{})'.format(
        pixel_x, pixel_y))
plt.xlabel('Wavelength')
plt.ylabel('Reflectance')
file = str(pixel_y)+ "_" + str(pixel_x)
name = file + ".png"
#print(name)
plt.xlim([2000, 2500])
plt.ylim([0, 10])
#plt.show()
#plt.savefig(name)
plt.clf()

""" 
for y in range(0, 1083):
    pixel_y = y
    for x in range(0,396):
        pixel_x = x

        pixel = img[
            pixel_y:pixel_y+1,
            pixel_x:pixel_x+1,
            :]

        #print("Shape: ", img.shape)
        #print("Datatype: ", img.dtype)
        #print(type(pixel[0][0]))
        if not np.all(pixel[0][0]==0):
            pixel_squeezed = np.squeeze(pixel)
            plt.plot(bands, pixel_squeezed)
            plt.title('Spectral Footprint\n(Pixel {},{})'.format(
                pixel_x, pixel_y))
            plt.xlabel('Wavelength')
            plt.ylabel('Reflectance')
            file = str(y)+ "_" + str(x)
            name = "images/" + file + ".png"
            print(name)
            plt.savefig(name)
            plt.clf()
            #plt.show() """

# k-means clustering
""" valid_band_range = [i for j in (range(0,191), range(212, 281), range(315,415)) for i in j] #remove water vapor bands
img_subset = img.read_subimage(range(400,600),range(400,600),bands=valid_band_range) #subset image by area and bands
(m,c) = kmeans(img_subset,5,50)  """
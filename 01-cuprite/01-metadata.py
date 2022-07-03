####################
### get metadata ###
####################

from _readfile import *

img = read(folder, hdrFile, imgFile)

# print metadata contents
md = img.metadata
print('\n')
print('METADATA')
print('--------')
for item in md:
    print(item)

print('\n')

# expand metadata details for description & map info
print('DESCRIPTION')
print('--------')
print(md['description'].strip())
print('\n')
print('MAP INFO')
print('--------')
print(md['map info'])

# get no. of bands
print('\n')
print('NO. OF BANDS')
print('--------')
print(len(md['wavelength']))

# get first & last bands
print('\n')
print('FIRST & LAST BANDS')
print('--------')
print('First 3 Band Center Wavelengths:',img.bands.centers[:3])
print('Last 3 Band Center Wavelengths:',img.bands.centers[-3:])

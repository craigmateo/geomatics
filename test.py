import codecs

folder = "C:/GIS/University of Waterloo/"
filename = folder+'20210821175814003001_00000000_resample.img' 

# Example: convert bytes to a String, using the built-in decode() method for the bytes class (from https://stackabuse.com/convert-bytes-to-string-in-python/)
""" b = b"Lets grab a \xf0\x9f\x8d\x95!"
print(type(b))
s = b.decode('UTF-8')
print(s) """

file = open(filename, "rb")

byte = file.read(1)

while byte:
    s = byte.decode('UTF-8',errors="ignore")
    print(s)
    byte = file.read(1)

file.close()

lines = []
with open(filename, 'rb') as image: 
    for line in image:
        #s = codecs.decode(line, 'UTF-8',errors="ignore")
        s = line.decode('UTF-8',errors="ignore")
        lines.append(s)

#print(lines[1].replace("\\x00",""))



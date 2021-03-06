#!/usr/bin/python
import os, sys
import Image, ImageChops

#get a list of files
lista = []
for root, dirs, files in os.walk('.'):
	for f in files:
		#print os.path.splitext(os.path.join(root,f))
		if f.rpartition(".")[2] == "jpg":
			lista.append(f)
lista.sort()
print(lista)

#create a new list for selected frames
lista2 = []

#start substracting frames in order
image1 = Image.open(lista[0])
for i in range(len(lista)-1):

	try:
		diferente = True
		image2= Image.open(lista[i+1])
		dif = ImageChops.subtract(image1, image2)
		
		# number of pixels in the image (width x height)
		pixels = dif.size[0]*dif.size[1]

		#[0][256]&[512] are black values from R G and B channel, all 3 must be equal to the
		#                     number of pixels in the image for the image to be full black
		if dif.histogram()[0] == dif.histogram()[256] == dif.histogram()[512] == pixels:
			diferente = False
		if not diferente:
			print("same frame")
		else:
			print("diferent frame: ",image1.filename, image2.filename)
			lista2.append(image1)
			image1 = Image.open(lista[i+1])
	except IOError:	
		print ("some image read error")

#create a directory to send diferent frames
filename = "./frame_diference/filename.txt"
dir = os.path.dirname(filename)
if not os.path.exists(dir):
	os.makedirs(dir)

# save the selected frames in a new directory
for i in lista2: 
	print(i.filename)
	i.save("./frame_diference/"+i.filename)

import vigra
import numpy
import damascene

img = vigra.impex.readImage("lena.jpg")
img = img.astype(numpy.uint8)

borders, textons, orientations = damascene.damascene(img)

vigra.impex.writeImage(borders, "lena_gpb.png")


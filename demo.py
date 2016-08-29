#from PIL import Image
#img = Image.open("/home/jairo/Documents/tmpDesarrollos/HypCam/snapshots/Cinves/27_08_2016/IRis/bloque1.png")
#img.show()

#Headers
from PIL import Image
import numpy as numpy

#Definitions
red, green, blue = 0, 1, 2

#Import image
idBloque 	= 4;
img 		= Image.open("/home/jairo/Documents/tmpDesarrollos/HypCam/snapshots/Cinves/27_08_2016/IRis/bloque" + str(idBloque) + ".png" )
img 		= img.convert('RGB')
imgW, imgH 	= img.size
imgMatrix 	= numpy.array(img)

#Isolate channels
imgR = Image.fromarray(imgMatrix[:,:,red])
imgG = Image.fromarray(imgMatrix[:,:,green])
imgB = Image.fromarray(imgMatrix[:,:,blue])

#Save isolated channels
if True:
	imgR.convert('L').save( "./Results/Bloque" + str(idBloque) + "/Red.tif" )
	imgG.convert('L').save( "./Results/Bloque" + str(idBloque) + "/Green.tif" )
	imgB.convert('L').save( "./Results/Bloque" + str(idBloque) + "/Blue.tif" )

#Cast into float in order to make division possible
IR 	= imgMatrix[:,:,red].astype(float)		#Cast into float
R 	= imgMatrix[:,:,blue].astype(float)		#Cast into float
G 	= imgMatrix[:,:,green].astype(float)	#Cast into float
numpy.seterr(invalid='ignore') 			#Ignore zero division

#------------------------------------------------------------------
# NDVI range(-1 to 1)
#------------------------------------------------------------------
#Calculate NDVI
NDVI 			= (IR-R)/(IR+R)
print "Before Max: " + str(numpy.amax(NDVI))
print "Before Average: " + str(numpy.average(NDVI))
print "Before Min: " + str(numpy.amin(NDVI))

#Transform into a displayable
lstNonV				= NDVI <= 0.0
lstVeg				= NDVI > 0.0
NDVI2Show			= NDVI + numpy.amin(NDVI)
NDVI2Show			= NDVI2Show / numpy.amax(NDVI)
NDVI2Show			= NDVI2Show * 255.0		#Set NDVY into grayscale
NDVI2Show[lstNonV]	= 0.0

#Delete non vegetation (NV) pixels
NDVI[lstNonV]		= 0.0
print "\n"
print "After Max: " + str(numpy.amax(NDVI[lstVeg]))
print "After Average: " + str(numpy.average(NDVI[lstVeg]))
print "After Min: " + str(numpy.amin(NDVI[lstVeg]))

#Generate image as red gradient color
imgNDVI 			= imgMatrix
imgNDVI[:,:,red] 	= NDVI2Show
imgNDVI[:,:,green] 	= 0
imgNDVI[:,:,blue] 	= 0
imgNDVI 			= Image.fromarray(imgNDVI)
imgNDVI.save( "./Results/Bloque" + str(idBloque) + "/NDVI_Bloque" + str(idBloque) + ".png" )
imgNDVI.save( "./Results/NDVI_Bloque" + str(idBloque) + ".png" )
#------------------------------------------------------------------


print 'It finishes successfully'



exit

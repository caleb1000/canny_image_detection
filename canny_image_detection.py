from PIL import Image
import math
#I really should use numpy in the future

def convert(list):
    return tuple(i for i in list)


im = Image.open('bank.png') # Can be many different formats.
copy = Image.open('bank.png') # Can be many different formats.
im2 = Image.open('bank.png')
im3 = Image.open('bank.png')
#pretty terrible having to open an image up three times. Should just use one
pix = im.load()
pix2 = im2.load()
pix3 = im3.load()
co = copy.load()

#print (im.size)  # Get the width and hight of the image for iterating over
#print (pix[x,y])  # Get the RGBA Value of the a pixel of an image
#print (pix[x,y][0]) how to get tubles rgb values
#print (pix[x,y][1])
#print (pix[x,y][2])
x = 0;
y = 0;

#please note this ignores the boarder of an image, I will fix this later but for now it should be fine
for x in range(im.width-2):
    x = x+1;
    for y in range(im.height-2):
        temp = []
        y = y+1;

        #canny edge?
        #first we apply a blur
        temp.append(int((.1*co[x-1,y][0] +.1*co[x+1,y][0] +.1*co[x,y-1][0] + .1*co[x,y+1][0] + .1*co[x-1,y-1][0] +.1*co[x+1,y+1][0] +.1*co[x-1,y+1][0] +.1*co[x+1,y-1][0] + .2*co[x,y][0])))
        temp.append(int((.1*co[x-1,y][1] +.1*co[x+1,y][1] +.1*co[x,y-1][1] + .1*co[x,y+1][1] + .1*co[x-1,y-1][1] +.1*co[x+1,y+1][1] +.1*co[x-1,y+1][1] +.1*co[x+1,y-1][1] + .2*co[x,y][1])))
        temp.append(int((.1*co[x-1,y][2] +.1*co[x+1,y][2] +.1*co[x,y-1][2] + .1*co[x,y+1][2] + .1*co[x-1,y-1][2] +.1*co[x+1,y+1][2] +.1*co[x-1,y+1][2] +.1*co[x+1,y-1][2] + .2*co[x,y][2])))
        co[x,y] = convert(temp)

for x in range(im.width-2):
    x = x+1;
    for y in range(im.height-2):
        y = y+1;
        temp = []
        #https://www.dynamsoft.com/blog/insights/image-processing/image-processing-101-color-space-conversion/
        #turn image to greyscale using special constants based on human eyes
        temp.append(int(co[x,y][0]*0.299 + co[x,y][1]*0.587 + co[x,y][2]*0.114))
        #temp[0] = int(temp[0]*0.333 + temp[1]*0.333 + temp[2]*0.333) this is if we do an even average of colors
        temp.append(temp[0])
        temp.append(temp[0])
        co[x,y] = convert(temp)

for x in range(im.width-2):
    x = x+1;
    for y in range(im.height-2):
        temp = []
        y = y+1;

        #https://www.youtube.com/watch?v=uihBwtPIBxM
        # Sobel x
        # -1,0,1
        # -2,0,2
        # -1,0,1
        #do it for rgb even though it is greyscale

        sobel_x = []
        sobel_x.append(int((-2*co[x-1,y][0] +2*co[x+1,y][0] +0*co[x,y-1][0] + 0*co[x,y+1][0] + -1*co[x-1,y-1][0] +1*co[x+1,y+1][0] +-1*co[x-1,y+1][0] +1*co[x+1,y-1][0] + 0*co[x,y][0])))
        sobel_x.append(int((-2*co[x-1,y][0] +2*co[x+1,y][0] +0*co[x,y-1][0] + 0*co[x,y+1][0] + -1*co[x-1,y-1][0] +1*co[x+1,y+1][0] +-1*co[x-1,y+1][0] +1*co[x+1,y-1][0] + 0*co[x,y][0])))
        sobel_x.append(int((-2*co[x-1,y][0] +2*co[x+1,y][0] +0*co[x,y-1][0] + 0*co[x,y+1][0] + -1*co[x-1,y-1][0] +1*co[x+1,y+1][0] +-1*co[x-1,y+1][0] +1*co[x+1,y-1][0] + 0*co[x,y][0])))

        pix[x,y] = convert(sobel_x)

        # Sobel y
        # -1,-2,-1
        # 0,0,0
        # 1,2,1

        sobel_y = []
        sobel_y.append(int((0*co[x-1,y][0] +0*co[x+1,y][0] +-2*co[x,y-1][0] + 2*co[x,y+1][0] + -1*co[x-1,y-1][0] +1*co[x+1,y+1][0] +1*co[x-1,y+1][0] +-1*co[x+1,y-1][0] + 0*co[x,y][0])))
        sobel_y.append(int((0*co[x-1,y][0] +0*co[x+1,y][0] +-2*co[x,y-1][0] + 2*co[x,y+1][0] + -1*co[x-1,y-1][0] +1*co[x+1,y+1][0] +1*co[x-1,y+1][0] +-1*co[x+1,y-1][0] + 0*co[x,y][0])))
        sobel_y.append(int((0*co[x-1,y][0] +0*co[x+1,y][0] +-2*co[x,y-1][0] + 2*co[x,y+1][0] + -1*co[x-1,y-1][0] +1*co[x+1,y+1][0] +1*co[x-1,y+1][0] +-1*co[x+1,y-1][0] + 0*co[x,y][0])))

        pix2[x,y] = convert(sobel_y)

        int_temp = int(pix[x,y][0])*int(pix[x,y][0]) + int(pix2[x,y][0])*int(pix2[x,y][0])

        avg = []
        avg.append(math.isqrt(int_temp))
        avg.append(math.isqrt(int_temp))
        avg.append(math.isqrt(int_temp))
        pix3[x,y] = convert(avg)

copy.save('blurred_greyscale.png')
im.save('sobel_x.png')  # Save the modified pixels as .png
im2.save('sobel_y.png')
im3.save('sobel_avg.png')

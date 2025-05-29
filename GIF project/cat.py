import imageio.v3 as iio 
Pname = ['nyan-cat1.png','nyan-cat2.png','nyan-cat3.png']
images = []
for f in Pname :
    images.append(iio.imread(f))
iio.imwrite('cat.gif',images, duration = 100 , loop = 0)

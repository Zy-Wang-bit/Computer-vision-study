from PIL import Image
from pylab import *
import numpy as np


def histeq(im, nbr_bins=256):
    imhist, bins = np.histogram(im.flatten(), nbr_bins)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    im2 = np.interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf


def main():
    im = np.array(Image.open('..\data\Eyja.jpg').convert('L'))
    im2, cdf = histeq(im)
    imshow(im2)
    show()


if __name__ == '__main__':
    main()

from PIL import Image
from pylab import *
import numpy as np
from scipy.ndimage import filters


def main():
    im = np.array(Image.open('..\data\Eyja.jpg'))

    im2 = np.zeros(im.shape)
    figure()
    for i in range(3):
        im2[:, :, i] = filters.gaussian_filter(im[:, :, i], 5)
    im2 = im2 / 255
    imshow(im2)
    show()


if __name__ == '__main__':
    main()

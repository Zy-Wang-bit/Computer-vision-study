from PIL import Image
from pylab import *
import numpy as np


def main():
    im = np.array(Image.open('..\data\Eyja.jpg').convert('L'))

    figure()
    gray()
    contour(im, origin='image')
    axis('equal')
    axis('off')

    figure()
    hist(im.flatten(), 128)
    show()


if __name__ == '__main__':
    main()

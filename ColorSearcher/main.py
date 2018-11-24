"""
date: Nov 11, 23
author: @BrendanMoore42

Image to Hex colours

Feed in an image and returns a list of the Hex colour values and names for that colour.
"""
#image imports
import sys
import requests
import numpy as np
import pandas as pd
from PIL import Image

#plotting imports
import matplotlib
import matplotlib.image as mpimg
matplotlib.use("TkAgg")
matplotlib.rcParams['interactive'] == True
import matplotlib.pyplot as plt

img = Image.open('test.jpg')

rgb_im = img.convert('RGB')
print(rgb_im)
plt.imshow(rgb_im)
plt.show()



# # image_test = plt.imshow('test.jpg')
# image_test = Image.open('test.jpg')
# image_test.load()
# # plt.imshow(image_test)
# # plt.show()


def main(image):
    """

    :param image:
    :return:
    """

    #grab image
    #image = requests.get(image)

    #image = np.asarray(image, dtype='int32')

    # print(image[500])
    # for i in image:
    #     print(i, '\n\n')
    #
    # plt.imshow(image)
    # plt.show()

    # plt.imshow(image)
    # print(type(image))
    # plt.show()
    pass

if __name__ == '__main__':
    # main(sys.argv)
    main(img)
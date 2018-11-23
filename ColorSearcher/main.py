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
matplotlib.use("TkAgg")
matplotlib.rcParams['interactive'] == True
import matplotlib.pyplot as plt

# image_test = plt.imshow('test.jpg')
image_test = Image.open('test.jpg')
image_test.load()
# plt.imshow(image_test)
# plt.show()

def main(image):
    """

    :param image:
    :return:
    """

    #grab image
    #image = requests.get(image)


    image = np.asarray(image, dtype='int32')

    print(image[0])


    image = image[0]
    plt.show(image[0])

    # plt.imshow(image)
    # print(type(image))
    # plt.show()


if __name__ == '__main__':
    # main(sys.argv)
    main(image_test)
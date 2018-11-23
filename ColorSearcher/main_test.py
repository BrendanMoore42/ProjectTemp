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
image_test = np.asarray('./test.jpg')
plt.show(image_test)

def main(image):
    """

    :param image:
    :return:
    """

    #grab image
    #image = requests.get(image)

    #plt.imshow(image)
    pass






if __name__ == '__main__':
    # main(sys.argv)
    main(image_test)
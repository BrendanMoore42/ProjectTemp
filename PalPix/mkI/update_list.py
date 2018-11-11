# import packages, credentials
import re
import sys
import time
import pickle
import numpy as np
import pandas as pd
import urllib.request

# import selenium webdriver and exceptions
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementNotVisibleException

# disable chained warnings
pd.options.mode.chained_assignment = None

# set parameters
url = 'https://uproxx.com/tv/best-netflix-original-series-to-watch-right-now-ranked/'
host_site = 'wordpress.com'  # ex. wordpress.com
topic = 'curly hair'  # ex. fashion
# store links
blogs = []


# set random sleep function to randomize link click time
def random_sleep(multiplier=1, verbose=False):
    """
    This function goes between various actions to give the browser time to load and
    prepare html for parsing.
    :multiplier: Extends time by number, default is 1
    :verbose: if True function will display how long it's sleeping
    """
    i = np.random.randint(2, 6)
    i = i * multiplier
    if verbose:
        print(f'sleeping for {i} seconds')
    time.sleep(i)


def scrape(url):
    """
    Opens google and searches for blogs with specified topic, scrolls through pages and
    extracts html links for each blog and outputs a list.

    Async elements may differ but can be sourced from the browser inspector. Where the
    click is intended search for <class='element_here'>.
    """

    # set list of dictionaries for data export
    page_links = []

    # set webddriver to chrome
    # can be Chrome(), Safari(), Firefox()
    print('Preparing driver...\n')
    driver = webdriver.Chrome()
    random_sleep()

    # collect links from href
    driver.get(url)
    # links = driver.find_elements_by_xpath("//*[@href]")
    random_sleep()

    print('Getting links...')
    # try:
    cite_list = driver.find_elements_by_tag_name('cite')
    desc_list = driver.find_elements_by_class_name('st')
    # caption_list = driver.find_elements_by_tag_name('p')
    for cite, desc in zip(cite_list, desc_list):
        x = cite.text
        x = x.split('.com/')[0]
        x = x + '.com'
        y = desc.text

        # print(x, y)

        blog_data = {'blog': x, 'desc': y}
        page_links.append(blog_data)

    # except:
    #         print('No caption...')

    print('\n\nClosing driver...')
    driver.close()
    random_sleep()

    # adding to blogs
    print('Adding to blogs...\n')
    blogs.append(page_links)
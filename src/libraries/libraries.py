def importions ():
    import os
    import time
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import requests as re
    from bs4 import BeautifulSoup as BS
    from serpapi import GoogleSearch
    from selenium import webdriver  # To control the browser
    from selenium.webdriver.common.keys import Keys  # To send keys to the browser
    from selenium.webdriver.common.by import By  # To specify how to locate elements on the page
    from selenium.webdriver.support.ui import WebDriverWait  # To wait for certain conditions
    from selenium.webdriver.support import expected_conditions as EC  # To specify what to wait for
    from selenium.webdriver.chrome.options import Options  # To customize browser options
    from selenium.common.exceptions import TimeoutException  # To handle timeouts
    import networkx as nx
    import cv2
    from mpl_toolkits import mplot3d


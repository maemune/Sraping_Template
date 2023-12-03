# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def option ():
    options = Options ()
    options.add_argument ('--proxy-server="direct://"')
    options.add_argument ('--proxy-bypass-list=*')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])

    #---Headless option---
    # options.add_argument ('--headless')
    # options.add_argument ('--blink-settings=imagesEnabled=false')
    # options.add_argument ('--disable-desktop-notifications')

    #---Window size option---
    # options.add_argument ('--window-size=360,640')
    # options.add_argument ('--window-size=1920,1080')
    # options.add_argument ('--start-maximized')

    #---No hardware acceleration---
    # options.add_argument ('--disable-gpu')

    #---Turn off all extensions---
    options.add_argument ('--disable-extensions')

    #---Fake Media---
    options.add_argument ('--use-fake-ui-for-media-stream')
    options.add_argument ('--use-fake-device-for-media-stream')

    service = Service (ChromeDriverManager ().install ())

    driver = webdriver.Chrome (service=service, options=options)
    return driver

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.common.by import By
# import time
from twilio.rest import Client
from random import seed, randint
import os
import os
import time
import json
import boto3
# import random
import string
import urllib
import inspect
import traceback
import subprocess
from datetime import datetime
from selenium import webdriver
from pyvirtualdisplay import Display
from botocore.exceptions import ClientError
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def jiecheck():
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("window-size=2560x1440")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    chrome_options.add_argument("--remote-debugging-port=9222")
    # CHANGE
    chrome_options.binary_location = '/opt/chrome/' + '88.0.4324.150' + '/chrome'

    driver = webdriver.Chrome(executable_path='/opt/chromedriver/' + "88.0.4324.96" + '/chromedriver',
                              options=chrome_options)
    driver.get("https://courses.wustl.edu/Semester/Listing.aspx")
    driver.refresh()
    driver.find_element(By.ID,"Body_dlDepartments_lnkDept_54").click()
    
    seed(1)

    time.sleep(randint(12, 23))

    items = driver.find_elements(By.ID,"trL31192L09L")
    
    seats = items[0].find_elements(By.CLASS_NAME, "ItemRowCenter")[0].text

    seatsleft = items[0].find_elements(By.CLASS_NAME, "ItemRowCenter")[1].text

    #to close the browser
    driver.close()
    
    return seats > seatsleft

def sendtext():
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Ayo jie! Check yo class :D",
                         from_='',
                         to=''
                     )

def handler(event, context):
    if(jiecheck()):
        sendtext()
    return "Done"

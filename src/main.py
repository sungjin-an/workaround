from fileinput import filename
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep
import os
import logging
import pandas as pd
import openpyxl
from datetime import datetime



# ckeck image save folder 
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        logging.ERROR ('Error: Creating directory. ' +  directory)
 
# check and return https uri
def check_https_URI(varUri):
    if not varUri.startswith("https://"):
        return "https://" + varUri
    else:
        return varUri


# Set Logger INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# define log file
log_file_handler = logging.FileHandler('screenshot.log')
log_file_handler.setFormatter(log_formatter)
logger.addHandler(log_file_handler)



varNum = 1
varDirPath = ".\\image\\"
varFilenamePrefix = "screenshot"
varInputDataFile = "sample_data.csv"

createFolder(varDirPath)



df = pd.read_csv(varInputDataFile)

for index, row in df.iterrows():


    logging.debug("Start---------------" + "%04d" % (index) )
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)

    # prefix with https
    driver.get( check_https_URI( row["URL"] ) )

    sleep(2)

    varNow = datetime.now()
    varSaveFileName = varFilenamePrefix + "_" + "%04d" % (index) + "_" + varNow.strftime("%Y%m%d_%H%M%S_%f") +  ".png"

    driver.save_screenshot( varDirPath + varSaveFileName )

    logging.info(">>Make Screenshot : " + row["URL"] + " ====> " + varSaveFileName)
    # print to console --------------------------------------
    print(">>Make Screenshot : " + row["URL"] + " ====> " + varSaveFileName)

    driver.close()
    logging.debug("End-----------------" + "%04d" % (index) )


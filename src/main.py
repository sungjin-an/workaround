from fileinput import filename
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from time import sleep
import os
import logging
import pandas as pd
import numpy as np
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

# make 2D array from data folder's files 
def make_data_array(data_direcctory):
    files = os.listdir(data_direcctory)

    varArrays = np.empty ( (0,2) )

    for file in files:
        if '.txt' in file:
            varName = file.rsplit(".")[0] 

            f = open ( f"{data_direcctory}{file}", "r") 
            
            lines = f.readlines()
            for line in lines:
                line = line.strip() 
                if ( len(line) > 10 ) : # maybe too short line is not a url
                    varUrl = line
                    break   # Only a file has one url

            varArrays = np.append(varArrays, np.array( [[ varName, varUrl ]] ), axis=0 )
            logging.debug( f"File : {data_direcctory}{file} ==> Name : {varName}, URL : {varUrl}" )

            f.close

    return varArrays


# Set Logger INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# define log file
log_file_handler = logging.FileHandler('screenshot.log')
log_file_handler.setFormatter(log_formatter)
logger.addHandler(log_file_handler)


varSleepSec = 1
varImageOutputDirPath = ".\\image\\"
varDataDirPath = ".\\data\\"
varFilenamePrefix = "screenshot"
varInputDataFile = "sample_data.csv"

createFolder(varImageOutputDirPath)

#--------------------------------------------
# Select case 1 or case 2
#--------------------------------------------
# case 1 : Read Data array from CSV file
# df = pd.read_csv(varInputDataFile)
#--------------------------------------------
# case 2 : Make Data array from data folder
df = pd.DataFrame( make_data_array(varDataDirPath) )
df.columns = ["NAME", "URL"]
#--------------------------------------------


for index, row in df.iterrows():

    logging.debug( f"Start ------------------ {index+1:04}")

    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)

    # prefix with https
    driver.get( check_https_URI( row["URL"] ) )

    sleep(varSleepSec)

    varSaveFileName = f"{varFilenamePrefix}_{index+1:04}_{row['NAME']}_{datetime.now():%Y%m%d_%H%M%S_%f}.png"

    # Capture full page
    element = driver.find_element(By.TAG_NAME, 'body')
    element_png = element.screenshot_as_png
    with open( varImageOutputDirPath + varSaveFileName , "wb") as file:
        file.write(element_png)

    logging.info( f">>Make Screenshot : {row['URL']} ===> {varSaveFileName}" )
    # print to console --------------------------------------
    print( f">>Make Screenshot {index+1:4} : {row['URL']} ===> {varSaveFileName}" )

    driver.close()

    logging.debug( f"End ------------------ {index+1:04}")

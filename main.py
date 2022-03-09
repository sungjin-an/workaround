from fileinput import filename
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep
import os
import logging



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
log_file_handler = logging.FileHandler('test.log')
log_file_handler.setFormatter(log_formatter)
logger.addHandler(log_file_handler)




varNum = 1
varDirPath = ".\\Image\\"
varFilenamePrefix = "screenshot"

createFolder(varDirPath)


varUrls = [
    "https://www.google.com"
    , "https://www.naver.com"
    , "github.com"
]


for x in varUrls:

    logging.debug("Start---------------" + "%04d" % (varNum) )
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--width=800")
    options.add_argument("--height=600")

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)

    # prefix with https
    driver.get( check_https_URI(x) )

    sleep(2)

    driver.save_screenshot( varDirPath + varFilenamePrefix + "_" + "%04d" % (varNum) + ".png")

    logging.info(">>Make Screenshot : " + x + " ====> " + varFilenamePrefix + "_" + "%04d" % (varNum) + ".png")
    # print(">>Make Screenshot : " + x + " ====> " + varFilenamePrefix + "_" + "%04d" % (varNum) + ".png")

    varNum += 1

    driver.close()
    logging.debug("End-----------------" + "%04d" % (varNum) )

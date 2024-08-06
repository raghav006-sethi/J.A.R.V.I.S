from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pathlib
import threading

def _re_forward(required_url,chrome_driver):
    while True:
        current_url=chrome_driver.current_url
        if current_url != required_url:
            print('trying to open required url')
            chrome_driver.get(required_url)
            sleep(1)

        else:
            break

warnings.simplefilter('ignore')
url='https://pi.ai/talk'
scriptdirectory=pathlib.Path().absolute()
chrome_driver_path=''
chrome_options=Options()
chrome_options.add_experimental_option('excludeSwitches',['enable_logging'])
chrome_options.add_argument('--log-level=3')
service=Service(chrome_driver_path)
user_agent='Mozilla/5.0(windows NT 6.1) AppleWebKit/537.2(KHTML,like Gecko)Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver=webdriver.Chrome(service=service,options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(2)
_re_forward(url,driver)
sleep(3)

def introduction(query="hi",voicestobechoosen=1):
    driver.find_element(by=by.XPATH,value=TEXTAREA).send_keys(query)
    sleep(2)

    try:
        driver.find_element(by=by.XPATH,value=SEND_BUTTON).click()
    except:
        driver.find_element(by=By.XPATH,value=TEXTAREA).send_keys('\n')
        print('pressed enter')

    
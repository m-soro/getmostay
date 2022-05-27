from selenium import webdriver
from datetime import datetime
from time import sleep
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_mostay(hotel_location,hotel_code):
    date = datetime.now().date().isoformat()
    site = "https://www.mandarinoriental.com/reservations/?"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')

    # un-comment for heroku
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)

    # un-comment to test locally
    # driver = webdriver.Chrome(options=chrome_options, service= ( Service('/Users/marksoro/chromedriver/chromedriver')) )

    driver.get(site+"arrive="+date+"&depart="+date+"&hotel="+ hotel_code +
                                  "&currency=USD&rooms=1&adults=2&promo=Stay%40MO%242016%40")
    driver.set_window_size(1250,900)

    def find_element_and_screenshot(screenshot_name):
        element = driver.find_element(By.CLASS_NAME,"cbe-calendar")
        sleep(1)
        return element.screenshot(screenshot_name)

    def click_next():
        return driver.find_element(By.CLASS_NAME,"datepick-cmd-next").click()

    find_element_and_screenshot('app/static/imgs/1.png')
    click_next()
    find_element_and_screenshot('app/static/imgs/2.png')
    click_next()
    find_element_and_screenshot('app/static/imgs/3.png')

    hotel_banner = driver.find_element(By.ID,"hotel")
    hotel_banner.screenshot('app/static/imgs/'+ hotel_location +'_image.png')

    driver.close()

    return print(f'\nScraping {hotel_location} done!\n')

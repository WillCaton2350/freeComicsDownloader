from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from seleniumbase import Driver
from src import data, nums, urls
from urllib.error import HTTPError
import logging, os, requests, shutil
from time import sleep

class web_driver:
    def main(self):
        self.driver = Driver(uc=True,incognito=True,headless=False,no_sandbox=True)
        j = 2
        try:
            for k in range(1,nums.num_pg):
                self.driver.get(f'{urls.url}'+f'Issue-1?id=240779#{k}')
                print('url success: page ',j)
                print('k: ',k)
                WDW(self.driver,1).until(
                    EC.presence_of_element_located((By.XPATH,f'/html/body/div[1]/div[4]/div[7]/img[{j}]')))
                print('element success')
                img = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[4]/div[7]/img[{j}]').get_attribute('src')
                open(os.path.join(os.path.expanduser('~'), 'Desktop', f'image_{j}.jpg'), 'wb').write(requests.get(img).content)
                # Next step: save each image separately. Avoid the current overwriting issue.
                self.driver.refresh()
                print('refresh')
                print('next pg')
                WDW(self.driver,1).until(
                    EC.presence_of_element_located((By.XPATH,f'//*[@id="containerRoot"]/div[4]/div[1]/label[2]')))
                print('element 2 found')
                WDW(self.driver,1).until(
                    EC.url_to_be(f'https://readcomiconline.li/Comic/Eat-Your-Young/Issue-1?id=240779#{k}'))
        except NoSuchElementException:
            print('err')

if __name__ == "__main__":
    try:
        func = web_driver()
        func.main()
    except KeyboardInterrupt as e:
        logging.error("ERR:: ",e)
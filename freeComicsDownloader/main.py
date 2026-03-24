from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By
import logging, os, requests, time, shutil
from src import data, nums, urls, xpaths
from urllib.error import HTTPError
from seleniumbase import Driver

    
class web_driver:
    def main(self):
        j = 1  # counter for saved images
        self.driver = Driver(uc=True, incognito=True, headless=True, no_sandbox=True)
        prev_src = None  # track previous image URL

        for k in range(1, nums.num_pg):
            page_url = f'{urls.url}Issue-1?id=240779#{k}'
            print('Loading page:', page_url)
            self.driver.get(page_url)

            retry_count = 0
            max_retries = 5
            visible_img = None

            # Retry loop to wait for the new visible image
            while retry_count < max_retries and visible_img is None:
                try:
                    # Wait for any img in #divImage
                    visible_img = WDW(self.driver, 5).until(
                        # passes the WDW through the anonomys lambda function and attaches it to 
                        # the d variable then uses the mechanisim of a list comp to set the img variable.
                        lambda d: next(
                            (img for img in d.find_elements(By.XPATH, '//div[@id="divImage"]//img') if img.is_displayed()),
                            None
                        )
                    )

                    if visible_img:
                        img_url = visible_img.get_attribute('src')

                        # If the same as previous page, retry
                        if img_url == prev_src:
                            print(f"Image not updated yet, retry {retry_count + 1}/{max_retries}")
                            visible_img = None
                            retry_count += 1
                            time.sleep(1)
                        else:
                            prev_src = img_url  # store new image URL
                            break
                    else:
                        print(f"No visible image found, retry {retry_count + 1}/{max_retries}")
                        retry_count += 1
                        time.sleep(1)

                except (TimeoutException, WebDriverException) as e:
                    print(f"Exception during retry {retry_count + 1}/{max_retries}: {e}")
                    retry_count += 1
                    time.sleep(1)

            if visible_img is None:
                print(f"Failed to load new image on page {k} after {max_retries} retries. Skipping page.")
                self.driver.refresh()
                continue  # go to next page

            # Save the image
            save_path = os.path.join(os.path.expanduser('~'), 'Desktop', f'image_{j}.jpg')
            try:
                with open(save_path, 'wb') as f:
                    f.write(requests.get(img_url).content)
                print(f"Saved image {j}: {save_path}")
                j += 1
            except Exception as e:
                print(f"Failed to save image {j}: {e}")

            # Optional refresh if needed
            self.driver.refresh()
            time.sleep(1)  # create delay between pages


if __name__ == "__main__":
    try:
        func = web_driver()
        func.main()
    except KeyboardInterrupt as e:
        logging.error("ERR:: ", e)
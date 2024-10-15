import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
def main():
    searchVar = input("видите поисковый запрос: ")
    zoom = input("видите зум от 2(самый маленький) до 21(самый большой): ")
    try:
        driver = webdriver.Chrome()
        driver.get(f"https://yandex.ru/maps/?ll=81.569086%2C47.948326&z={zoom}")
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "input__control._bold"))
        )

        search.clear()
        search.send_keys(searchVar)
        search.send_keys(Keys.ENTER)
        time.sleep(10)
        markers = driver.find_elements(By.CLASS_NAME, "ymaps3x0--marker")
        driver.implicitly_wait(10)
        for i in markers:
            if i.text != "":
                print(i.text)
            time.sleep(5)
            
        time.sleep(5)
    except:
        print("Break")
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    main()
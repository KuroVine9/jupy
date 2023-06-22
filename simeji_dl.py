from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-gpu")
    driver = webdriver.Chrome(option)
    url = "https://gall.dcinside.com/mgallery/board/view/?id=girlslastyour&no=5311&page=1"

    driver.get(url)
    driver.implicitly_wait(5)

    i: int = 1
    while True:
        page = driver.find_element(By.PARTIAL_LINK_TEXT, f"{i}화")
        if not page: break
        page.click()
        driver.implicitly_wait(5)
        driver.switch_to.window(driver.window_handles[1])

        page2 = driver.find_element(By.PARTIAL_LINK_TEXT, "본문 이미지 다운로드")
        if not page2: break
        page2.click()
        driver.implicitly_wait(5)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        i+=1
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = Options()

with webdriver.Chrome(executable_path='./webdriver/chromedriver.exe', options=chrome_options) as driver:
    wait = WebDriverWait(driver, 100)
    driver.get("https://v.douyin.com/Jd1WCv7/")
    wait.until(presence_of_element_located((By.CSS_SELECTOR, ".play-btn")))
    driver.find_element_by_css_selector(".play-btn").click()

    video = wait.until(presence_of_element_located((By.CSS_SELECTOR, ".player")))

    video_src = video.get_attribute('src')

    print(video_src)

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"}

    video_src = video_src.replace('playwm', 'play')

    print(video_src)

    response = requests.request("get", video_src, headers=headers)

    with open('test.mp4', "wb") as mp4:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                mp4.write(chunk)





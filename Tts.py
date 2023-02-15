import base64
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_tts(movie_id: int):
    url = "https://weilbyte.github.io/tiktok-tts/"
    content = []

    with open(f"{movie_id}/{movie_id}.txt", "r") as f:
        # Read each line of the file one by one
        for line in f:
            # Strip the leading and trailing whitespace from the line
            line = line.strip()
            # Add the line to the list
            content.append(line)
    part = 0
    for part_of_content in content:
        part += 1
        options = Options()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        text_area = driver.find_element(By.ID, "text")
        text_area.click()
        time.sleep(2)
        text_area.send_keys(part_of_content)
        select = driver.find_element(By.ID, "voice")
        select.click()
        time.sleep(1)
        select.send_keys(Keys.DOWN)
        time.sleep(1)
        select.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element(By.ID, "submit").click()
        time.sleep(4)
        src_url = driver.find_element(By.ID, "audio").get_attribute('src')
        driver.find_element(By.ID, "audio")
        base64_audio = src_url[23:]
        driver.close()

        b64d = base64.b64decode(base64_audio)
        with open(f"{movie_id}/{movie_id}_part_{part}.mp3", "wb") as out:
            out.write(b64d)

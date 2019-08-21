import time
import os
from selenium import webdriver

driver = webdriver.Chrome()

# スクリーンショットの保存先を指定
fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshot.png")

# 指定したURLを開く
driver.get('https://iine-programming.hatenablog.com/')
time.sleep(5)

# スクリーンショットを撮影
driver.save_screenshot(fileName)

# Webdriverの終了
driver.quit()
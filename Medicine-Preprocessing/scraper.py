from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import codecs
import pandas as pd



from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service()
driver = webdriver.Chrome(service=service, options=options)

WEBSITE = "https://calligrapher.ai"

medicines = list(pd.read_csv("pharmacy.csv")["medicines"])


driver.get(WEBSITE)
time.sleep(2)

for each in medicines:
    # for each in medicines_cleaned:
    slider = driver.find_element(By.ID, "bias-slider")
    driver.execute_script(f"arguments[0].value = {0};", slider)
    speed_slider = driver.find_element(By.ID, "speed-slider")
    driver.execute_script(f"arguments[0].value = {9.5};", speed_slider)
    select = Select(driver.find_element(By.ID, "select-style"))
    select.select_by_visible_text("5")
    text_area = driver.find_element(By.ID, "text-input")
    # text_area.send_keys(Keys.CONTROL, "a")  # or Keys.COMMAND on Mac
    text_area.send_keys(each)
    time.sleep(1)
    # driver.find_element(By.ID, "draw-button").click()
    driver.find_element(By.ID, "draw-button").click()
    time.sleep(2)
    driver.find_element(By.ID, "save-button").click()
    text_area = driver.find_element(By.ID, "text-input").clear()

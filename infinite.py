from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.merinolaminates.com/en/product_category/merinolam/")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
browser.close()
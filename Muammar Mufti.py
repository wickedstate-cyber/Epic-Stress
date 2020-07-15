from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'
login_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div'

email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

email_element.send_keys ('USERNAME')
password_element.send_keys ('PASSWORD')
login_button_element.click()

text_box_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
text_box_element = driver.find_element_by_xpath(text_box_xpath)
text_box_element.send_keys ('TWEET HERE')

image_xpath = driver.find_element_by_xpath("//input[@accept = 'image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm']")
image_xpath.send_keys(os.getcwd() + "//FILENAME.png")
    
tweet_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div'
tweet_button_element = driver.find_element_by_xpath(tweet_button_xpath)
tweet_button_element.click()













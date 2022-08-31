import colorama
import selenium
import warnings
import os
import time
import pyperclip
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

user = input("Enter your username or email:")
password = input("Enter your password:")

warnings.filterwarnings("ignore", category=DeprecationWarning) 

option = webdriver.ChromeOptions()
option.add_argument("--mute-audio")
option.add_extension(os.getcwd() + "\solver.crx")
option.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options = option)
driver.get('https://discord.com/login')

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input").send_keys(user)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input").send_keys(password)

time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]").click()

time.sleep(15)

token = driver.execute_script("return (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()")
print(token)

time.sleep(360)
import warnings
import os
import time
import pyperclip
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from colorama import Back, Fore

user = input(f"{Fore.GREEN}Enter your username or email: {Fore.RESET}")
password = input(f"{Fore.GREEN}Enter your password: {Fore.RESET}")

warnings.filterwarnings("ignore", category=DeprecationWarning) 

options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
options.add_extension(os.getcwd() + "\solver.crx")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
driver.get('https://discord.com/login')

def is_element_on_page(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except Exception:
        return False
    return True

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input").send_keys(user)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input").send_keys(password)

time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]").click()

time.sleep(4)

while is_element_on_page("//*[@id='app-mount']/div[2]/div/div[1]/div/div/div/section/div/div[2]/div/iframe"):
    time.sleep(0)

time.sleep(2)

if is_element_on_page("/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div[2]/div/div/input"):
    authcode = input("Enter your 2fa code: ")
else:
    pass

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div[2]/div/div/input").send_keys(authcode)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div[2]/button[1]").click()

time.sleep(5)

token = driver.execute_script("return (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()")
print(f"{Fore.CYAN}token")
pyperclip.copy(token)
print(f"Copied to clipboard{Fore.RESET}")

print(f"{Fore.RED.RED}Quitting...")
driver.quit()

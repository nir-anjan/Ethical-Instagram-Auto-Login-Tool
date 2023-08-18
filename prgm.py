from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def logout():
    more_btn = driver.find_element(By.CLASS_NAME,"_ab6-")
    more_btn.click()
    
    logout_btn =driver.find_element(By.CLASS_NAME,"x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft")
    logout_btn.click()

    return




def login(user,pw):
    uesername_elt=driver.find_element(By.NAME,"username")
    pwd_elt = driver.find_element(By.NAME,"password")
    time.sleep(1)

    uesername_elt.clear()
    uesername_elt.send_keys(user)

    pwd_elt.clear()
    pwd_elt.send_keys(pw)
    pwd_elt.send_keys(Keys.RETURN)

    return

driver = webdriver.Chrome()

#open a tab with that link
driver.get("https://www.instagram.com/")  
#assert "Python" in driver.title
time.sleep(5)

uname = ""
pwd = ""
login(uname,pwd)


time.sleep(20)
print("successfuly logged in! ")

logout()

time.sleep(5)

driver.close()
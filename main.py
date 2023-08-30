import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

#set chrome as browser
driver = webdriver.Chrome()
wait=WebDriverWait(driver,200)



def login(user,pw):
    uesername_elt=wait.until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
    pwd_elt =wait.until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
    
    #entering username
    uesername_elt.clear()
    uesername_elt.send_keys(user)

    #entering password
    pwd_elt.clear()
    pwd_elt.send_keys(pw)
    pwd_elt.send_keys(Keys.RETURN)

    if (wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "_ab2z")))):
        print("Sorry, your password was incorrect. Please double-check your password.")
        return

    #save your login details pop up
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"_ac8f"))).click()
    
    print("hehe")
    #notification permission pop up
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"_a9--._a9_1"))).click()
   
    return


def logout():
    more="xl5mz7h"
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,more))).click() 
  
    for i in range(0,7):
        pyautogui.press('tab')   
        time.sleep(1)
    pyautogui.press('enter')
    return


#main
uname = input("Enter the your Username: ")
pwd = input("Enter the your Password: ")

#open a tab with that link
driver.get("https://www.instagram.com/") 

#maximize the window
driver.maximize_window()


login(uname,pwd)

ch=int(input("If you want to logout enter 1: "))
if ch==1:
    logout()
    print("Closing Browser....")
    time.sleep(3)
    driver.close()
    print("Logout successful! ")

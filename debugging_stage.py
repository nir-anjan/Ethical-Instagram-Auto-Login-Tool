
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
wait=WebDriverWait(driver,20)

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

    #time.sleep(5)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"_ac8f"))).click()
    
    print("hehe")
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"_a9--._a9_1"))).click()
    #driver.find_element(By.CLASS_NAME,"_a9-- _a9_1").click()
    return

def messaging():
    driver.find_element(By.CLASS_NAME,"x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j").click()
    
    return

def logout():
    more="xl5mz7h"
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'//*[@id="mount_0_0_ow"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a/div'))).click()

    
    #wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,))).click()
    #profile x1n2onr6

    return



#open a tab with that link
driver.get("https://www.instagram.com/")  
driver.maximize_window()    





uname = "___ob__i__to___"
pwd = "newnewme@2023"
login(uname,pwd)
print("gfahgdfahsgdha")

#messaging()
time.sleep(3)
logout()
ch=int(input("enter choice: "))
if ch==1:
    driver.close()
    print("successfuly completed! ")
else:
    time.sleep(120)
    driver.close()
    print("successfuly completed! ")

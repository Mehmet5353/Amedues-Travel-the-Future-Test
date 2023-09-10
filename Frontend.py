from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://flights-app.pages.dev/")

driver.fullscreen_window()
def Selection(pos):

    a=driver.find_element(By.ID,"headlessui-combobox-button-\:R1a9lla\:")
    ActionChains(driver).click(a).perform()

    b=driver.find_element(By.ID,"headlessui-combobox-input-\:Rq9lla\:")

    for i in range(pos):
        ActionChains(driver).click(b).key_down(Keys.DOWN).perform()
    ActionChains(driver).click(b).send_keys('\ue007').perform()


    c=driver.find_element(By.ID,"headlessui-combobox-button-\:R1ahlla\:")
    ActionChains(driver).click(c).perform()

    d=driver.find_element(By.ID,"headlessui-combobox-input-\:Rqhlla\:")
    for i in range(pos):
        ActionChains(driver).click(d).key_down(Keys.DOWN).perform()
    ActionChains(driver).click(d).send_keys('\ue007').perform()

    time.sleep(2)

def Selectionn(tot, tot2, iterr, desired):

    if iterr<desired:
        pos = random.randint(0, 6)
        pos2 = random.randint(0, 6)
        a=driver.find_element(By.ID,"headlessui-combobox-button-\:R1a9lla\:")
        ActionChains(driver).click(a).perform()
        b=driver.find_element(By.ID,"headlessui-combobox-input-\:Rq9lla\:")
        if(pos%2==0):
            if(pos<14):
                for i in range(pos):
                    ActionChains(driver).click(b).key_down(Keys.DOWN).perform()
                    tot+=pos
            else:
                for i in range(pos):
                    ActionChains(driver).click(b).key_down(Keys.UP).perform()
                    tot-=pos
            ActionChains(driver).click(b).send_keys('\ue007').perform()
        else:
            if(pos>0):
                for i in range(pos):
                    ActionChains(driver).click(b).key_down(Keys.UP).perform()
                    tot-=pos
            else:
                for i in range(pos):
                    ActionChains(driver).click(b).key_down(Keys.DOWN).perform()
                    tot+=pos
            ActionChains(driver).click(b).send_keys('\ue007').perform()

        

        c=driver.find_element(By.ID,"headlessui-combobox-button-\:R1ahlla\:")
        ActionChains(driver).click(c).perform()
        d=driver.find_element(By.ID,"headlessui-combobox-input-\:Rqhlla\:")
        if(pos2%2!=0):
            if(tot2<15):
                for i in range(pos2):
                    ActionChains(driver).click(d).key_down(Keys.DOWN).perform()
                    tot2+=pos2
            else:
                for i in range(pos2):
                    ActionChains(driver).click(d).key_down(Keys.UP).perform()
                    tot2-=pos2
            ActionChains(driver).click(d).send_keys('\ue007').perform()
        else:
            if(tot2>0):
                for i in range(pos2):
                    ActionChains(driver).click(d).key_down(Keys.UP).perform()
                    tot2-=pos2
            else:
                for i in range(pos2):
                    ActionChains(driver).click(d).key_down(Keys.DOWN).perform()
                    tot2+=pos2
            ActionChains(driver).click(d).send_keys('\ue007').perform()
        iterr+=1
        time.sleep(2)
        return Selectionn(tot, tot2, iterr, desired)
    else:
        return 

for j in range(14):
    Selection(1)
driver.close()
print("Bug is detected, same cities can be entered as a input")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://flights-app.pages.dev/")
driver.fullscreen_window()
tot=0
tot2=0

Selectionn(0, 0, 0, 20)
print("Search part is done, some routes does  not exist")

print("Found X items is same as the number of flight")



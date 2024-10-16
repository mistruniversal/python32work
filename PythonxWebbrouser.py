from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
# link="https://suninjuly.github.io/simple_form_find_task.html"

# try:
#     browser=webdriver.Chrome()
#     browser.get(link)
#
#     input1=browser.find_element(By.TAG_NAME,"input")
#     input1.send_keys("Ivan")
#
#
#
#     input2=browser.find_element(By.TAG_NAME,"last_name")
#     input2.send_keys("Petrov")
#
#
#     input3=browser.find_element(By.TAG_NAME,"city")
#     input3.send_keys("Smolensk")
#
#     input4=browser.find_element(By.ID,"country")
#     input4.send_keys("Russian")
#
#
#     button=browser.find_element(By.CSS_SELECTOR,"button.btn")
#     button.click()
# except:
#     print(1)

# link="https://suninjuly.github.io/selects1.html"
# first_d=webdriver.Chrome()
# first_d.get(link)
#
# getnum1=first_d.find_element(By.ID,"num1").text
# getnum2=first_d.find_element(By.ID,"num2").text
# Patchnum=first_d.find_element(By.ID,"dropdown")
#
# Patchnum.send_keys(str(int(getnum1)+int(getnum2)))
#
# getsub=first_d.find_element(By.CSS_SELECTOR,"button.btn-default")
# getsub.click()
#
# time.sleep(10)
# first_d.quit()


# print(2==range(1,10))






# link="https://suninjuly.github.io/selects1.html"
# first_d=webdriver.Chrome()
# first_d.get(link)
#
# getnum1=first_d.find_element(By.ID,"num1").text
# getnum2=first_d.find_element(By.ID,"num2").text
# Patchnum=first_d.find_element(By.ID,"dropdown")
#
# Patchnum.send_keys(str(int(getnum1)+int(getnum2)))
#
# getsub=first_d.find_element(By.CSS_SELECTOR,"button.btn-default")
# getsub.click()
#
# time.sleep(10)
# first_d.quit()




link="https://www.metalcity.ru/catalog/stellagi/arhivnye/ms/"
brovser=webdriver.Chrome()
brovser.get(link)

getelement=brovser.find_element(By.CLASS_NAME,"md-btn-success")
getelement.click()
time.sleep(3)
getelement1=brovser.find_element(By.ID,"submit-button")
getelement1.click()
time.sleep(2)
getelement2=brovser.find_element(By.CLASS_NAME,"md-btn-success")
getelement2.click()
time.sleep(5)
getelement3=brovser.find_element(By.ID,"barba-wrapper")


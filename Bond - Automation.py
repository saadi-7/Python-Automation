#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from csv import reader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains as A


# In[3]:


driver = webdriver.Chrome("/Users/sadaattameem/Desktop/chromedriver2")
driver.get('https://www.corporatebonds.in/Forms/Login.aspx')
driver.maximize_window()
val = 40 
driver.implicitly_wait(val)
username=driver.find_element_by_xpath("//input[@name='Login1$UserName']")
username.send_keys('minions')
password=driver.find_element_by_xpath("//input[@type='password']")
password.send_keys("Bonds@123")
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.get("https://www.corporatebonds.in/Forms/GeneratedDealSlip.aspx")
for row in range (1,12):
    page=driver.find_element_by_xpath(f"//*[@id='ctl00_ContentPlaceHolder1_vws_DealSlip_gv_Details']/tbody/tr[12]/td/table/tbody/tr/td[{row}]")
    page.click()
    time.sleep(3)
    page.click()
    time.sleep(3)
    for i in range(1,11):
        box=driver.find_element_by_xpath(f"(//input[@type='image'])[{i}]")
        name='Name'
        name_of_the_buyer=driver.find_element_by_xpath(f"//*[@id='ctl00_ContentPlaceHolder1_vws_DealSlip_gv_Details']/tbody/tr[{i+1}]/td[10]").text
        box.click()
        a = A(driver)
        time.sleep(2)
        pan=driver.find_element_by_xpath("(//td[@class='LabelCSS'])[3]").text
        pan_number=driver.find_element_by_xpath("//span[@id='ctl00_ContentPlaceHolder1_lbl_PAN']").text
        isin=driver.find_element_by_xpath("(//td[@class='LabelCSS'])[2]").text
        isin_number=driver.find_element_by_xpath("//span[@id='ctl00_ContentPlaceHolder1_txt_ISIN']").text
        settlement=driver.find_element_by_xpath("//*[@id='Tr6']/td[1]").text
        settlement_amount=driver.find_element_by_xpath("//*[@id='Tr6']/td[2]").text
        time.sleep(2)
        #name_of_the_buyer.click()
        # a.click_and_hold(name_of_the_buyer).perform()
        # a.key_down(Keys.CONTROL).send_keys("a").perform()
        # a.key_down(Keys.CONTROL).send_keys("c").perform()
        # a.click_and_hold(name_of_the_buyer).perform()
        # random=driver.find_element_by_xpath("(//textarea[@onblur='ConvertUCase(this);'])[1]")
        # a.click_and_hold(random).perform()
        # #a.key_down(Keys.CONTROL).send_keys("v").perform()
        # random.send_keys(Keys.SHIFT, Keys.INSERT)
        # a.KeyUp(Keys.Control);
        # a.Build().Perform()
        print(i,name,name_of_the_buyer)
        print(i,pan,pan_number)
        print(i,isin,isin_number)
        print(i,settlement,settlement_amount)
        time.sleep(1)
        driver.back()
    driver.back()
    
#driver.quit()


# In[ ]:





# In[ ]:





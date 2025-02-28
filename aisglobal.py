from selenium import webdriver

driver = webdriver.Chrome()
driver.get("url")

driver.find_element("uasername").send_keys('username')
driver.find_element("password").send_keys("password")
driver.find_element("xpath").click()

ele = driver.find_elements("xpath")
dta = [1,2,3,4,5]

for i in ele:
    if i.text() in dta:
        print("data matching")
    else:
        print("not matching data",i)
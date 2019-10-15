from selenium import webdriver

#Definitions & Launch
driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
#driver = webdriver.Firefox(executable_path='./drivers/geckodriver.exe')
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/")
assert "The Internet" in driver.title

link_alerts = driver.find_element_by_link_text("JavaScript Alerts")
link_alerts.click()

btn_JSConfirm = driver.find_element_by_xpath('//button[text()="Click for JS Confirm"]')
btn_JSConfirm.click()

driver.switch_to.alert.accept()  #Hit Okay on JS Confirm

p_result = driver.find_element_by_id("result")
if p_result.text == "You clicked: Ok":  #Verify contents of results section
    print("Okay was clicked")
else:
    print("Okay was not clicked")

driver.close()
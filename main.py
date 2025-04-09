from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.uitestingplayground.com/dynamicid")

ele = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

print(ele.text)
print(ele.get_attribute("id"))
driver.quit()

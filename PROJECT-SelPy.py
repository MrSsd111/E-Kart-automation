import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element(By.XPATH,"//a[@class = 'nav-link'][text() = 'Shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")

for product in products:
    prod1 = product.find_element(By.XPATH, "div/h4/a").text
    print(prod1)
    if prod1 == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
        break

time.sleep(2)

driver.find_element(By.XPATH,"//a[@class = 'nav-link btn btn-primary']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@class = 'validate filter-input form-control ng-untouched ng-pristine ng-valid']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()= 'India']")))
driver.find_element(By.XPATH, "//a[text()= 'India']").click()
driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@class= 'btn btn-success btn-lg']").click()
final = driver.find_element(By.CSS_SELECTOR, "div[class = 'alert alert-success alert-dismissible']").text
print(final)
assert "Success! Thank you!" in final
driver.close()
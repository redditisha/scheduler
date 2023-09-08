from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://trends.google.com")

print("Done")

driver.quit()

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')  # Disable sandboxing for headless Chrome

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://trends.google.com")

print("Done")

driver.quit()

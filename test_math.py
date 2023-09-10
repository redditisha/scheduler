# Import math Library
import math
from selenium import webdriver

# Return the base-10 logarithm of different numbers
print(math.log10(2.7183))
print(math.log10(2))
print(math.log10(1))
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://trends.google.com")

print("Done")

driver.quit()

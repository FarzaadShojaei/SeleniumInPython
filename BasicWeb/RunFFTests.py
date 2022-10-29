from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
class RunFFTests():
 def testMethod(self):
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path="C:\\chromedriver\\geckodriver.exe")

    driver.get("https://www.letskodeit.com")


ff=RunFFTests()
ff.testMethod()
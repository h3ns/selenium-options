'''
Created on May 30, 2018
@author: venkateshwara.d
'''
from selenium import webdriver
import os

class RunEdgeTestsWindows():
    # https://sites.google.com/a/chromium.org/chromedriver/downloads
    # http://chromedriver.storage.googleapis.com/index.html?path=2.21/
    def test(self):
        driverLocation = os.path.abspath('..')  + "\\temp\\drivers\\msedgedriver98"
        os.environ["webdriver.edge.driver"] = driverLocation
        driver = webdriver.Edge(driverLocation)
        driver.get("http://www.letskodeit.com")

chromeTest = RunEdgeTestsWindows()
chromeTest.test()
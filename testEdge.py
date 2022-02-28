# pip install webdriver-manager
# https://pypi.org/project/webdriver-manager/

# selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get("https://www.duckduckgo.com")
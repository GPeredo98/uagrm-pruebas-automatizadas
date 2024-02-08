import os
from datetime import datetime
import warnings
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import Edge


def get_driver(browser, url):
    driver = None
    if browser == 'edge':
        edge_path = 'drivers/msedgedriver.exe'
        # driver = Edge(executable_path=edge_path)
        driver = webdriver.Chrome()
    elif browser == 'chrome':
        driver = webdriver.Edge(executable_path='drivers/msedgedriver.exe')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')

    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def take_screenshot(driver, folder, name):
    day = datetime.now().strftime('%Y-%m-%d')
    now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    try:
        os.makedirs('./screenshots/%s/%s' % (day, folder))
    except:
        pass
    driver.get_screenshot_as_file('screenshots/%s/%s/%s %s.png' % (day, folder, name, now))


def resource_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)

    return do_test


def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate
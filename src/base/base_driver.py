import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver(object):
    def __init__(self, host, driver_addr, log):
        self.log = log

        s = Service(driver_addr)
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()
        self.driver.get(host)

        self.wait = WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.1)

    # def __new__(cls, *args, **kw):
        # if not hasattr(cls, '_instance'):
        #     orig = super(BaseDriver, cls)
        #     cls._instance = orig.__new__(cls)
        # return cls._instance

    def find(self, method, value):
        """
        封装元素定位方法
        :param method:
        :param value:
        :return:
        """

        if method == 'id':
            self.element = self.wait.until(lambda x: x.find_element(By.ID, value))
        elif method == 'xpath':
            self.element = self.wait.until(lambda x: x.find_element(By.XPATH, value))
        elif method == 'class':
            self.element = self.wait.until(lambda x: x.find_element(By.CLASS_NAME, value))
        elif method == 'tag':
            self.element = self.wait.until(lambda x: x.find_element(By.TAG_NAME, value))
        elif method == 'name':
            self.element = self.wait.until(lambda x: x.find_element(By.NAME, value))
        elif method == 'linktext':
            self.element = self.wait.until(lambda x: x.find_element(By.PARTIAL_LINK_TEXT, value))
        elif method == 'css':
            self.element = self.wait.until(lambda x: x.find_element(By.CSS_SELECTOR, value))
        else:
            self.log.error('无此查找方式，语法错误')

        if self.element:
            return self.element
        else:
            self.log.error('未获取到此元素')

    def ec_find(self, method, value):
        """
        封装基于ec的元素定位
        :param method:
        :param value:
        :return:
        """

        if method == 'xpath':
            self.element = self.wait.until(EC.visibility_of_element_located((By.XPATH, value)))
        else:
            self.log.error('无此查找方式，语法错误')

        if self.element:
            return self.element
        else:
            self.log.error('未获取到此元素')

    def tear_down(self):
        """
        清理数据
        :return:
        """
        self.driver.quit()


if __name__ == '__main__':
    print(os.path.join(os.path.dirname(os.getcwd()), 'base/logs'))

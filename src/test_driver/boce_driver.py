from selenium.webdriver.common.by import By

from src.base.base_driver import BaseDriver
from src.base.enum.boce_element_enum import BoceElementEnum


class BoceDriver(BaseDriver):

    def __init__(self, host, driver_addr, log, account, password, url):
        self.url = url
        self.account = account
        self.password = password

        super(BoceDriver, self).__init__(host, driver_addr, log)

    def login(self):
        """
        执行登录操作
        :return:
        """
        self.find('xpath', BoceElementEnum.ACCOUNT_XPATH.value).send_keys(self.account)
        self.find('xpath', BoceElementEnum.PASSWORD_XPATH.value).send_keys(self.password)
        self.find('xpath', BoceElementEnum.LOGIN_BUTTON_XPATH.value).click()

    def find_host_input(self):
        """
        查找ip输入框
        :return:
        """

        self.find('xpath', BoceElementEnum.HOST_INPUT_XPATH.value).send_keys(self.url)

    def find_subm_btn(self):
        """
        查找检测按钮
        :return:
        """

        self.find('xpath', BoceElementEnum.SUBM_BTN_XPATH.value).click()

    def get_data(self):
        """
        解析数据，整理数据
        :return:
        """

        get_data = self.find('class', BoceElementEnum.GET_DATA_CLASS_NAME.value)\
            .find_elements(By.TAG_NAME, 'tr')
        if get_data:
            lst = []
            for i in get_data:
                item = i.find_elements(By.TAG_NAME, 'td')[5].text
                lst.append(item)
            self.log.debug(lst)

    def find_flex_success(self):
        """
        等待检测完毕的相关提示文案的出现
        :return:
        """

        self.ec_find('xpath', BoceElementEnum.FLEX_SUC_XPATH.value)

        self.get_data()

from enum import Enum


class BoceElementEnum(Enum):
    """
    boce元素枚举
    """
    # 输入框：host
    HOST_INPUT_XPATH = '/html/body/div[1]/div[1]/div[1]/input[2]'
    # 按钮：检测一下
    SUBM_BTN_XPATH = '/html/body/div[1]/div[1]/div[1]/input[3]'
    # 文案：解析时间
    GET_DATA_CLASS_NAME = 'node-data-tbody'
    # 文案：已检测结束
    FLEX_SUC_XPATH = "/html/body/div[8]"
    # 登录账号
    ACCOUNT_XPATH = '//*[@id="pane-account"]/form/div[1]/div/div[1]/input'
    # 登录密码
    PASSWORD_XPATH = '//*[@id="pane-account"]/form/div[2]/div/div[1]/input'
    # 登录按钮
    LOGIN_BUTTON_XPATH = '//*[@id="app"]/div[1]/div[2]/div/div/div/div[3]/button'

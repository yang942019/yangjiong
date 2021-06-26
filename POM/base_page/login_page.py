from time import sleep

from selenium import webdriver

from POM.commont.base_page import CommonKey
from POM.config.chrome_options import conf_options
from POM.config.read_config import read_fig


class Login(CommonKey):
    url = read_fig('TEST_SERVER', 'url') + 'shopxo/index.php?s=/index/user/logininfo.html'
    user_input = ('xpath', '//input[@name="accounts"]')
    psd_input = ('name', 'pwd')
    login = ('xpath', '//button[text()="登录"]')

    def login_fun(self, user, password):
        self.visit(self.url)
        self.input(self.user_input, user)
        self.input(self.psd_input, password)
        self.click(self.login)


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        lg = Login(driver)
        lg.login_fun('wj942019', 'yj942019')
        sleep(3)
        driver.quit()
    except:
        driver.quit()

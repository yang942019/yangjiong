'''
关键字驱动
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class CommonKey:
    def __init__(self, driver):
        # self.driver = open_browser(browser)
        self.driver = driver
        self.driver.implicitly_wait(10)

    # 访问网页
    def visit(self, txt):
        self.driver.get(txt)

    # 定位元素
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击操作
    def click(self, loc):
        self.locator(loc).click()

    # 设置窗口句柄
    def handle(self):
        handle = self.driver.window_handles
        if len(handle) > 2:
            self.driver.close()
            handle = self.driver.window_handles
            self.driver.switch_to.window(handle[1])

    # 隐式等待
    def explicit(self, loc):
        WebDriverWait(self.driver, 10, 0.05).until(lambda el: self.driver.find_element(*loc), message='定位失败')

    # 退出

    def quit(self):
        self.driver.quit()

    # 文本断言
    def assert_text(self, loc, txt):
        try:
            reality = self.locator(loc).text
            assert txt == reality, '断言失败'
            return True
        except Exception:
            self.log.exception('出现异常，断言失败：{0} != {1}'.format(txt, reality))
            return False

    def title_(self):
        return self.driver.title

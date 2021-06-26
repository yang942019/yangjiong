import allure
import pytest
from selenium import webdriver
from ddt import ddt
from POM.base_page.cart_page import CartPage
from POM.base_page.login_page import Login
from POM.base_page.phone_product_page import PhonePage

from POM.config.chrome_options import conf_options
from POM.config.read_yaml import read


@allure.step
def step(num):
    print(f'-------{num}')


@ddt
@allure.epic('这是一个商城pom模式测试')
@allure.feature('测试模块1')
class TestPom:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.lg = Login(cls.driver)
        cls.pp = PhonePage(cls.driver)
        cls.cp = CartPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.run(order=1)
    @allure.testcase('shopxo/index.php?s=/index/user/logininfo.html')
    @allure.title('登录模块测试')
    @allure.story('pom测试，目前模块为登录模块')
    @pytest.mark.parametrize('data', read(r'D:\daily_use\python\git_warehouse\POM\data\login.yaml'))
    def test_login(self, data):
        '''
        登录模块与加入购物车
        '''
        step(1)
        self.lg.login_fun(data['user'], data['password'])

    # 添加商品
    @pytest.mark.run(order=2)
    @allure.story('添加商品')
    def test_add_cart(self):
        '''
        添加商品测试
        '''
        step(2)
        self.pp.add_cart()

    # 购物车校验

    @pytest.mark.run(order=3)
    @allure.story('购物车验证')
    def test_assert_cart(self):
        step(3)
        self.cp.cart_info()


if __name__ == '__main__':
    pytest.main()

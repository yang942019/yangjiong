'''
    CartPage:购物车页面，校验商品是否添加成功
'''



# 购物车页面
from POM.commont.base_page import CommonKey
from POM.config.read_config import read_fig


class CartPage(CommonKey):
    url = read_fig('TEST_SERVER', 'url') + 'shopxo/index.php?s=/index/cart/index.html'

    goods = ('xpath', '//a[contains(text(),"iPhone")]')

    # 校验商品是否存在
    def cart_info(self):
        self.visit(self.url)
        # return self.assert_text(self.goods, 'iPhone')
        self.explicit(self.goods)

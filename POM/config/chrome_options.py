from selenium import webdriver


# ChromeOptions类的封装

def conf_options():
    # 配置ChromeOptions
    options = webdriver.ChromeOptions()
    # 默认启动的driver窗体最大化
    options.add_argument('start-maximized')
    # 去掉提示正在执行自动化的警告条：没啥用，仅限于强迫症患者以及部分特别的系统。
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 这个现在已经用不了了，这是老版本去掉警告条的方式
    # options.add_argument('disable-infobars')
    # 添加本地缓存
    # options.add_argument(r'--user-data-dir=C:\Users\15414\AppData\Local\Google\Chrome\User Data')
    # 添加无头指令：有斟酌地进行使用。
    # options.add_argument('--headless')
    # 添加去掉密码弹窗管理
    prefs = {}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    options.add_experimental_option("prefs", prefs)
    # 隐身模式
    # options.add_argument('incognito')
    # 指定窗口大小的指令
    # options.add_argument('window-size=2000,4000')
    # 默认浏览器启动的坐标位置
    # options.add_argument('window-position=200,400')
    return options

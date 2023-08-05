import logging
import os
import sys
import time
import allure
from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from qrunner.utils.webdriver_manager_extend import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from qrunner.utils.log import logger
from qrunner.utils.config import conf
from urllib import parse
from selenium.webdriver.remote.remote_connection import LOGGER
from qrunner.utils.exceptions import ScreenFailException

LOGGER.setLevel(logging.WARNING)


class Browser(object):
    """
    根据关键词初始化浏览器操作句柄，
    如'chrome、google chrome、gc'代表chrome浏览器，
    如'firefox、ff'代表火狐浏览器，
    如'edge'代表edge浏览器，
    如'safari'代表safari浏览器
    """
    name = None

    def __new__(cls, name=None):
        cls.name = name

        if (cls.name is None) or (cls.name in ["chrome", "google chrome", "gc"]):
            return cls.chrome()
        # elif cls.name in ['internet explorer', 'ie', 'IE']:
        #     return cls.ie()
        elif cls.name in ['firefox', 'ff']:
            return cls.firefox()
        elif cls.name == 'edge':
            return cls.edge()
        # elif cls.name == 'opera':
        #     return cls.opera()
        elif cls.name == 'safari':
            return cls.safari()
        raise NameError(f"Not found {cls.name} browser")

    @staticmethod
    def chrome():
        # if ChromeConfig.command_executor != "":
        #     return webdriver.Remote(command_executor=ChromeConfig.command_executor,
        #                             desired_capabilities=DesiredCapabilities.CHROME.copy())
        chrome_options = ChromeOptions()
        headless_flag = conf.get_item('web', 'headless')
        if headless_flag:
            chrome_options.add_argument('--headless')

        chrome_options.add_argument("--incognito")  # 隐身模式
        chrome_options.add_experimental_option("excludeSwitches",
                                               ['enable-automation'])  # 去除自动化控制提示

        # 分别在环境变量、指定目录、淘宝镜像中查找驱动文件
        exe_path = ''
        try:
            exe_path = conf.get_item('common', 'executable_path')
            logger.debug(f'在指定目录中搜索驱动文件: {exe_path}')
            driver = webdriver.Chrome(options=chrome_options,
                                      executable_path=exe_path)
        except Exception as first_e:
            logger.debug(f'找不到执行文件: {exe_path}')
            logger.debug(first_e)
            try:
                exe_path = 'chromedriver'
                logger.debug(f'在环境变量中搜索驱动文件: {exe_path}')
                driver = webdriver.Chrome(options=chrome_options,
                                          executable_path=exe_path)
            except Exception as second_e:
                logger.debug(f'找不到执行文件: {exe_path}')
                logger.debug(second_e)
                try:
                    logger.debug(f'在淘宝镜像中搜索驱动文件: ')
                    exe_path = ChromeDriverManager().install()
                    driver = webdriver.Chrome(options=chrome_options,
                                              executable_path=exe_path)
                except Exception as third_e:
                    logger.debug(f'找不到执行文件: {exe_path}')
                    logger.debug(third_e)
                    logger.debug('请设置正确的驱动文件路径！！！')
                    sys.exit()
                else:
                    logger.debug('在淘宝镜像中查找成功!')
            else:
                logger.debug('在环境变量中查找成功')
        else:
            logger.debug('在指定目录中查找成功!')

        timeout = conf.get_item('common', 'timeout')
        driver.set_page_load_timeout(timeout)
        if headless_flag:
            driver.set_window_size(1920, 1080)
        else:
            driver.maximize_window()
        return driver

    @staticmethod
    def firefox():
        # if FirefoxConfig.command_executor != "":
        #     return webdriver.Remote(command_executor=FirefoxConfig.command_executor,
        #                             desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        firefox_options = FirefoxOptions()
        headless_flag = conf.get_item('web', 'headless')
        if headless_flag:
            firefox_options.headless = True

        # driver = webdriver.Firefox(options=firefox_options,
        #                            executable_path=GeckoDriverManager().install())

        # 分别在环境变量、指定目录、淘宝镜像中查找驱动文件
        exe_path = ''
        try:
            exe_path = conf.get_item('common', 'executable_path')
            logger.debug(f'在指定目录中搜索驱动文件: {exe_path}')
            driver = webdriver.Firefox(options=firefox_options,
                                       executable_path=exe_path)
        except Exception as first_e:
            logger.debug(f'找不到执行文件: {exe_path}')
            logger.debug(first_e)
            try:
                exe_path = 'geckodriver'
                logger.debug(f'在环境变量中搜索驱动文件: {exe_path}')
                driver = webdriver.Firefox(options=firefox_options,
                                           executable_path=exe_path,)
            except Exception as second_e:
                logger.debug(f'找不到执行文件: {exe_path}')
                logger.debug(second_e)
                try:
                    logger.debug(f'在淘宝镜像中搜索驱动文件: ')
                    exe_path = GeckoDriverManager().install()
                    driver = webdriver.Firefox(options=firefox_options,
                                               executable_path=exe_path,)
                except Exception as third_e:
                    logger.debug(f'找不到执行文件: {exe_path}')
                    logger.debug(third_e)
                    logger.debug('请设置正确的驱动文件路径！！！')
                    sys.exit()
                else:
                    logger.debug('在淘宝镜像中查找成功!')
            else:
                logger.debug('在环境变量中查找成功')
        else:
            logger.debug('在指定目录中查找成功!')

        timeout = conf.get_item('common', 'timeout')
        driver.set_page_load_timeout(timeout)
        if headless_flag:
            driver.set_window_size(1920, 1080)
        else:
            driver.maximize_window()
        return driver

    # @staticmethod
    # def ie():
    #     # if IEConfig.command_executor != "":
    #     #     return webdriver.Remote(command_executor=IEConfig.command_executor,
    #     #                             desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())
    #     driver = webdriver.Ie(executable_path=IEDriverManager().install())
    #     timeout = conf.get_item('common', 'timeout')
    #     driver.set_page_load_timeout(timeout)
    #     driver.maximize_window()
    #     return driver

    @staticmethod
    def edge():
        # if EdgeConfig.command_executor != "":
        #     return webdriver.Remote(command_executor=EdgeConfig.command_executor,
        #                             desired_capabilities=DesiredCapabilities.EDGE.copy())
        # driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager(log_level=1).install())

        # 分别在环境变量、指定目录、淘宝镜像中查找驱动文件
        exe_path = ''
        try:
            exe_path = conf.get_item('common', 'executable_path')
            logger.debug(f'在指定目录中搜索驱动文件: {exe_path}')
            driver = webdriver.Edge(executable_path=exe_path)
        except Exception as first_e:
            logger.debug(f'找不到执行文件: {exe_path}')
            logger.debug(first_e)
            try:
                exe_path = 'msedgedriver'
                logger.debug(f'在环境变量中搜索驱动文件: {exe_path}')
                driver = webdriver.Edge(executable_path=exe_path)
            except Exception as second_e:
                logger.debug(f'找不到执行文件: {exe_path}')
                logger.debug(second_e)
                try:
                    logger.debug(f'在淘宝镜像中搜索驱动文件: ')
                    exe_path = EdgeChromiumDriverManager(log_level=1).install()
                    driver = webdriver.Edge(executable_path=exe_path)
                except Exception as third_e:
                    logger.debug(f'找不到执行文件: {exe_path}')
                    logger.debug(third_e)
                    logger.debug('请设置正确的驱动文件路径！！！')
                    sys.exit()
                else:
                    logger.debug('在淘宝镜像中查找成功!')
            else:
                logger.debug('在环境变量中查找成功')
        else:
            logger.debug('在指定目录中查找成功!')

        timeout = conf.get_item('common', 'timeout')
        driver.set_page_load_timeout(timeout)
        driver.maximize_window()
        return driver

    # @staticmethod
    # def opera():
    #     # if OperaConfig.command_executor != "":
    #     #     return webdriver.Remote(command_executor=OperaConfig.command_executor,
    #     #                             desired_capabilities=DesiredCapabilities.OPERA.copy())
    #     driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    #     timeout = conf.get_item('common', 'timeout')
    #     driver.set_page_load_timeout(timeout)
    #     driver.maximize_window()
    #     return driver

    @staticmethod
    def safari():
        # if SafariConfig.command_executor != "":
        #     return webdriver.Remote(command_executor=SafariConfig.command_executor,
        #                             desired_capabilities=DesiredCapabilities.SAFARI.copy())
        driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        driver.maximize_window()
        timeout = conf.get_item('common', 'timeout')
        driver.set_page_load_timeout(timeout)
        return driver


class WebDriver(object):
    _instance = {}

    def __new__(cls, browser_name=None):
        # if not browser_name:
        #     browser_name = conf.get_item('web', 'browser_name')
        if browser_name not in cls._instance:
            cls._instance[browser_name] = super().__new__(cls)
        return cls._instance[browser_name]

    def __init__(self, browser_name=None):
        self.d = Browser(browser_name)

    @classmethod
    def get_instance(cls, browser_name=None):
        """Create singleton"""
        if browser_name not in cls._instance:
            logger.info(f'[{browser_name}] Create web driver singleton')
            return WebDriver(browser_name)
        return WebDriver._instance[browser_name]

    def open_url(self, url=None, login=True):
        if url is None:
            base_url = conf.get_item('common', 'base_url')
            if not base_url:
                logger.debug('请设置base_url')
                sys.exit()
            url = base_url
        else:
            if 'http' not in url:
                base_url = conf.get_item('common', 'base_url')
                if not base_url:
                    logger.debug('请设置base_url')
                    sys.exit()
                url = parse.urljoin(base_url, url)
        logger.info(f'访问: {url}')
        self.d.get(url)
        # 把默认请求头添加到cookie中
        if login:
            headers = conf.get_item('common', 'login_headers')
            logger.debug(headers)
            cookies = []
            if headers:
                for k, v in headers.items():
                    cookies.append({"name": k, "value": v})
                self.add_cookies(cookies)
                self.refresh()

    def back(self):
        logger.info('返回上一页')
        self.d.back()

    def screenshot(self, file_name):
        """
        截图并保存到预定路径
        @param file_name: foo.png or fool
        @return:
        """
        try:
            # 把文件名处理成test.png的样式
            if '.' in file_name:
                file_name = file_name.split(r'.')[0]
            # 截图并保存到当前目录的images文件夹中
            img_dir = os.path.join(os.getcwd(), 'images')
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            time_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒')
            file_path = os.path.join(img_dir, f'{time_str}-{file_name}.png')
            self.d.save_screenshot(file_path)
            # 上传allure报告
            allure.attach.file(file_path, attachment_type=allure.attachment_type.PNG, name=f'{file_name}.png')
            return file_path
        except Exception as e:
            raise ScreenFailException(f'{file_name} 截图失败\n{str(e)}')

    # def screenshot_and_mark(self, file_name, rect):
    #     """给图片指定范围画上红框
    #     rect: [x, y, width, height]
    #     x: 左上坐标x
    #     y：左上角坐标y
    #     width：矩形宽度
    #     height：矩形高度
    #     """
    #     # 把文件名处理成test.png的样式
    #     if '.' in file_name:
    #         file_name = file_name.split(r'.')[0]
    #     # 截图并保存到当前目录的images文件夹中
    #     img_dir = os.path.join(os.getcwd(), 'images')
    #     if os.path.exists(img_dir) is False:
    #         os.mkdir(img_dir)
    #     time_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒')
    #     file_path = os.path.join(img_dir, f'{time_str}-{file_name}.png')
    #     self.d.save_screenshot(file_path)
    #     # 画框
    #     ImageRecognition.mark(file_path, rect)
    #     # 上传allure报告
    #     allure.attach.file(file_path, attachment_type=allure.attachment_type.PNG, name=f'{file_name}.png')
    #     return file_path

    @property
    def page_content(self):
        page_source = self.d.page_source
        logger.info(f'获取页面内容: \n{page_source}')
        return page_source

    # @property
    # def rect(self):
    #     logger.info('获取窗口的坐标及宽高')
    #     return self.d.get_window_position()

    def max_window(self):
        logger.info('窗口设置全屏')
        self.d.maximize_window()

    def set_window(self, width, height):
        logger.info('设置窗口长宽')
        self.d.set_window_size(width, height)

    def get_windows(self):
        logger.info(f'获取当前打开的窗口列表')
        return self.d.window_handles

    def switch_window(self, old_windows):
        logger.info('切换到最新的window')
        current_windows = self.d.window_handles
        newest_window = [window for window in current_windows if window not in old_windows][0]
        self.d.switch_to.window(newest_window)

    def window_scroll(self, width, height):
        logger.info(f'设置scroll bar的宽高')
        js = "window.scrollTo({w},{h});".format(w=str(width), h=str(height))
        self.d.execute_script(js)

    def switch_to_frame(self, frame_id):
        logger.info(f'切换到frame {frame_id}')
        self.d.switch_to.frame(frame_id)

    def switch_to_frame_out(self):
        logger.info('从frame中切出来')
        self.d.switch_to.default_content()

    def execute_js(self, script, *args):
        logger.info(f'执行js脚本: \n{script}')
        self.d.execute_script(script, *args)

    def click(self, element):
        logger.info(f'点击元素: {element}')
        self.d.execute_script('arguments[0].click();', element)

    def quit(self):
        logger.info('退出浏览器')
        self.d.quit()

    def close(self):
        logger.info('关闭当前页签')
        self.d.close()

    def add_cookies(self, cookies: list):
        for cookie in cookies:
            self.d.add_cookie(cookie)

    def get_cookies(self):
        logger.info('获取cookies')
        cookies = self.d.get_cookies()
        logger.info(cookies)
        return cookies

    def get_cookie(self, name):
        logger.info(f'获取cookie: {name}')
        cookie = self.d.get_cookie(name)
        logger.info(cookie)
        return cookie

    def delete_all_cookies(self):
        logger.info('删除所有cookie')
        self.d.delete_all_cookies()

    def delete_cookie(self, name):
        logger.info(f'删除cookie: {name}')
        self.d.delete_cookie(name)

    def refresh(self):
        logger.info(f'刷新当前页')
        self.d.refresh()

    def get_title(self):
        logger.info('获取页面标题')
        title = self.d.title
        logger.info(title)
        return title

    def get_url(self):
        logger.info('获取页面url')
        url = self.d.current_url
        logger.info(url)
        return url

    def get_alert_text(self):
        logger.info('获取alert的文本')
        alert_text = self.d.switch_to.alert.text
        logger.info(alert_text)
        return alert_text

    def accept_alert(self):
        logger.info('同意确认框')
        self.d.switch_to.alert.accept()

    def dismiss_alert(self):
        logger.info('取消确认框')
        self.d.switch_to.alert.dismiss()



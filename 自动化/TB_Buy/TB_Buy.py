import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  

def wait_for_element(driver, locator, max_wait_time=60):
    wait_time = 5
    total_wait_time = 0
    while total_wait_time < max_wait_time:
        try:
            element = WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located(locator))
            print(f"成功找到元素：{locator[1]}")
            return element
        except TimeoutException:
            print(f"未能找到元素：{locator[1]}，继续等待...")
            total_wait_time += wait_time
            wait_time = min(wait_time * 2, max_wait_time - total_wait_time)
    print(f"已超过最大等待时间 {max_wait_time} 秒，未能找到元素：{locator[1]}")
    return None

def click_button(browser, locator, success_message):
    button = wait_for_element(browser, locator)
    if button:
        time.sleep(1)
        button.click()
        print(success_message)
        return True
    else:
        print(f"未找到按钮：{locator[1]}")
        return False

def login(browser):
    login_button_locator = (By.LINK_TEXT, "亲，请登录")
    return click_button(browser, login_button_locator, '点击登录按钮成功，请扫码登录')

def go_to_cart(browser):
    cart_button_locator = (By.XPATH, "//span[@id='J_MiniCartNum']")
    return click_button(browser, cart_button_locator, '进入购物车成功')

def select_all(browser):
    select_all_button_locator = (By.CSS_SELECTOR, '#J_SelectAll1')
    return click_button(browser, select_all_button_locator, '全选成功')

def go_to_checkout(browser):
    checkout_button_locator = (By.CSS_SELECTOR,'#J_SmallSubmit')
    return click_button(browser, checkout_button_locator, '点击结算成功，进入提交订单页面')

def submit_order(browser):
    submit_button_locator = (By.CSS_SELECTOR,'a[title="提交订单"]')
    return click_button(browser, submit_button_locator, '点击提交订单成功')

def jiesuan(buy_time, browser):
    time.sleep(1)
    click_time = datetime.datetime.now()
    time_difference = click_time - buy_time
    print('点击购买的时间差（秒）：', time_difference.total_seconds())

def buy(buy_time, browser):
    while True:
        now = datetime.datetime.now()
        if now >= buy_time:
            break
        time.sleep(0.000001)  
    submit_order(browser)
    jiesuan(buy_time, browser)
    browser.quit()
def pre_load_page(browser):
    # 在此添加页面预加载的代码
    pass

def main():
    buy_time = None
    while not buy_time:
        user_input = input('请输入抢购时间（格式：2024-04-27 20:23:00）：')
        try:
            buy_time = datetime.datetime.strptime(user_input, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print('时间格式错误，请重新输入。')
    # 创建 WebDriver 实例，并设置隐式等待时间
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)  # 设置隐式等待时间为 10 秒
    browser.get('https://www.taobao.com')
    pre_load_page(browser)  # 预加载页面内容
    if login(browser) and go_to_cart(browser) and select_all(browser) and go_to_checkout(browser):
        buy(buy_time, browser)
if __name__ == '__main__':
    main()


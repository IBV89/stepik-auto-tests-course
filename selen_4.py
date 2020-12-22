import math
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_first = browser.find_element_by_class_name('trollface.btn.btn-primary').click()

    new = browser.window_handles[1]
    browser.switch_to.window(new)

    x = int(browser.find_element_by_id('input_value').text)
    func = str(math.log(abs(12*math.sin(x))))

    answer_input = browser.find_element_by_id('answer').send_keys(func)

    button_second = browser.find_element_by_class_name('btn.btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()

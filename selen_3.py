# Работа с модальными окнами

import time
import math
from selenium import webdriver

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_first = browser.find_element_by_class_name('btn-primary').click()
    browser.switch_to.alert.accept()

    x = float(browser.find_element_by_id('input_value').text)
    result = math.log(abs(12 * math.sin(x)))

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(str(result))

    button = browser.find_element_by_class_name('btn.btn-primary').click()


finally:
    time.sleep(5)
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button = WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.ID, 'book'))
    )
    button.click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    func = str(math.log(abs(12*math.sin(x))))

    answer_input = browser.find_element(By.ID, 'answer').send_keys(func)
    button_answer = browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(5)
    browser.quit()

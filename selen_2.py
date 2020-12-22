# Загрузка файла

from selenium import webdriver
import time
import os


link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(path, 'r.txt')

    first_name = browser.find_element_by_name('firstname')
    last_name = browser.find_element_by_name('lastname')
    email = browser.find_element_by_name('email')
    input_file = browser.find_element_by_id('file')
    button = browser.find_element_by_class_name('btn-primary')

    first_name.send_keys('Name')
    last_name.send_keys('Surname')
    email.send_keys('mail@mail.ru')
    input_file.send_keys(path)
    button.click()

finally:
    time.sleep(5)
    browser.quit()


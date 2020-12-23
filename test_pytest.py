import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', ['https://stepik.org/lesson/236895/step/1',
                                   'https://stepik.org/lesson/236896/step/1',
                                   'https://stepik.org/lesson/236897/step/1',
                                   'https://stepik.org/lesson/236898/step/1',
                                   'https://stepik.org/lesson/236899/step/1',
                                   'https://stepik.org/lesson/236903/step/1',
                                   'https://stepik.org/lesson/236904/step/1',
                                   'https://stepik.org/lesson/236905/step/1'])
class TestParametrize():
    def test_text_from_site(self, browser, links):

        link = links
        browser.get(link)
        answer = math.log(int(time.time()))

        input_answer = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.TAG_NAME, 'textarea')))

        input_answer.send_keys(str(answer))
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
        button.click()
        hint = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))).text

        assert hint == "Correct!", f'Сообщение {hint}, ожидалось Correct!'



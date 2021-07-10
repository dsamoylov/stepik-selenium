from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    print(y)


    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)                                          

    checkbox_label = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox_label.click()

    radio_label = browser.find_element_by_css_selector("[for='robotsRule']")
    radio_label.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
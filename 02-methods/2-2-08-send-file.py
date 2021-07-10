from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)
                                                                
    first_name_input = browser.find_element_by_name("firstname")
    first_name_input.send_keys("Dmirty")

    last_name_input = browser.find_element_by_name("lastname")
    last_name_input.send_keys("Samoylov")

    email_input = browser.find_element_by_name("email")
    email_input.send_keys("samoylov@mail.ru")

    file_input = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '2-2-08-file-to-send.txt')
    file_input.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
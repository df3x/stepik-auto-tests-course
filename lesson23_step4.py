from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    alert = browser.switch_to.alert
    #alert_text = alert.text
    alert.accept()

    time.sleep(1)


    #confirm = browser.switch_to.alert
    #confirm.accept()
    #confirm.dismiss()


    #prompt = browser.switch_to.alert
    #prompt.send_keys("My answer")
    #prompt.accept()


    element = browser.find_element_by_id("input_value")
    x = element.text
    y = calc(x)

    element = browser.find_element_by_id("answer")
    element.send_keys(y)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
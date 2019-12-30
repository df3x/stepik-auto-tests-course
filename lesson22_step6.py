from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element_by_id("input_value")
    x = element.text
    y = calc(x)

    element = browser.find_element_by_id("answer")
    element.send_keys(y)

    #button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    element = browser.find_element_by_id("robotCheckbox")
    element.click()

    element = browser.find_element_by_id("robotsRule")
    element.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
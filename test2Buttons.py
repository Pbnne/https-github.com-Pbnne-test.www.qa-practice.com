from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.support.ui import Select    
from time import sleep    
from selenium.webdriver.common.keys import Keys



browser = webdriver.Firefox() 
browser.maximize_window()  # Открываем браузер на полный экран
browser.get("https://www.qa-practice.com/elements/input/simple")
sleep (4)

# Вкладка Button
element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/button')]")
element.click()
sleep (4)
# Клик на кнопку Click (Simple button)
try:
    element = browser.find_element(By.ID, "submit-id-submit")
    element.click()
    print ("Кнопка нажата")

except NoSuchElementException:
    print ("Кнопка не нашлась")
sleep (2)
try:
    element = browser.find_element(By.ID, "result")
    print ("Полуил подтверждение что кнопка сработала")

except NoSuchElementException:
    print ("Кнопка не нашлась")
sleep (2)
# Клик на кнопку Like a button
element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/button/like_a_button')]")
element.click()
sleep (4)
# Клик на кнопку Click (Like a button
try:
    element = browser.find_element(By.XPATH, "//a[@href='#']")
    element.click()
    print ("Кнопка нажата")

except NoSuchElementException:
    print ("Кнопка не нашлась")
sleep (2)
try:
    element = browser.find_element(By.ID, "result")
    print ("Полуил подтверждение что кнопка сработала")

except NoSuchElementException:
    print ("Кнопка не нашлась")

# Клик на кнопку Disabled
element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/button/disabled')]")
element.click()
sleep (4)
try:
    select_element = browser.find_element(By.ID, 'id_select_state')

     # Создайте объект Select
    select = Select(select_element)

     # Выберите последний элемент в списке
    options = select.options  # Получаем все варианты
    select.select_by_visible_text(options[-1].text)
    sleep (1)
    element = browser.find_element(By.ID, "submit-id-submit")
    element.click()
    print ("Кнопка нажата")
except NoSuchElementException:
    print ("Кнопка не нашлась")
sleep (4)
try:
    element = browser.find_element(By.ID, "result")
    text_content = element.text
    print ("Полуил подтверждение что кнопка сработала", text_content)
except NoSuchElementException:
    print ("Кнопка не нашлась")
browser.quit()  # Закрываем браузер после завершения всех тестов

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.support.ui import Select    
from time import sleep    
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox() 
browser.maximize_window()  # Открываем браузер на полный экран
browser.get("https://www.qa-practice.com/elements/button/simple")
sleep (4)

sleep (4)

# Вкладка Button
element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/checkbox')]")
element.click()
sleep (5)


# Найдите все элементы чекбоксов на странице
checkboxes = browser.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
# Выводим количество чекбоксов
print(f'Количество чекбоксов на странице: {len(checkboxes)}')

if {len(checkboxes)} == 1:
    print ("Нашел на странице 1 флажок")
else:
    print ("Больше 1 флажка на странице")

checkboxes[0].click()

sleep (4)

element = browser.find_element(By.ID, "submit-id-submit")
element.click()

try:
    element = browser.find_element(By.ID, "result")
    print ("Полуил подтверждение что кнопка сработала")
except NoSuchElementException:
    print ("Кнопка не нашлась")

sleep (4)

element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/checkbox/mult_checkbox')]")
element.click()
sleep (5)

# Найдите все элементы чекбоксов на странице
checkboxes = browser.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
# Выводим количество чекбоксов
print(f'Количество чекбоксов на странице: {len(checkboxes)}')

if {len(checkboxes)} == 1:
    print ("Нашел на странице 1 флажок")
else:
    print ("Больше 1 флажка на странице")

checkboxes[0].click()
checkboxes[1].click()
checkboxes[2].click()

element = browser.find_element(By.ID, "submit-id-submit")
element.click()

sleep(4)

try:
    element = browser.find_element(By.ID, "result")
    print ("Полуил подтверждение что кнопка сработала")
except NoSuchElementException:
    print ("Кнопка не нашлась")

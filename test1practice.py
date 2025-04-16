import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC




browser = webdriver.Firefox() 
browser.maximize_window()  # Открываем браузер на полный экран
browser.get("https://www.qa-practice.com/elements/input/simple")

# Определяем локатор
element_locator = (By.XPATH, "//a[contains(@href, '/elements/input/email')]")
try:
    # Ожидаем, пока элемент с указанным локатором не появится
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(element_locator)
    )
    print("Элемент найден")
except TimeoutException:
    print("Элемент не найден за отведенное время")
finally:
    print("Загрузил страницу")


# Text input TEST
itams = ["test_user", "example.text", "user-123", "name.surname", "valid_email", "sample-26", "ab", "text_with_underscores", "valid-text", "t12345", " ", "#", "user@localhost", "user@local host", "user@.localhost", "longemailaddresslongemailaddress", "a", "user!", "user@localhost!"]
for item in itams:

    # ПОИСК ПО ID
    input_field = browser.find_element(By.ID, 'id_text_string')
    # Вводим текст в элемент
    input_field.send_keys(item)
    # Нажимаем Enter
    input_field.send_keys(Keys.ENTER)
    
    sleep (4)
    try:
    # Попытка найти элемент по ID
        element = browser.find_element(By.ID, "error_1_id_text_string")
        print("Ошибка:", element.text, item)
        input_field = browser.find_element(By.ID, 'id_text_string')
        input_field.clear()
    except NoSuchElementException:
        print("Ввод текста прошел успешно", item)

# Клик на элемент
element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/input/email')]")
element.click()

element_locator = (By.ID, 'id_email') 

#Email field 
items = ["test@localhost", "user1@localhost", "admin@localhost", "name.surname@localhost", "sample123@localhost", "t@localhost", "u@localhost", "longemailaddress@localhost", "test_email@localhost", "valid-email@localhost.com", "user@localhost!", "user@local host", "user@.localhost"]
for item in items:
    print(item)  # Выводим текущий элемент
    # Поиск поля ввода по ID
    input_field = browser.find_element(By.ID, 'id_email')
    sleep (1)
    # Вводим текст в элемент
    input_field.send_keys(item)
    sleep (1)
    # Нажимаем Enter
    input_field.send_keys(Keys.ENTER)
    sleep (4)
    try:
    # Попытка найти элемент по ID
        element = browser.find_element(By.ID, "error_1_id_email")
        print("Ошибка:", element.text, item)
        input_field = browser.find_element(By.ID, 'id_email')
        input_field.clear()
    except NoSuchElementException:
        print("Ввод email прошел успешно", item)

element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/input/passwd')]")
element.click()
sleep (4)

#Password field
items = ["Password1!", "Hello@123", "Test!2023", "MyP@ssw0rd", "Secure#1abc", "Example1@", "Strong!Pass2", "Valid@Password3", "Qwerty!4", "Abc#1234Def", "1A!bcdEfgh", "P@ssw0rd123", "HelloWorld!5", "Smart@Choice6", "My*Secret7"]
for item in items:
    print(item)
    input_field = browser.find_element(By.ID,"id_password")
    sleep(2)
    input_field.send_keys(item)
    input_field.send_keys(Keys.ENTER)
    sleep(3)
    try:
        element = browser.find_element(By.ID, "error_1_id_password")
        print ("Ошибка найдена", element.text, item)
        input_field = browser.find_element(By.ID,"id_password")
        input_field.clear()
    except NoSuchElementException:
        print ("Ошибка не найдена", item)

browser.quit()  # Закрываем браузер после завершения всех тестов

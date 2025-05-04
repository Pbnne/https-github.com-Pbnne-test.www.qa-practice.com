from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.support.ui import Select    
from time import sleep    
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox() 
browser.maximize_window()  # Открываем браузер на полный экран
browser.get("https://www.qa-practice.com/elements/checkbox/single_checkbox")
sleep (4)

# Вкладка Button
element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/select')]")
element.click()
sleep (5)

element = browser.find_element(By.ID, "id_choose_language")
element.click()
sleep(3)

# Создаем объект Select
select = Select(element)

# Выбираем опцию "Python" по значению
select.select_by_value("1") 

element = browser.find_element(By.ID, "submit-id-submit")
element.click()
sleep(3)

element = browser.find_element(By.XPATH, "//a[contains(@href, '/elements/select/mult_select')]")
element.click()
sleep(3)


element = browser.find_element(By.ID, "id_choose_the_place_you_want_to_go")
element.click()
sleep(3)
# Создаем объект Select
select = Select(element)
# Выбираем опцию "Python" по значению
select.select_by_value("1") 

element = browser.find_element(By.ID, "id_choose_how_you_want_to_get_there")
element.click()
sleep(3)

# Создаем объект Select
select = Select(element)
# Выбираем опцию "Python" по значению
select.select_by_value("2") 

element = browser.find_element(By.ID, "id_choose_when_you_want_to_go")
element.click()
sleep(3)

# Создаем объект Select
select = Select(element)
# Выбираем опцию "Python" по значению
select.select_by_value("3") 


element = browser.find_element(By.ID, "submit-id-submit")
element.click()
sleep(3)

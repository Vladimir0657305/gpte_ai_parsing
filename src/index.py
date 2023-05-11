from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://gpte.ai/")

# Ждем, чтобы страница загрузилась
time.sleep(2)

# Прокручиваем страницу до конца, чтобы загрузить все элементы
while True:
    # Прокручиваем страницу до конца
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Ждем, чтобы страница загрузилась
    time.sleep(2)

    # Проверяем, достигли ли мы конца страницы
    end_of_page = driver.execute_script("return window.innerHeight+window.pageYOffset >= document.body.offsetHeight;")
    if end_of_page:
        break

# Теперь можно парсить содержимое страницы, включая все элементы, загруженные при скролле
content = driver.page_source

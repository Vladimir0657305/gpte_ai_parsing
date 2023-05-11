from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://gpte.ai/")

# Прокручиваем страницу до конца, чтобы загрузить все элементы
while True:
    # Прокручиваем страницу до конца
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Ждем, чтобы страница загрузилась
    time.sleep(15)

    # Проверяем, достигли ли мы конца страницы
    end_of_page = driver.execute_script("return window.innerHeight+window.pageYOffset >= document.body.offsetHeight;")
    if end_of_page:
        break

    # Находим ссылку на Older Posts и кликаем на нее
    older_posts_link = driver.find_element_by_css_selector('nav.pagination a.older-posts')
    older_posts_url = urljoin(driver.current_url, older_posts_link.get_attribute('href'))
    print("Processing URL:", older_posts_url)
    driver.get(older_posts_url)

    # Ждем, чтобы страница загрузилась
    time.sleep(10)

# Теперь можно парсить содержимое страницы, включая все элементы, загруженные при скролле
content = driver.page_source

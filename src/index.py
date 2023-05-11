from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
import time
import pandas as pd

data_all = []

def get_data(driver):
    # Создаем список, в котором будем хранить данные
    data = []
    
    # Находим все элементы статей на странице
    # articles = driver.find_elements_by_css_selector('body div.viewport div.site-content div.total-wrap main.site-main div.inner div.post-feed article.post-card')
    articles = driver.find_elements(By.CSS_SELECTOR, 'body div.viewport div.site-content div.total-wrap main.site-main div.inner div.post-feed article.post-card')


    # Извлекаем информацию из каждой статьи и добавляем ее в список данных
    for article in articles:
        title = article.find_element(By.CSS_SELECTOR, 'h2.post-card-title').text
        category = article.find_element(By.CSS_SELECTOR, '.post-card-primary-tag').text
        description = article.find_element(By.CSS_SELECTOR, 'div.post-card-excerpt').text
        image_url = article.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')

        print("Processing article:", title)
        print("Category:", category)
        print("Description:", description)
        print("Image URL:", image_url)

        data.append({
            'Title': title,
            'Category': category,
            'Description': description,
            'Image URL': image_url
        })

    return data

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://gpte.ai/")

# Получаем данные со стартовой страницы и добавляем их в переменную data
data_all = get_data(driver)

# Прокручиваем страницу до конца, чтобы загрузить все элементы
num_page = 2
while num_page <= 72:
    # Строим URL страницы для парсинга
    url = f"https://gpte.ai/page/{num_page}"

    # Загружаем страницу и получаем данные
    driver.get(url)
    data_all += get_data(driver)

    # Увеличиваем номер страницы
    num_page += 1
# Закрываем драйвер
driver.quit()

# Создаем DataFrame из списка данных
df = pd.DataFrame(data_all)

# Сохраняем DataFrame в CSV-файл
df.to_csv('data.csv', index=False)



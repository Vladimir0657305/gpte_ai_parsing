from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urljoin
import requests
import time
import pandas as pd

last_page = 72
data_all = []

def get_data(driver):
    # Создаем список, в котором будем хранить данные
    data = []
    
    # Находим все элементы статей на странице
    articles = driver.find_elements(By.CSS_SELECTOR, 'body div.viewport div.site-content div.total-wrap main.site-main div.inner div.post-feed article.post-card')

    # Извлекаем информацию из каждой статьи и добавляем ее в список данных
    for article in articles:
        title_elem = article.find_element(By.CSS_SELECTOR, 'h2.post-card-title')
        title = title_elem.text if title_elem else None
        
        # category = None
        for category_selector in ['.post-card-primary-tag', '.post-card-tags']:
            try:
                category_elem = article.find_element(By.CSS_SELECTOR, category_selector)
                category_text = category_elem.text
                if category_text:
                    category_list = category_text.split()
                    if len(category_list) > 1:
                        category = category_list[1]
                    else:
                        category = category_list[0]
                else:
                    category = 'Unknown'
                break
            except NoSuchElementException:
                category = 'Unknown'
                continue
        
        description_elem = article.find_element(By.CSS_SELECTOR, 'div.post-card-excerpt')
        description = description_elem.text if description_elem else None
        
        image_elem = article.find_element(By.CSS_SELECTOR, 'img')
        image_url = image_elem.get_attribute('src') if image_elem else None

        # Извлекаем ссылку
        link = None
        try:
            link_elem = article.find_element(By.CSS_SELECTOR, 'a.post-card-content-link')
            link = link_elem.get_attribute('href')
        except NoSuchElementException:
            link = 'Unknown'
            pass

        try:
            # Переходим по ссылке и получаем URL после переадресации
            response = requests.get(link, verify=False)
            final_url = response.url
        except (requests.exceptions.ConnectionError, AttributeError):
            final_url = 'Unknown'
            pass

        
        print("Processing article:", title)
        print("Category:", category)
        print("Description:", description)
        print("Image URL:", image_url)
        print("Link:", final_url)

        data.append({
            'Title': title,
            'Category': category,
            'Description': description,
            'Image URL': image_url,
            'Link': final_url
        })

    return data



driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://gpte.ai/")

# Получаем данные со стартовой страницы и добавляем их в переменную data
data_all = get_data(driver)

# Прокручиваем страницу до конца, чтобы загрузить все элементы
num_page = 2
while num_page <= last_page:
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
df.to_csv('D:/data.csv', index=False)



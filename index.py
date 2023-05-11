driver = webdriver.Chrome()
driver.get("https://gpte.ai/")

# Ждем, чтобы страница загрузилась
time.sleep(5)

# Прокручиваем страницу до конца, чтобы загрузить все элементы
while True:
    # Прокручиваем страницу до конца
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Ждем, чтобы страница загрузилась
    time.sleep(10)

    # Проверяем, достигли ли мы конца страницы
    end_of_page = driver.execute_script("return window.innerHeight+window.pageYOffset >= document.body.offsetHeight;")
    if end_of_page:
        # Если достигли конца страницы, ждем еще 5 секунд, чтобы дополнительный контент загрузился
        time.sleep(10)

        # Проверяем, есть ли на странице еще элементы для загрузки
        end_of_page = driver.execute_script("return window.innerHeight+window.pageYOffset >= document.body.offsetHeight;")
        if end_of_page:
            # Если есть еще элементы для загрузки, прокручиваем страницу до конца снова
            continue
        else:
            # Если больше нет элементов для загрузки, выходим из цикла
            break

# Теперь можно парсить содержимое страницы, включая все элементы, загруженные при скролле
content = driver.page_source

# gpte.ai parsing

The program does the following:

1. Imports the necessary modules: webdriver from selenium to automate the web browser, Keys to work with the keyboard, By to determine how to find elements on the web page, NoSuchElementException for exception handling, urljoin from urllib.parse to combine URLs, requests for sending HTTP requests, time for execution delays, and pandas for working with data in a table format.

2. Sets the value of the last_page variable to 72, which means that 72 pages will be processed.

3. Creates an empty data_all list that will contain all the data.

4. Defines a get_data(driver) function that will retrieve information from articles on a web page. The function takes a driver object as an argument.

5. Inside the function, finds all article elements on the page using the driver.find_elements() method and a CSS selector.

6. Extracts information from each article such as title, category, description, image URL and link. If the element is not found, sets the corresponding value to None or 'Unknown'.

7. Adds the retrieved data to the data list.

8. Returns the data list from the function.

9. Creates a webdriver.Chrome() object to control the Chrome web browser.

10. Sets an implicit wait of 10 seconds to wait for elements on the page to load.

11. Opens the start page "https://gpte.ai/" using the driver.get() method.

12. Gets the data from the first page and adds it to the data_all variable using the get_data(driver) function.

13. Builds the URL of the page to be parsed, incrementing the page number in each iteration of the loop.

14. Loads the page using the driver.get() method and retrieves the data using the get_data(driver) function.

15. Adds the received data to the data_all variable.

16. Increases the page number.

17. Closes the driver using the driver.quit() method.

18. Creates a DataFrame object from the data_all data list using pd.DataFrame().

19. Saves the DataFrame object to a CSV file using the to_csv() method. The file is saved at the specified path 'D:/data.csv' and without indexes.

[![trophy](https://github-profile-trophy.vercel.app/?username=Vladimir0657305)]([https://github.com/ryo-ma/github-profile-trophy](https://github.com/Vladimir0657305))

[![Ashutosh's github activity graph](https://github-readme-activity-graph.cyclic.app/graph?username=Vladimir0657305&theme=react)](https://github.com/ashutosh00710/github-readme-activity-graph)

![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Vladimir0657305&theme=solarized_dark)

![](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Vladimir0657305&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Vladimir0657305&theme=solarized_dark)

![](https://komarev.com/ghpvc/?username=Vladimir0657305)

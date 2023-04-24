import csv
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.metacritic.com/browse/games/genre/metascore/real-time/all?view=detailed"
driver = webdriver.Chrome()

try:
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "clamp-list")))

    games = driver.find_elements(By.CLASS_NAME, "clamp-summary-wrap")
    game_urls = []

    with open('metacritic.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Platform', 'Date of release', "Genre", 'Rating', "Amount of ratings"])

        for game in games:
            game_title = game.find_element(By.CSS_SELECTOR, "a.title")
            game_url = game_title.text
            link = game_title.get_attribute("href")
            game_urls.append((game_url, link))

        for url in game_urls:
            driver.get(url[1])
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.hover_none")))

            title = driver.find_element(By.CSS_SELECTOR, "a.hover_none").text
            platform = driver.find_element(By.CSS_SELECTOR, "span.platform").text
            rating = driver.find_element(By.CSS_SELECTOR, "span[itemprop='ratingValue']").text

            date_element = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[3]/ul/li[2]/span[2]").text
            date_obj = datetime.strptime(date_element, "%b %Y")
            date = date_obj.strftime("%m/%Y")

            try:
                amount_ratings = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/p/span[2]/a").text
                genre = driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul/li[2]/span[4]').text
            except Exception as ex:
                amount_ratings = ""
                genre = ""

            writer.writerow([title, platform, date, genre, rating, amount_ratings])
except Exception as ex:
    print(ex)

finally:
    driver.quit()
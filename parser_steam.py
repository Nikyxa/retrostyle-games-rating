import csv
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://steam250.com/tag/rts"
driver = webdriver.Chrome()

try:
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "col1")))

    games = driver.find_elements(By.CLASS_NAME, "appline")

    with open('steam.csv', mode='w', encoding='utf-8', newline='', ) as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Platform', 'Date of release', "Genre", 'Rating', "Amount of ratings"])

        for game in games:
            title = game.find_element(By.TAG_NAME, 'a').text
            genre = game.find_element(By.CLASS_NAME, "genre").text

            rating_element = game.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/span[2]").text
            rating = float(rating_element.strip('%')) / 100

            amount_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/span[3]").text.split()
            amount_ratings = amount_element[0]

            date_element = game.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/span[3]/a").text
            date_obj = datetime.strptime(date_element, "%b %Y")
            date = date_obj.strftime("%m/%Y")

            platform_element = game.find_element(By.CSS_SELECTOR, 'span.win')
            platform = platform_element.get_attribute('title')

            writer.writerow([title, platform, date, genre, rating, amount_ratings])

except Exception as ex:
    print(ex)

finally:
    driver.quit()
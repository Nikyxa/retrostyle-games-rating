import csv

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

    with open('steam.csv', mode='w', newline='', ) as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Genre', 'Date of release', 'Rating'])

        for game in games:
            title = game.find_element(By.TAG_NAME, 'a').text
            # platform = game.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[5]/div[2]/span/span").text
            date = game.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/span[3]/a").text
            genre = game.find_element(By.CLASS_NAME, "genre").text
            rating = game.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/span[2]").text

            writer.writerow([title, genre, date, rating])

except Exception as ex:
    print(ex)

finally:
    driver.quit()
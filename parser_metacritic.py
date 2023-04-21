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

    for game in games:
        title = game.find_element(By.CSS_SELECTOR, "a.title").text
        platform = game.find_element(By.CSS_SELECTOR, "span.data").text
        date = game.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/div[2]/span",
        ).text
        rating = game.find_element(By.CLASS_NAME, "metascore_w").text
        # description = game.find_element(By.CSS_SELECTOR, "a.title").text
        print(f"Title: {title}, Platform: {platform}, Date of release: {date}, Rating: {rating}")
except Exception as ex:
    print(ex)

finally:
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.gamespot.com/new-games/?sort=score&game_filter%5Bplatform%5D=all&game_filter%5Bgenres%5D%5B%5D=44&game_filter%5BminRating%5D=&game_filter%5BtimeFrame%5D=all&game_filter%5BstartDate%5D=&game_filter%5BendDate%5D=&game_filter%5Btheme%5D=&game_filter%5Bregion%5D=&___game_filter%5Bdevelopers%5D=&___game_filter%5Bpublishers%5D="
driver = webdriver.Chrome()

try:
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "editorial")))

    games = driver.find_elements(By.CSS_SELECTOR, "div.media")

    for game in games:
        title = game.find_element(By.CLASS_NAME, "media-title").text
        # platform = game.find_element(By.CSS_SELECTOR, "span.data").text
        date = game.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div/section/section/section/div[1]/a/div[2]/div/time/span",
        ).text
        rating = game.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div/section/section/section/div[1]/a/div[1]/div[1]/span[1]/strong").text
        # description = game.find_element(By.CSS_SELECTOR, "a.title").text
        print(f"Title: {title}, Date of release: {date}, Rating: {rating}")
except Exception as ex:
    print(ex)

finally:
    driver.quit()
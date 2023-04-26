import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://en.wikipedia.org/wiki/Pikmin_2"
driver = webdriver.Chrome()

try:
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "infobox-label")))

    with open("pikmin2_info.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Title",
                "Developer(s)",
                "Producer(s)",
                "Designer(s)",
                "Info",
            ]
        )

        title = driver.find_element(By.CLASS_NAME, "firstHeading").text
        developer = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[3]/td").text
        producer = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[6]/td").text
        designer = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[7]/td").text
        info = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[3]").text
        writer.writerow([title, developer, producer, designer, info])

except Exception as ex:
    print(ex)

finally:
    driver.quit()

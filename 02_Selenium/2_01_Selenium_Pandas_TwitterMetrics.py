from selenium import webdriver

import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.chrome.options import Options
chrome_optionsme = Options()
chrome_optionsme.add_argument("--incognito")
chrome_optionsme.add_argument("--window-size=1920x1080")
import datetime


#chrome_driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_optionsme)
driver.get("https://twitter-trends.iamrohit.in/")


main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "panel-body")))

main = (main.text)
ranking_list = []
trending_list = []
volume_list = []
text_raw = main.split('\n')

for line in text_raw[2:-2]:
    ranking = line.split('. ')[0]
    tweet_raw = line.split('. ')[1]
    volume = tweet_raw.split(" ")[-2]
    trending = tweet_raw.split(volume)[0]
    ranking_list.append(ranking)
    trending_list.append(trending)
    volume_list.append(volume)
today = datetime.date.today()
date = f'{today:%Y-%m-%d}'
csv_name = f'twitter_metrics_{date}.csv'
print('Writing data in: ', csv_name)
df = pd.DataFrame({"Ranking": ranking_list, "Trending": trending_list, "Volume": volume_list})
df.to_csv(csv_name, encoding='utf-8', index=False)


#    driver.quit()

driver.quit()
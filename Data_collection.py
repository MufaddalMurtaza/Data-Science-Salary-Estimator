import Scraper_bot as sb
import pandas as pd

path = "C:\Program Files (x86)\chromedriver.exe"

df = sb.get_jobs('Data-Scientist',
                 1000,
                 True,
                 path = path,
                 slp_time=10)

df.to_csv('US_DS_jobs.csv')

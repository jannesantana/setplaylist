import os
from dotenv import load_dotenv
load_dotenv()
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time




def open_URL_spit_songs(url): 
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url) # loads the JS from the url
    time.sleep(3)  # wait for the JS to load
    

    soup = BeautifulSoup(driver.page_source, "html.parser") # uses BeautifulSoup to parse the html and extracts the artist name and the songs
    artist = soup.find("meta", property="qc:artist")
    driver.quit()

    songs = [li.get_text(strip=True).removesuffix('Play Video') for li in soup.select("li.setlistParts.song")]

    return artist["content"],songs 
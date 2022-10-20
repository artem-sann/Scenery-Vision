from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from random import choice
from tqdm import trange, tqdm
import time
PATH_TO_VENDOR_CODES = "vendor_codes.csv"

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--start-maximized")
# options.add_argument("--no-sandbox") #bypass OS security model
# options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)


def get_html(link: str, name_file: str, dir_to_page_source: str):
    scroll_pause_time = 0.8
    driver.get(link)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(choice([0.5, 0.6, 0.7]))
    with open(f"{dir_to_page_source}/{name_file}.html", "a") as f:
        f.write(driver.page_source)


with open(PATH_TO_VENDOR_CODES, "r") as file:
    codes = file.readlines()[10405:] # 94021766
    for code in tqdm(codes):
        name_file = code.strip()
        link = f"https://sokolov.ru/jewelry-catalog/product/{name_file}/"
        dir_to_page_source = "data_html"
        try:
            get_html(link, name_file, dir_to_page_source)
        except Exception as ex:
            print(code)
            print(ex)
            print("\n")
            with open("error_vendor_codecs.csv", "a") as error_file:
                error_file.write(code + "\n")
driver.close()

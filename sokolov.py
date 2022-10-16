from bs4 import BeautifulSoup
from glob import glob
from random import randint
from requests import get
from time import sleep
from tqdm import trange, tqdm

PAGE_COUNT = 482

for i in trange(1, PAGE_COUNT + 1):
    res = get(f"https://sokolov.ru/jewelry-catalog/?page={i}")

    with open(f"data/{i}.html", "wb") as f:
        f.write(res.content)

    sleep(randint(4, 7))


for item in tqdm(glob("data/*.html")):
    with open(item, "rb") as file:
        bs = BeautifulSoup(file.read(), "html.parser")

    parsed = bs.find_all("script")[5]
    text = parsed.text

    with open(f"data/{i}.json", "w", encoding='utf8') as f:
        f.write(text[text.find('characteristics:') + len('characteristics:'):text.find('window.app.sort') - len('}\n}      }\n    };\n\n    \n    //window.app.templateData.filters.items[10000] = {\n')])

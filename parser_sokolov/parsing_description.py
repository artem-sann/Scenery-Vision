from bs4 import BeautifulSoup
from glob import glob
from tqdm import tqdm

for i, item in enumerate(tqdm(glob("data_html/*.html")), start=1):
    flag = False
    name_file = item[10:].split(".")[0]
    with open(item, "rb") as file:
        bs = BeautifulSoup(file.read(), "lxml")
    parsed_data = bs.find("div", attrs={"class": "sklv-product-page-tabs-tab inner", "data-tab-id": "about"})
    try:
        if parsed_data is not None:
            splits = parsed_data.text.strip().split("\n", maxsplit=1)
            if splits[0] == "Об украшении":
                text_1 = splits[1].replace('\xa0', ' ')
                with open('description_data.csv', 'a') as csvfile:
                    csvfile.write(",".join([name_file, text_1]))
                    csvfile.write("\n")
                flag = True

        parsed_data = bs.find("div", attrs={"class": "sklv-product-page-tabs-tab inner", "data-tab-id": "about-collection"})
        if parsed_data is not None and flag:
            splits = parsed_data.text.strip().split("\n", maxsplit=1)
            if splits[0] == "О коллекции":
                text_2 = splits[1].replace('\xa0', ' ')
                with open('description_data.csv', 'a') as csvfile:
                    csvfile.write(",".join([name_file, text_1 + " " + text_2]))
                    csvfile.write("\n")
    except Exception as ex:
        print(name_file)
        print(ex)

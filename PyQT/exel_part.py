import json
import pandas as pd
import re
import requests


def delete_empty_info(data: list) -> list:
    to_del = []
    reformated_data = data.copy()
    u = 0
    for txt in data:
        for txt_elem in txt:
            if txt[txt_elem] == "":  # Тут не должно быть индекса?
                to_del.append(txt_elem)
        for p in range(len(to_del)):
            del reformated_data[u][to_del[p]]
        to_del.clear()
        u = u + 1

    return reformated_data


def delete_useless_info(data: list) -> list:
    j = 0
    for txt in data:
        if txt["Свойство"] == "ИД товара на площадке Tmall" or txt["Свойство"] == "Код ролика на YouTube":
            del data[j]
        j = j + 1
    return data


def filter_camel_for_text(text: str) -> str:
    if "JSON" in text:
        return text
    result = text[0].upper()
    for el in text[1:]:
        if el.isupper():
            result += " "
        result += el.lower()
    return result


def filter_camel_for_json(json_to_reformat: list) -> list:
    for unit in json_to_reformat:
        for key in unit.copy():
            unit[filter_camel_for_text(key)] = unit.pop(key)
    return json_to_reformat


def remove_text_between_parens(text: str) -> str:
    n = 1
    while n:
        text, n = re.subn(r'\([^()]*\)', '', text)
    return text


def fix_foto_links(link: str) -> str:
    link = link.replace(chr(92), "/")
    return link


def reformat_json(j_data: list) -> dict:
    new_json = {}
    for unit in j_data:
        if len(unit) == 2 and "Свойство" in unit and "Значение" in unit:
            key, value = unit["Свойство"], unit["Значение"]
            new_json[key] = value
    return new_json


def load_and_processing_excel(filename: str):  # загрузка файла и первичная обработка таблицы
    file = filename
    xl = pd.ExcelFile(file)

    # берем первый лист и переводим в dataframe
    sheet = xl.sheet_names
    df1 = xl.parse(sheet[0])

    # удаление пустых столбцов и строчек, сброс индексации и переименование столбцов
    df1.dropna(axis='columns', how='all', inplace=True)
    df1.dropna(axis=0, how='all', inplace=True)
    df1.reset_index(drop=True, inplace=True)

    # применяем Camel фильтр
    for i in range(len(df1.columns)):
        df1.iloc[0][i] = filter_camel_for_text(df1.iloc[0][i])

    # Обновляем индексацию
    headers = df1.iloc[0]
    table = pd.DataFrame(df1.values[1:], columns=headers)
    table.dropna(axis='columns', how='all', inplace=True)

    # удаление столбцов, где все значения одинаковые
    cols = table.columns
    for i in range(len(table.columns)):
        unics = table[cols[i]].unique()
        if len(unics) == 1 and table[cols[i]].isna().sum() == 0:
            table.drop([cols[i]], axis=1, inplace=True)

    # удаление мусора в скобках
    table["JSONГабариты"] = table["JSONГабариты"].apply(remove_text_between_parens)
    table["JSONВставки"] = table["JSONВставки"].apply(remove_text_between_parens)
    table["JSONТеги"] = table["JSONТеги"].apply(remove_text_between_parens)

    # преобразование строк в json формат
    table["JSONВставки"] = table["JSONВставки"].apply(json.loads)
    table["JSONГабариты"] = table["JSONГабариты"].apply(json.loads)
    table["JSONТеги"] = table["JSONТеги"].apply(json.loads)

    # camel для столбцов
    table["JSONВставки"] = table["JSONВставки"].apply(filter_camel_for_json)  # type: ignore

    # очистка json от мусора
    table["JSONГабариты"] = table["JSONГабариты"].apply(delete_useless_info)  # type: ignore
    table["JSONВставки"] = table["JSONВставки"].apply(delete_empty_info)  # type: ignore
    table["JSONГабариты"] = table["JSONГабариты"].apply(delete_empty_info)  # type: ignore

    table["JSONГабариты"] = table["JSONГабариты"].apply(reformat_json)
    table["Путь к фото"] = table["Путь к фото"].apply(fix_foto_links)
    table["Описание"] = ""

    return table  # return dataframe table


def download_image(link: str, name: str) -> None:  # link from table["Путь к фото"]  name from table['Наименование']
    img = requests.get(link)
    locate = './jewelry_images' + str(name) + '.jpg'
    img_file = open(locate, 'wb')
    img_file.write(img.content)
    img_file.close()


def excel_save(table: pd.DataFrame, path):  # сохраняет таблицу по указанному пути
    table.to_excel(path, index=False)
    return True


def transform_to_json(df: pd.DataFrame):  # преобразует таблицу для отправки в api
    results = []
    columns = df.columns
    for index, row in df.iterrows():
        dict_json = {}
        mask = pd.notna(row)
        row = row[mask]
        new_columns = columns[mask]
        for column, unit in zip(new_columns, row):
            dict_json[column] = unit
        results.append(dict_json)
    return results

# TEST
#path = "C:/Users/artem/Documents/Scenery-Vision/one.xlsx"
#print(load_and_processing_excel(path))

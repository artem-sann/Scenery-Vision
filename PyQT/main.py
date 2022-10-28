import json
import pandas as pd
import re

# file = input("Введите название файла: ")
file = 'All.xlsx'
xl = pd.ExcelFile(file)

# берем первый лист и переводим в dataframe
sheet = xl.sheet_names
df1 = xl.parse(sheet[0])


def delete_empty_info(data):
    to_del = []
    data1 = data
    u = 0
    for txt in data:
        for txt1 in txt:
            if txt[txt1] == "":
                to_del.append(txt1)
        for p in range(len(to_del)):
            del data1[u][to_del[p]]
        to_del.clear()
        u = u + 1

    return data1


def delete_useless_info(data):
    j = 0
    for txt in data:
        if txt["Свойство"] == "ИД товара на площадке Tmall" or txt["Свойство"] == "Код ролика на YouTube":
            del data[j]
        j = j + 1
    return data


def filter_camel_for_text(text):
    if "JSON" in text:
        return text
    result = text[0].upper()
    for el in text[1:]:
        if el.isupper():
            result += " "
        result += el.lower()
    return result


def filter_camel_for_json(json):
    for unit in json:
        for key in unit.copy():
            unit[filter_camel_for_text(key)] = unit.pop(key)
    return json


def remove_text_between_parens(text):
    n = 1
    while n:
        text, n = re.subn(r'\([^()]*\)', '', text)
    return text


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

# camel для колонки

# преобразование строк в json формат
table["JSONВставки"] = table["JSONВставки"].apply(json.loads)
table["JSONГабариты"] = table["JSONГабариты"].apply(json.loads)
table["JSONТеги"] = table["JSONТеги"].apply(json.loads)

table["JSONВставки"] = table["JSONВставки"].apply(filter_camel_for_json)

# очистка json от мусора
table["JSONГабариты"] = table["JSONГабариты"].apply(delete_useless_info)
table["JSONВставки"] = table["JSONВставки"].apply(delete_empty_info)


# print(table["JSONВставки"][1])
# table["JSONВставки"][1] = camel_to_json(table["JSONВставки"][1])
# print(table["JSONВставки"][1])


def reformat_json(json):
    new_json = {}
    for unit in json:
        if len(unit) == 2 and "Свойство" in unit and "Значение" in unit:
            key, value = unit["Свойство"], unit["Значение"]
            new_json[key] = value
    return new_json


def transform_to_json(df: pd.DataFrame):
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

# json.dumps(transform_to_json(table), indent=4, ensure_ascii=False)

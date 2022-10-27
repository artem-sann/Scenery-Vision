import json
import pandas as pd
import re

# file = input("Введите название файла: ")
file = 'All.xlsx'
xl = pd.ExcelFile(file)

# берем первый лист и переводим в dataframe
sheet = xl.sheet_names
df1 = xl.parse(sheet[0])


def filter_camel_case(text):
    if "JSON" in text:
        return text
    result = text[0].upper()
    for el in text[1:]:
        if el.isupper():
            result += " "
        result += el.lower()
    return result


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
    df1.iloc[0][i] = filter_camel_case(df1.iloc[0][i])

# Обновляем индексацию
headers = df1.iloc[0]
table = pd.DataFrame(df1.values[1:], columns=headers)
table.dropna(axis='columns', how='all', inplace=True)

# удаление столбцов где все значения одинаковые
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

print(table)

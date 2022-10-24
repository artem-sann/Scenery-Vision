import pandas as pd

file = input("Введите название файла: ")
xl = pd.ExcelFile(file)

# массив из названий листов
sheet = xl.sheet_names

# переводим в dataframe
df1 = xl.parse(sheet[0])
print(df1)



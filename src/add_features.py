import pandas as pd

# Загрузка данных с явным указанием разделителя и заголовков
df = pd.read_csv('data/train/normalized_train.csv', sep=';')

# Проверка столбцов
print("Доступные столбцы:", df.columns.tolist())

# Создание новой фичи на основе столбца 'Area'
df['New_Feature'] = df['Area'] * 2

# Сохранение результата
df.to_csv('data/train/final_train.csv', index=False, sep=';')
print("Данные успешно обработаны и сохранены!")
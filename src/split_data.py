import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Загрузка очищенных данных
df = pd.read_csv('data/prepare/cleaned_data.csv', sep=';')

# Разделение данных (80% - train, 20% - test)
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Сохранение результатов
train.to_csv('data/train/train.csv', index=False, sep=';')
test.to_csv('data/val/test.csv', index=False, sep=';')

print(f"Данные разделены: {len(train)} тренировочных и {len(test)} тестовых записей")
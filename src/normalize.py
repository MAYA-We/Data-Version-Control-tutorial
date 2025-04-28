import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

# Загрузка тренировочных данных
train_path = 'data/train/train.csv'
df = pd.read_csv(train_path, sep=';')

# Проверка данных перед нормализацией
print("\nДо нормализации:")
print(f"- Минимальное значение Area: {df['Area'].min()}")
print(f"- Максимальное значение Area: {df['Area'].max()}")

# Создание и применение нормализатора
scaler = MinMaxScaler()
df['Area'] = scaler.fit_transform(df[['Area']])

# Проверка результатов
print("\nПосле нормализации:")
print(f"- Минимальное значение Area: {df['Area'].min()}")
print(f"- Максимальное значение Area: {df['Area'].max()}")

# Сохранение результатов
output_path = 'data/train/normalized_train.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False, sep=';')

print(f"\nНормализованные данные сохранены в {output_path}")
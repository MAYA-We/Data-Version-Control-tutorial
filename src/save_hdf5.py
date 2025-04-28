import pandas as pd

# Загрузка нормализованных данных
df = pd.read_csv('data/train/normalized_train.csv')

# Сохранение в HDF5 (бинарный формат)
df.to_hdf(
    'data/train/train.h5',  # Путь к выходному файлу
    key='df',               # Ключ для доступа к данным
    mode='w'               # Режим записи (перезапись, если файл существует)
)

print("Данные успешно сохранены в HDF5!")
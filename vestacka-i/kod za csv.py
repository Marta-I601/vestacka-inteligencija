import pandas as pd

# Definisemo kolone
columns = [
    'animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 
    'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 
    'tail', 'domestic', 'catsize', 'class_type'
]

# Ucitavamo podatke
data = pd.read_csv('C:\\Users\\HP\\vestacka-i\\zoo.data', names=columns)

# Snimiju se podaci u CSV fajl
data.to_csv('C:\\Users\\HP\\vestacka-i\\zoo.csv', index=False)

# Broj zivotinja po tipu klase
class_counts = data['class_type'].value_counts().reset_index()
class_counts.columns = ['class_type', 'count']

# Snimi brojanje u CSV fajl
class_counts.to_csv('C:\\Users\\HP\\vestacka-i\\class_counts.csv', index=False)

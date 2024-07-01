import pandas as pd

# Preuzimanje podataka
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data'
column_names = ["animal_name", "hair", "feathers", "eggs", "milk", "airborne", "aquatic", "predator", 
                "toothed", "backbone", "breathes", "venomous", "fins", "legs", "tail", "domestic", 
                "catsize", "class_type"]
zoo_data = pd.read_csv(url, names=column_names)

# Pregled podataka
print(zoo_data.head())

import matplotlib.pyplot as plt

# Analiza podataka - broj zivotinja po klasama
class_counts = zoo_data['class_type'].value_counts()

# Prikazi mi rezulte
plt.bar(class_counts.index, class_counts.values)
plt.xlabel('Class Type')
plt.ylabel('Number of Animals')
plt.title('Number of Animals per Class Type')
plt.show()

# Cuvanje rezultata za MATLAB
class_counts.to_csv('class_counts.csv', header=True)

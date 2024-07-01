import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Ucitaj podatke
columns = [
    'animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 
    'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 
    'tail', 'domestic', 'catsize', 'class_type'
]

data = pd.read_csv('C:\\Users\\HP\\vestacka-i\\zoo.data', names=columns)

# Provera broja instanci i osobina
print(f"Broj instanci: {data.shape[0]}")
print(f"Broj osobina (kolona): {data.shape[1] - 2}")  # Oduzimamo 2 jer su 'animal_name' i 'class_type' kolone svaka za sebe

# Provera nedostajucih vrednosti
print("Nedostajuće vrednosti po kolonama:")
print(data.isnull().sum())

# Provera i uklanjanje duplikata
duplicates = data.duplicated(subset=['animal_name'])
print(f"Broj duplikata: {duplicates.sum()}")
data = data.drop_duplicates(subset=['animal_name'])

# Prikaz prvih nekoliko redova podataka
print(data.head())

# Distribucija klasa
class_counts = data['class_type'].value_counts()
class_counts.plot(kind='bar')
plt.xlabel('Tip klase')
plt.ylabel('Broj zivotinja')
plt.title('Broj zivotinja po tipu klase')
plt.show()

# Analiziramo osobinu za svaku klasu
class_groups = data.groupby('class_type').mean()
print(class_groups)

# Korelacija osobina
correlation_matrix = data.drop(columns=['animal_name', 'class_type']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation between Features')
plt.show()

# Priprema podataka
X = data.drop(columns=['animal_name', 'class_type'])
y = data['class_type']

# Podela podataka na trening i test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Kreiranje i treniranje modela
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predikcija i evaluacija
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# 1.Chargement des données
df = pd.read_csv('C:/Users/jallo/Desktop/Apprendre/courses_info.csv')
print("Les 5 premières lignes : \n",df.head()) # Les 5 premières lignes
print("Informations générales :\n",df.info()) # Infos générales (types, colonnes, valeurs manquantes)
print("Nom des colonnes :\n",df.columns) # Nom des colonnes
print("Statistiques descriptives :\n",df.describe(include='all')) # Statistiques descriptives
print(df.isna().mean()) # Données manquantes

# 2. Visualisation
 #Nombre de formations par thématique
 # Taille du graphique
plt.figure(figsize=(12, 6))

# Comptage des formations par thématique
import matplotlib.pyplot as plt

# Count occurrences of each theme
theme_counts = df['theme'].value_counts()

# Plot the data
plt.bar(theme_counts.index, theme_counts.values)

# Add labels and title
plt.title("Nombre de formations par thématique")
plt.xlabel("Nombre de formations")
plt.ylabel("Thématique")

# Adjust layout for better display
plt.tight_layout()

# Show the plot
plt.show()

 


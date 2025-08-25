import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement du Jeu de données
df = pd.read_csv('C:/Users/jallo/Desktop/ProjetS_DA/Salary_Data.csv')
print("Les 5 premières lignes :\n",df.head())
# Voir les informations
print("Les informations :\n",df.info())
# Les statistiques
print("Les statistiques :\n",df.describe())
# le nombre de lignes et de colonnes du DataFrame
print("La taille du DataFrame:\n",df.shape)

# Voir s'il y'a des duplications 
print("Nombre de duplications :\n",df.duplicated().sum())
# Voir s'il y'a des valeurs nulles
print("Les valeurs nulles de chaque colonne:\n",df.isnull().sum())

# Nettoyage des données
 # supprimer les doubons
df = df.drop_duplicates() 
print("Nombre de duplications :\n",df.duplicated().sum())
 # Corriger les colonnes nulle
df['Age'] = df['Age'].fillna(df["Age"].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Years of Experience'] = df["Years of Experience"].fillna(df['Years of Experience'].median())
df['Gender'] = df['Gender'].fillna('Non Spécifié')
df['Education Level'] = df['Education Level'].fillna(df['Education Level'].mode()[0])
df['Job Title'] = df['Job Title'].fillna(df['Job Title'].mode()[0])
print("Les valeurs nulles de chaque colonne:\n",df.isnull().sum())

# Calcul des mesures de tendance centrale
 # 1.La moyenne
Age_Moyenne = df['Age'].mean()
Salary_Moyenne = df['Salary'].mean()
Experience_Moyenne = df['Years of Experience'].mean()
 # 2.La médiane
Age_Mediane = df['Age'].median()
Salary_Mediane = df['Salary'].median()
Experience_Mediane = df['Years of Experience'].median()
 # 3.Le mode
Gender_Mode = df['Gender'].mode()
Education_Mode = df['Education Level'].mode()
Job_Mode = df['Job Title'].mode()
Age_Mode = df['Age'].mode()
Salary_Mode = df['Salary'].mode()
Experience_Mode = df['Years of Experience'].mode()
# Affichage
print("=== Moyenne ===")
print("Âge moyen :", Age_Moyenne)
print("Salaire moyen :", Salary_Moyenne)
print("Expérience moyenne :", Experience_Moyenne)

print("\n=== Médiane ===")
print("Âge médian :", Age_Mediane)
print("Salaire médian :", Salary_Mediane)
print("Expérience médiane :", Experience_Mediane)

print("\n=== Mode ===")
print("Genre le plus fréquent :", Gender_Mode)
print("Niveau d'éducation le plus fréquent :", Education_Mode)
print("Poste le plus fréquent :", Job_Mode)
print("Âge le plus fréquent :", Age_Mode)
print("Salaire le plus fréquent :", Salary_Mode)
print("Expérience la plus fréquente :", Experience_Mode)

#Calcul des mesures de dispersion
 # Écart-type (standard deviation)
ecart_type_age = df['Age'].std()
ecart_type_salaire = df['Salary'].std()
ecart_type_experience = df['Years of Experience'].std()

# Variance
variance_age = df['Age'].var()
variance_salaire = df['Salary'].var()
variance_experience = df['Years of Experience'].var()

# Étendue (valeur max - valeur min)
etendue_age = df['Age'].max() - df['Age'].min()
etendue_salaire = df['Salary'].max() - df['Salary'].min()
etendue_experience = df['Years of Experience'].max() - df['Years of Experience'].min()

#Affichage
print("\n=== Ecart-type ===")
print("Ecart-type Age :", ecart_type_age)
print("Ecart-type Salaire :", ecart_type_salaire)
print("Ecart-type Expérience :", ecart_type_experience)

print("\n=== Variance ===")
print("Variance Age :", variance_age)
print("Variance Salaire :", variance_salaire)
print("Variance Expérience :", variance_experience)

print("\n=== Etendue ===")
print("Etendue Age:", etendue_age)
print("Etendue Salaire :", etendue_salaire)
print("Etendue Expérience :", etendue_experience)

# Importer le fichier
df.to_csv('C:\\Users\\jallo\\Desktop\\ProjetS_DA\\Salary_Data_Cleaned.csv', index=False)










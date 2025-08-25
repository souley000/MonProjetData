import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1.Chargement du ficher
data = pd.read_csv('C:/Users/jallo/Desktop/CoursDA/PD_DA/employes.csv')
print("Voici la liste des employés :\n",data)

# 2.Identifier et afficher les valeurs manquantes.
lack = data.isnull().sum()
print("Les valeurs manquantes :\n",lack)
# Remplace l'âge manquant par la moyenne des âges
data['Age'] = data['Age'].fillna(data['Age'].mean()).astype(int)

# 3.Détecter les valeurs aberrantes du salaire (trop élevées ou négatives) 
# # Définir les seuils pour les outliers
q1 = data['Salaire'].quantile(0.25)
q3 = data['Salaire'].quantile(0.75)
Iqr = q3 - q1
outliers_bas = q1 - 1.5*Iqr
outliers_haut = q3 + 1.5*Iqr
# Supprimer les outliers
data_clean = data[(data['Salaire'] >= outliers_bas) & (data['Salaire'] <= outliers_haut)].copy()


# 4.Standardiser le format des noms et départements
data['Nom'] = data['Nom'].str.strip().str.lower()
data['Département'] = data['Département'].str.strip().str.lower()

# 5. Ajouter une colonne "Expérience"
def categoriser_experience(age):
    if age < 30:
        return "Débutant"
    elif 30 <= age <= 40:
        return "Intermédiaire"
    else:
        return "Senior"
data_clean['Expérience'] = data_clean['Age'].apply(categoriser_experience)

# Affichage du résultat final
print("\n✅ Données nettoyées :\n", data_clean)

# télécharger les données
data_clean.to_csv('C:/Users/jallo/Desktop/CoursDA/PD_DA/employes_nettoyes.csv', index=False)

# Représentation graphiques :
# Histogramme
sns.histplot(data['Salaire'], kde=True)  # Histogramme avec une courbe de densité (KDE)
plt.xlabel('Salaire')
plt.ylabel('Fréquence')
plt.title('Distribution des salaires')
plt.show()

#Diagramme de dispersion
sns.scatterplot(x=data['Age'], y=data['Salaire'])
plt.xlabel('Âge')
plt.ylabel('Salaire')
plt.title('Relation entre l\'âge et le salaire')
plt.show()

# Graphique en ligne 
sns.lineplot(x=data['Age'], y=data['Salaire'])
plt.xlabel('Âge')
plt.ylabel('Salaire')
plt.title('Tendance des salaires selon l\'âge')
plt.show()

#Diagramme en barre
sns.barplot(x='Département', y='Salaire', data=data)
plt.xlabel('Département')
plt.ylabel('Salaire moyen')
plt.title('Salaire moyen par département')
plt.show()

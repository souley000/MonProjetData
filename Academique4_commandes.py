import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement du fichier
commande = pd.read_csv('C:/Users/jallo/Desktop/CoursDA/PD_DA/commandes.csv')
print("La liste des commandes : \n", commande)

# Valeurs manquantes
print("Les valeurs NaN :\n",commande.isnull().sum())
commande['Quantité'] = commande['Quantité'].fillna(commande['Quantité'].mean())
commande['Prix_Unitaire'] = commande['Prix_Unitaire'].fillna(commande['Prix_Unitaire'].mean())
# Les doublons 
print("Les doublons:\n",commande.loc[commande.duplicated(subset=['Commande_ID','Date','Client','Produit','Quantité','Prix_Unitaire','Total','Statut'])])
commande  = commande.drop_duplicates()
# Format texte
commande['Client'] = commande['Client'].str.strip().str.title()
commande['Produit'] = commande['Produit'].str.strip().str.title()
# Correction des totaux
commande.drop(columns=['Total'], inplace=True)
commande['Total_calculé'] = commande['Quantité'] * commande['Prix_Unitaire']
commande.rename(columns={'Total_calculé': 'Total'}, inplace=True)

commande.to_csv('C:/Users/jallo/Desktop/CoursDA/PD_DA/commandes_nettoyées.csv', index=False)
print("Les données nettoyées :\n",commande)
print("Les données sont enregistrées en format csv.")

# Visualisation des données
# 1. Afficher les totals des ventes
# vente_par_client = commande.groupby('Client')['Total'].sum().sort_values(ascending=False)
# sns.barplot(x=vente_par_client.index, y=vente_par_client.values)
# plt.figure(figsize=(8,4))
# plt.title("Total des ventes par client")
# plt.ylabel("Montant total (€)")
# plt.xlabel("Client")
# plt.xticks(rotation=45)
# plt.tight_layout()
# #plt.show()


#Diagramme en barre des produits
plt.figure(figsize=(8, 4))
sns.barplot(x='Produit',y='Quantité', data=commande)
plt.xlabel("Produits")
plt.ylabel("Quantités")
plt.title("Les produits les plus vendus")

plt.xticks(rotation=45)  # Incliner les noms des produits si nécessaire
plt.show()

# Histogramme des produits
plt.hist(commande['Quantité'], bins=5, color='red', edgecolor='black')
plt.xlabel('Quantités')
plt.ylabel('Nombre de commandes')
plt.title("Répartition des quantités commandées")
plt.show()
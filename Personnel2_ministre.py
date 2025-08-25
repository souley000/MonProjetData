import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# 1.Chargement des données
df = pd.read_csv('C:/Users/jallo/Desktop/Apprendre/ministere-de-linterieur-discussions-2025-04-18-15-28.csv', sep=';')
# print("Les 5 premières lignes : \n",df.head()) # Les 5 premières lignes
# print("Informations générales :\n",df.info()) # Infos générales (types, colonnes, valeurs manquantes)
# print("Nom des colonnes :\n",df.columns) # Nom des colonnes
# print("Statistiques descriptives :\n",df.describe(include='all')) # Statistiques descriptives
# print(df.isna().mean()) # Données manquantes

# 2.Nettoyage et manipulation
df_clean = df[['id','user','subject','title', 'size', 'participants', 'messages', 'closed', 'closed_by']].copy()
print(df_clean)
print(df_clean.info())
print(df_clean.describe(include='all'))
print(df_clean.isna().mean())  # Vérifie la proportion de valeurs manquantes

print("Type de message :",df_clean['messages'].dtype)
df_clean['messages'] = pd.to_numeric(df_clean['messages'], errors='coerce')
df_100_msg = df_clean[df_clean['messages'] > 100]
print(df_100_msg.shape)

# 3.Visualisation
top10 = df_clean.sort_values(by='messages', ascending=False).head(10)
print(df_clean['participants'].head(10))  # Affiche les 10 premières valeurs


#print(top10)
# plt.figure(figsize=(10,6))
# sns.barplot(x='messages',y='title',data=top10)
# plt.title("Les 10 messages les plus actives.")
# plt.xlabel("Nombre de message")
# plt.ylabel("Titre de la discussion")

# plt.show()


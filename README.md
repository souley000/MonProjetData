# MonProjetData

Projet d'analyse de données avec Python, Jupyter Notebook et Power BI.  
Ce projet contient plusieurs fichiers pour effectuer le nettoyage, l'analyse et la visualisation de différents jeux de données (salaires, ventes, employés, formations, discussions, COVID-19, Jeux Olympiques).

## Contenu du projet

- `nettoyage_analyse.py` : Script Python pour le nettoyage et l'analyse descriptive des données salariales.  
  Inclut : chargement du CSV, gestion des valeurs manquantes et doublons, calcul des mesures de tendance centrale et de dispersion, export du jeu de données nettoyé.

- `analyse_ventes.py` : Script Python pour l'analyse exploratoire des données de ventes.  
  Inclut : vérification des doublons et valeurs manquantes, calcul de la moyenne et médiane des ventes, visualisation de la distribution des ventes.

- `nettoyage_employes.py` : Script Python pour le nettoyage et l'analyse des données des employés.  
  Inclut : gestion des valeurs manquantes et outliers, standardisation des noms et départements, ajout d’une colonne "Expérience", export des données nettoyées, et visualisations (histogramme, scatterplot, lineplot, barplot).

- `nettoyage_commandes.py` : Script Python pour le nettoyage et l'analyse des données de commandes.  
  Inclut : gestion des valeurs manquantes et doublons, standardisation des noms de clients et produits, recalcul des totaux des commandes, export des données nettoyées, et visualisations (barplot et histogramme).

- `analyse_formations.py` : Script Python pour l'analyse des données sur les formations.  
  Inclut : exploration des données (aperçu, informations générales, statistiques descriptives, valeurs manquantes) et visualisation du nombre de formations par thématique.

- `analyse_discussions.py` : Script Python pour le nettoyage et l'analyse des discussions du ministère de l’Intérieur.  
  Inclut : sélection et nettoyage des colonnes pertinentes, conversion de la colonne `messages` en numérique, filtrage des discussions avec plus de 100 messages, exploration des données, et préparation pour visualisation des 10 discussions les plus actives.

- `autre_script1.py` : Autres scripts Python utiles pour le projet (ajouter une description si nécessaire).  
- `autre_script2.ipynb` : Notebook Jupyter pour l'analyse exploratoire supplémentaire (ajouter une description si nécessaire).

- `covid19.pbix` : Rapport Power BI pour visualiser et analyser les données COVID-19.  
  Inclut : graphiques sur l’évolution des cas, répartition par pays et analyse des tendances.

- `JO_analysis.pbix` : Rapport Power BI pour l'analyse des Jeux Olympiques.  
  Inclut : visualisations sur les médailles, performances par pays et disciplines.

- `salary_cleaned.pbix` : Rapport Power BI basé sur le fichier Salary_Data nettoyé.  
  Inclut : analyses sur les salaires, expérience, âge et niveaux d’éducation.

## Instructions

1. **Python & Notebooks**  
   - Installer Python 3.x  
   - Installer les librairies nécessaires :  
     ```bash
     pip install pandas numpy matplotlib seaborn
     ```  
   - Exécuter les scripts `.py` dans un IDE (PyCharm, VSCode) ou terminal  
   - Ouvrir les notebooks `.ipynb` avec Jupyter Notebook ou JupyterLab

2. **Power BI**  
   - Ouvrir les fichiers `.pbix` avec Power BI Desktop  
   - Explorer les rapports interactifs et les visualisations  

## Auteur
Souleymane Diallo

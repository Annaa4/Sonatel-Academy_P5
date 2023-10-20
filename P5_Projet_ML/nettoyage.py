#1. Avec un script python, récupérer touts les fichiers qui sont dans le dossier et stocker les dans un fichier csv que vous nommez data .
import os
import pandas as pd

# Dossier contenant les fichiers CSV qu'on souhaite fusionner
dossier_source = "P5_Projet_ML/données_ventes"
# Chemin du fichier CSV de sortie
fichier_sortie = "P5_Projet_ML/data.csv"

# Liste pour stocker les dataframes des fichiers CSV
dataframes = []

# Parcourir tous les fichiers dans le dossier source
for fichier in os.listdir(dossier_source):
    if fichier.endswith(".csv"):
        chemin_fichier = os.path.join(dossier_source, fichier)
        # Lire chaque fichier CSV et le stocker dans la liste des dataframes
        df = pd.read_csv(chemin_fichier)
        dataframes.append(df)

# Fusionner les dataframes en un seul dataframe
df_fusion = pd.concat(dataframes, ignore_index=True)

# Écrire le dataframe fusionné dans un fichier CSV de sortie
df_fusion.to_csv(fichier_sortie, index=False)

print("Fusion terminée. Le fichier CSV de sortie est disponible à l'emplacement :", fichier_sortie)

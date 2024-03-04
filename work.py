import pandas as pd
import numpy as np
import matplotlib as plt
import os
import csv
os.chdir('/home/onyxia/Visualisation-Parcoursup/')
TEST2='/home/onyxia/Visualisation-Parcoursup/TEST.csv'
with open(TEST2, mode='r', encoding='utf-8') as fichier:
    lecteur_csv = csv.reader(fichier)
    en_tete = next(lecteur_csv)  # Pour sauter l'en-tête si votre fichier en contient une
    nombre_lignes = sum(1 for ligne in lecteur_csv)

print(f"Nombre d'observations : {nombre_lignes}")
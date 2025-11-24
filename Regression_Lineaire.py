#Prédire le prix d’une maison (modèle de régression linéaire)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#On crée un data set simple (plus surface augmente et plus le prix augmente
# Exemple simple : surface en m² et prix en euros
surface = np.array([30, 50, 70, 80, 120, 150, 200]).reshape(-1, 1)
prix = np.array([80000, 120000, 160000, 180000, 250000, 310000, 400000])


#On sépare les données en train et test
X_train, X_test, y_train, y_test = train_test_split(
    surface, prix, test_size=0.2, random_state=42)

#Création et entrainement du modèle
modele = LinearRegression()
modele.fit(X_train, y_train)


#evaluer le modèle
score = modele.score(X_test, y_test)
print("Précision du modèle :", score)


#faire une prédiction
surface_test = np.array([[1]])
prediction = modele.predict(surface_test)
print("Prix estimé pour 100 m² :", prediction[0])

#Visualiser le modèle
plt.scatter(surface, prix, label="Données réelles")
plt.plot(surface, modele.predict(surface), label="Modèle", linewidth=3)
plt.xlabel("Surface (m²)")
plt.ylabel("Prix (€)")
plt.legend()
plt.show()


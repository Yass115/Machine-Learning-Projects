# Explication du code sur a Régression Linèaire

### 🧠 **Vue d’ensemble : ce que fait ton programme**

Quand tu lances ton code :

1. Python charge les bibliothèques.
2. Il crée les données et les met en forme.
3. Il coupe ces données en deux morceaux (train + test).
4. Il crée un modèle vide (non entraîné).
5. Il **entraîne** le modèle → il découvre les meilleurs poids & biais.
6. Il **teste** le modèle sur des données inconnues.
7. Il **fait une prédiction** sur une nouvelle surface.
8. Il **dessine** les points et la droite apprise.

Maintenant, reprenons cela **en profondeur**, ligne par ligne.

---

### 🧱 **1) Importation des bibliothèques**

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
```

##### Ce qui se passe réellement :

* Python charge les modules installés dans ton environnement.
* `numpy` fournit des fonctions pour créer et manipuler des vecteurs/matrices.
* `scikit-learn` charge des classes de modèles ML.
* `matplotlib` prépare les outils pour afficher des graphiques.

👉 **Rôle important :**
Sans ces bibliothèques, Python ne peut pas faire de machine learning proprement.

---

### 🧱 **2) Création du dataset**

```python
surface = np.array([30, 50, 70, 80, 120, 150, 200]).reshape(-1, 1)
prix = np.array([80000, 120000, 160000, 180000, 250000, 310000, 400000])
```

##### Ce que fait Python :

1. **Créer un tableau numpy**

   * pas une liste, mais une structure optimisée en C (ultra rapide)
   * adaptée aux opérations mathématiques massives

2. `.reshape(-1, 1)`

   * transforme un tableau de forme `(7,)` → `(7, 1)`
   * scikit-learn exige toujours une **matrice** pour les entrées

##### Ce que ça implique :

Tu viens de créer **7 exemples**, chacun avec **1 seule caractéristique**.

---

### ✂️ **3) Séparer les données : train/test**

```python
X_train, X_test, y_train, y_test = train_test_split(
    surface, prix, test_size=0.2, random_state=42
)
```

##### Ce que fait Python :

1. Il prend tes 7 exemples.
2. Il mélange les données (pour éviter des biais).
3. Il en garde 20 % pour le test (≈ 1 ou 2 exemples).
4. Il sépare les entrées (`surface`) et sorties (`prix`).

👉 Résultat :

* `X_train` → données pour apprendre (`surface`)
* `y_train` → prix correspondants
* `X_test` → données jamais vues
* `y_test` → prix pour vérifier l'exactitude

##### Pourquoi ?

Pour détecter le **surapprentissage**.

---

### 🤖 **4) Création du modèle**

```python
modele = LinearRegression()
```

##### Ce que Python crée réellement :

Un objet qui contient :

* `coef_` (les poids) → pas encore définis
* `intercept_` (le biais) → pas encore défini
* un algorithme d’optimisation
* une structure interne pour gérer l’apprentissage

👉 Le modèle est **vide** : il ne sait rien.

---

### 🧠 **5) Entraînement du modèle**

```python
modele.fit(X_train, y_train)
```

##### C’est LA partie la plus importante.

Voici ce que Python fait réellement :

---

#### 🔥 **Étape 1 : Initialisation**

Scikit-learn commence avec :

* des poids **aléatoires**
* un biais **aléatoire**

Exemple :

```
w = 0.578
b = 1234
```

---

#### 🔥 **Étape 2 : Calcul des prédictions**

Il applique la formule :

```
prix_prédit = w × surface + b
```

pour **tous les exemples d'entraînement**.

---

#### 🔥 **Étape 3 : Calcul de l’erreur**

Il calcule une **fonction de coût**, souvent :

```
erreur = (prix_réel - prix_prédit)^2
```

Il additionne toutes les erreurs.

---

#### 🔥 **Étape 4 : Calcul du gradient**

Le modèle détermine :

* dans quelle direction ajuster les poids pour réduire l’erreur
  (augmenter w ? diminuer w ? augmenter b ? …)

Il calcule **la pente** de la montagne d’erreur.

---

#### 🔥 **Étape 5 : Ajustement des poids**

Python modifie légèrement :

* `w` (poids)
* `b` (biais)

dans la direction qui **diminue l’erreur**.

C’est la **descente de gradient**.

---

#### 🔥 **Étape 6 : Répétition**

Scikit-learn répète :

* calculer prédictions
* calculer erreur
* ajuster poids

…jusqu’à avoir les **meilleures valeurs possibles**.

👉 À la fin, `w` et `b` deviennent optimaux.

---

### 📘 **6) Évaluation du modèle**

```python
score = modele.score(X_test, y_test)
```

##### Ce que Python fait :

1. Il fait une prédiction pour `X_test`.
2. Il compare avec `y_test`.
3. Il calcule la métrique **R²** :

```
1.0 = parfait  
0.0 = aussi mauvais qu’un hasard  
< 0 = catastrophique  
```

👉 Ça te dit si le modèle **généralise**.

---

### 🔮 **7) Faire une prédiction**

```python
surface_test = np.array([[100]])
prediction = modele.predict(surface_test)
```

##### Ce que Python fait :

* il prend 100
* applique la formule apprise :

```
prix = w × 100 + b
```

* renvoie la valeur calculée

**Très important :**
Le modèle utilise maintenant **les vrais poids et biais appris**, pas ceux du début.

---

### 📊 **8) Visualisation**

```python
plt.scatter(surface, prix)
plt.plot(surface, modele.predict(surface))
plt.show()
```

##### Ce qui se passe :

1. `plt.scatter` trace les points réels.
2. `modele.predict(surface)` calcule la droite.
3. `plt.plot` trace la droite apprise.
4. `plt.show()` affiche la figure.

👉 Tu visualises :

* si la droite colle bien
* si les données sont linéaires
* l’efficacité de l'apprentissage

---

### 🎉 **Conclusion : ce qui se passe réellement**

Quand tu exécutes ton code :

✔ Python **charge les données**
✔ Les **prépare** sous forme de matrices
✔ Les **sépare** en entraînement et test
✔ Crée un modèle **vide**
✔ Le modèle **apprend** les meilleurs poids et biais
✔ Il **se teste** sur des données nouvelles
✔ Il peut maintenant **prédire**
✔ Et tu **visualises** tout ça

---

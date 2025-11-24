# Explications Mathématique de la régression Linéaire

---

# 🎯 **Objectif**

Comprendre précisément :

* comment scikit-learn trouve **w** (le coefficient)
* comment il trouve **b** (l’intercept)
* pourquoi le modèle trouve *la meilleure droite possible*
* comment les maths garantissent un résultat optimal

---

# 🧠 1) Le modèle que scikit-learn apprend

Pour une seule variable (ton cas) :

```
prix_prédit = w × surface + b
```

Scikit-learn doit trouver **le meilleur w** et **le meilleur b**
pour que la droite colle au mieux aux points.

---

# 🔥 2) Le principe mathématique utilisé : **Méthode des moindres carrés**

Scikit-Learn utilise une méthode mathématique très classique :

> **Minimiser la somme des erreurs au carré.**

Pour chaque point, l’erreur est :

```
erreur = prix_réel – prix_prédit
```

Mais au lieu de prendre directement l’erreur, on prend :

```
erreur²
```

Pourquoi ?

* toujours positif
* punit fort les grosses erreurs
* permet de trouver une solution exacte

La somme totale des erreurs carrées est :

```
E = ∑ (prix_réel – (w × surface + b))²
```

**Le but est de trouver w et b qui minimisent E.**

---

# 🧱 3) Comment trouver w et b qui minimisent l’erreur ?

C’est ici que les maths arrivent.

L’idée :

1. On calcule la dérivée de l’erreur **par rapport à w**
2. On la met = 0
3. On résout → on obtient w optimal

Puis on fait pareil pour **b**.

Scikit-learn utilise cette solution **exacte**, car c’est plus rapide et plus stable que la descente de gradient dans les petits modèles linéaires.

---

# 🧩 4) Formules finales (simplement expliquées)

### ✔️ Le poids w

Pour **une seule variable**, scikit-learn utilise :

[
w = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sum (x - \bar{x})^2}
]

Où :

* (x) = surface
* (y) = prix
* (\bar{x}) = moyenne des surfaces
* (\bar{y}) = moyenne des prix

👉 C’est exactement la formule de la **pente d’une droite de régression**.

**Interprétation :**

> w est proportionnel à la corrélation entre surface et prix.

---

### ✔️ Le biais b

Une fois w trouvé :

[
b = \bar{y} - w\bar{x}
]

**Interprétation :**

> b ajuste la droite pour qu’elle passe “au bon endroit”.

---

# 🔍 5) Intuition très simple derrière ces formules

👉 **w** mesure combien le prix change quand la surface change.

Si les surfaces augmentent et les prix augmentent → w positif
Si les surfaces augmentent mais les prix diminuent → w négatif
Si aucune relation → w ≈ 0

👉 **b** ajuste la droite verticalement pour qu’elle s’aligne sur les données.

---

# 🧠 6) Exemple concret avec ton dataset

Surfaces = `[30, 50, 70, 80, 120, 150, 200]`
Prix = `[80000, 120000, 160000, 180000, 250000, 310000, 400000]`

Scikit-learn va calculer :

1. la moyenne des surfaces
2. la moyenne des prix
3. les différences `(x - mean(x))`
4. les produits `(x - mean(x))(y - mean(y))`
5. w = somme(produits) / somme((x - mean(x))²)
6. b = mean(y) – w × mean(x)

Résultat :
Tu obtiendras un w ≈ **2000** et un b ≈ **20000** (approximativement).

---

# 🧨 7) Pour plusieurs caractéristiques ?

Si on avait :

* surface
* chambres
* âge
* etc.

Alors scikit-learn utilise la formule matricielle :

[
w = (X^T X)^{-1} X^T y
]

C’est la solution analytique des moindres carrés (méthode OLS).

Ne t’inquiète pas : scikit-learn fait les calculs automatiquement.
Tu n’as jamais besoin de le faire à la main.

---

# 🧩 8) Résumé clair

| Élément       | Comment scikit-learn le calcule ?             | Sens                                          |
| ------------- | --------------------------------------------- | --------------------------------------------- |
| **w (poids)** | Formule des moindres carrés                   | Importance de la surface                      |
| **b (biais)** | Calculé à partir de w et des moyennes         | Ajustement vertical                           |
| **Objectif**  | Minimiser la somme des erreurs au carré       | Trouver la meilleure droite                   |
| **Méthode**   | Solution analytique sans descente de gradient | Plus rapide et exact pour les modèles simples |

---

# 🎉 Tu as compris mathématiquement comment scikit-learn apprend !

C’est exactement ce qui se passe dans tous les modèles linéaires.

---

Projet 2 — Détecter des attaques réseau avec le Machine Learning
Nom / Prénom : FALL Madiagne
Un IDS doit décider, pour chaque flux réseau, s'il est normal (0) ou une attaque (1). Ce projet entraîne et compare plusieurs modèles de classification sur 3000 flux (≈ 28 % d'attaques).
Lancer le projet
1.	Exploration : 3000 lignes, 90 valeurs manquantes (colonne duration), 27,8 % d'attaques. Les classes sont déséquilibrées, donc on utilise le F1 de la classe attaque et pas seulement l'accuracy.
2.	Prétraitement (dans un Pipeline) : imputation par la médiane, mise à l'échelle (StandardScaler) des variables numériques, encodage one-hot de protocol.
3.	Validation : 80 % entraînement / 20 % validation, découpage stratifié (random_state=42). Les trois modèles utilisent class_weight="balanced".
4.	Modèle final : le meilleur modèle est ré-entraîné sur toutes les données et enregistré dans models/model.joblib.
Résultats
Nom / Prénom : FALL Madiagne 
Mesures sur le jeu de validation (classe « attaque ») :
Modèle	F1 (attaque)	Rappel (attaque)	Précision (attaque)
Régression logistique	0,920	0,898	0,943
Arbre de décision (profondeur 6)	0,953	0,964	0,942
Forêt aléatoire (300 arbres)	0,976	0,976	0,976
Modèle retenu et pourquoi :
La forêt aléatoire est retenue : elle a le meilleur F1 sur la classe attaque et le meilleur rappel, ce qui compte le plus pour un IDS. Elle donne aussi un F1 de 0,958 en validation croisée à 5 plis, ce qui indique que le résultat ne dépend pas d'un découpage chanceux. La régression logistique, modèle linéaire, est la moins bonne : la frontière entre flux normaux et attaques n'est pas linéaire dans les données. Un arbre seul s'en sort mieux, mais une forêt, qui moyenne beaucoup d'arbres, généralise mieux.
Analyse des erreurs (faux négatifs / faux positifs) :
Avec la forêt aléatoire sur les 600 flux de validation :
•	Faux négatifs : 2 attaques ratées sur 167. C'est le pire cas en sécurité : une attaque non détectée ne déclenche aucune alerte, et l'attaquant peut scanner, forcer un mot de passe ou saturer un service sans être arrêté.
•	Faux positifs : 2 fausses alertes sur 433 flux normaux. Elles coûtent du temps aux analystes, mais elles ne laissent entrer personne.
Dans un IDS, on préfère donc quelques fausses alertes de plus plutôt qu'une attaque manquée : on cherche d'abord un rappel élevé, puis la meilleure précision possible. 


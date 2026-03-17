# 📧 Système de Classification d'Emails (IA)

Ce projet est une solution complète de **Machine Learning** permettant de classer automatiquement des emails en trois catégories : **Important**, **Normal**, ou **Spam**.

## 🏗️ Architecture du Projet
L'application suit une structure de déploiement moderne :
1. **Modèle ML** : Entraîné avec Scikit-Learn (Algorithme Naive Bayes).
2. **Prétraitement** : Transformation du texte en vecteurs numériques via TF-IDF.
3. **API Web** : Créée avec Flask pour exposer le modèle sur Internet.
4. **Hébergement Cloud** : Déployé sur **Render** (PaaS).
5. **Test Client** : Vérification de l'API depuis une instance **AWS EC2**.

## 📁 Liste des Fichiers
* `app.py` : Le code Python contenant l'entraînement du modèle et les routes de l'API Flask.
* `emails_dataset.csv` : Le jeu de données utilisé pour l'apprentissage supervisé.
* `requirements.txt` : Liste des bibliothèques nécessaires (Flask, Pandas, Scikit-Learn, Gunicorn).
* `README.md` : Documentation du projet.

## 🚀 Utilisation de l'API

### URL de base
`https://test1-uzwj.onrender.com`

### Endpoint de Prédiction
**Route** : `/predict`  
**Méthode** : `POST`  
**Format des données** : `JSON`

### Exemple de test (Commande cURL pour AWS EC2)
Pour tester l'IA depuis un terminal distant, utilisez la commande suivante :

```bash
curl -X POST [https://test1-uzwj.onrender.com/predict](https://test1-uzwj.onrender.com/predict) \
     -H "Content-Type: application/json" \
     -d '{"email": "URGENT : Merci de valider le rapport de réunion avant ce soir"}'

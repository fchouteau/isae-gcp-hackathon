# Team Packaging of ML Model

## Objectif

Packager un modèle de machine learning derrière une webapplication pour pouvoir la déployer sur le web et servir des prédictions à des utilisateurs

## Déroulement

- Transformer un notebook de prédiction en “WebApp” en remplissant `app.stub.py`
- Tester sa webapp localement
- Packager l'application sous forme d'une image docker
- Tester son image docker localement
- Uploader le docker sur Google Container Registry

## Détails

### Tester son application

Dans un terminal, vous pouvez faire `uvicon app:app --reload` pour lancer la webbapp FastAPI qui sert le modèle,

Ensuite vous pouvez lancer le notebook tests pour vérifier que tout marche

Ensuite vous pouvez passer à l'étape suivante

## Liens Utiles

https://fastapi.tiangolo.com/
https://requests.readthedocs.io/en/master/
https://testdriven.io/blog/fastapi-streamlit/

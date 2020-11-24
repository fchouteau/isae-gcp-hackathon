# Team Companion UX webapp

## Objectif

Créer une application "compagnon" qui permet de faire des requêtes à un modèle de façon ergonomique et de visualiser les résultats

## Déroulement

- Remplir `app.stub.py`, le renommer en `app.py` en remplissant les bons champs (s'aider des notebooks dans `app/`) et en créant des jolies visualisations
- Tester sa webapp localement (il y a un mode test)
- Packager l'application sous forme d'une image docker
- Tester son image docker localement
- Uploader le docker sur Google Container Registry

## Détails

### Tester son application localement

- installer les dépendances (`pip install -r requirements.txt`)
- `streamlit run app.py`, qui créée l'application interactive sur le port 8501 de la machine (localhost:8501)

### Construire le docker

```bash
docker build -t eu.gcr.io/{your registry}/{your app name}:{your version} -f Dockerfile . 
```

### Tester le docker

Au lieu de faire `uvicorn`, vous pouvez lancer le docker localement et aller sur localhost:8501 pour tester le docker

```bash
docker run --rm -p 8501:8501 eu.gcr.io/{your registry}/{your app name}:{your version}
```

## Liens Utiles

https://docs.streamlit.io/en/stable/getting_started.html

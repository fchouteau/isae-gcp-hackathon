# Team Packaging of ML Model

## Objectif

Packager un modèle de machine learning derrière une webapplication pour pouvoir la déployer sur le web et servir des prédictions à des utilisateurs

Le modèle: Un détecteur d'objets sur des photographies "standard" supposé marcher en temps réel, qui sort des "bounding boxes" autour des objets détecté dans des images

![image](cats_yolo.png)
 
Le papier vaut la lecture

https://pjreddie.com/media/files/papers/YOLOv3.pdf

On récupère la version disponible sur torchhub https://pytorch.org/hub/ultralytics_yolov5/ qui correspond à ceci https://github.com/ultralytics/yolov5

Voici une petite explication de l'historique https://medium.com/towards-artificial-intelligence/yolo-v5-is-here-custom-object-detection-tutorial-with-yolo-v5-12666ee1774e

On se propose ici de wrapper 3 versions du modèle (S,M,L) qui sont 3 versions +/- complexes du modèle YOLO-V5, afin de pouvoir comparer les performances et les résultats

![models](https://user-images.githubusercontent.com/26833433/97808084-edfcb100-1c64-11eb-83eb-ffed43a0859f.png)

## Déroulement

- Transformer un notebook de prédiction en “WebApp” en remplissant `app.stub.py` et en le renommant en `app.py`
- Tester sa webapp localement
- Packager l'application sous forme d'une image docker
- Tester son image docker localement
- Uploader le docker sur Google Container Registry

## Détails

### Tester son application

Dans un terminal, vous pouvez faire `uvicorn app:app --reload` pour lancer la webbapp FastAPI qui sert le modèle,

Ensuite vous pouvez lancer le notebook tests pour vérifier que tout marche

Ensuite vous pouvez passer à l'étape suivante

### Construire le docker

```bash
docker build -t eu.gcr.io/{your registry}/{your app name}:{your version} -f Dockerfile . 
```

### Tester le docker

Au lieu de faire `uvicorn`, vous pouvez lancer le docker localement et le tester de la même façon avec le notebook

```bash
docker run --rm -p 8000:8000 eu.gcr.io/{your registry}/{your app name}:{your version}
```

## Liens Utiles

https://fastapi.tiangolo.com/
https://requests.readthedocs.io/en/master/
https://testdriven.io/blog/fastapi-streamlit/

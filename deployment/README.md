# Team Déploiement

## Objectif

Déployer de façon "scalable" sur google cloud platform les deux applications, s'assurer qu'elles peuvent communiquer

## Déroulement

- Essayer de déployer deux “dummy applications” en attendant
- Récupérer les deux images dockers de fastapi et streamlit
- Tester localement (via docker compose) les deux images docker et vérifier qu'elles communiquent bien
- Remplacer les applications “dummy” par les vraies applications sur GCP
- Exposer aux utilisateurs en envoyant l'URL de l'application compagnon (et celle du modèle)

## Détails

## Liens Utiles

Docker Compose (tests locaux)
https://docs.docker.com/compose/

Google Cloud Run (serverless managed) - Easier to deploy, harder to control
https://cloud.google.com/run/docs/quickstarts/prebuilt-deploy

Google Kubernetes Engine (managed kubernetes)
https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app

https://medium.com/velotio-perspectives/a-practical-guide-to-deploying-multi-tier-applications-on-google-container-engine-gke-5f476805595d

https://cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps

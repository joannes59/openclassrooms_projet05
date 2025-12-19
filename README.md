---
title: Openclassrooms Projets05
emoji: 🏆
colorFrom: green
colorTo: blue
sdk: docker
pinned: false
short_description: 'Formation ML deploy docker '
---

# Déployez votre modèle de Machine Learning

## 🧠 Description
Exercice de formation OpenClassRoom.

Projet de Machine Learning incluant un modèle RandomForest, exposé via une API et déployé sur HuggingFace.

Rendre un modèle de machine learning utilisable en production tout en respectant les meilleures pratiques de l'ingénierie logicielle.
Démonstration d'un Proof of Concept (POC)


## 🚀 Installation

```bash

git clone https://github.com/joannes59/openclassrooms_projet05.git

cd openclassrooms_projet05
pip install -r requirements.txt



```

## ▶️ Utilisation

Dans le cadre d'une utilisation sur la plate forme Hugging, le port exposé est définit sur 7860.

```bash
uvicorn app.main:app --host 0.0.0.0 --port 7860

```

## ▶️ Docker

```bash

docker build -t docker_projet05 .
docker run -p 7860:7860 docker_projet05



```

## 📁 Structure du projet

Voir l'arborescence dans la documentation.

## 🧪 Tests
```bash
pytest
```



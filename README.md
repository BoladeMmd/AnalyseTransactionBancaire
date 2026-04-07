# 💳 Real-Time Banking Transactions Monitoring

## 📌 Description
Ce projet consiste à concevoir et implémenter une plateforme de surveillance des transactions bancaires en temps réel, en s’appuyant sur une architecture orientée streaming. L’objectif principal est de simuler, traiter et analyser des flux de transactions afin de détecter des comportements suspects et fournir une visualisation dynamique des données.

Le système repose sur Apache Kafka pour la gestion des flux de données, permettant de transmettre en continu les transactions générées par un producteur vers un consommateur. Ce dernier applique des règles simples de détection de fraude avant de stocker les données dans une base PostgreSQL pour un usage analytique et historique.

Les données sont ensuite exploitées dans Power BI, où plusieurs tableaux de bord interactifs ont été conçus pour suivre en temps quasi réel :

le volume des transactions,
les montants échangés,
la répartition par type,
et les transactions frauduleuses.

Ce projet met en œuvre une architecture complète de traitement de données, allant de l’ingestion à la visualisation, en passant par le stockage et l’analyse.

## 🎯 Objectifs

-Simuler un flux de transactions bancaires en temps réel

-Mettre en place un pipeline de traitement avec Kafka

-Implémenter une logique simple de détection de fraude

-Stocker les données dans une base relationnelle

-Construire des dashboards interactifs pour l’analyse


## 🧱 Architecture
Producer → Kafka → Consumer → PostgreSQL → Power BI


-**Producer** : Génère des données de transaction  
- **Kafka** : diffuse les données en temps réel  
- **Consumer** : traite les données et détecte les fraudes potentielles   
- **PostgreSQL** : stocke les données historiques  
- **Power BI** : visualise les données (en temps réel et analyses)

  
## ⚙️ Technologies
- Apache Kafka (via Docker)
- Python (Kafka Producer & Consumer)
- PostgreSQL 
- Power BI 




## DASHBOADS
**1ere Page**

La premiere page resume les transactions de facon general 


## ▶️ Lancer le projet

```bash
docker-compose up -d
python3 producer/producer.py
python3 consumer/consumer.py

# 💳 Real-Time Banking Transactions Monitoring

## 📌 Description
Ce projet consiste à concevoir et implémenter une plateforme de surveillance des transactions bancaires en temps réel, en s’appuyant sur une architecture orientée streaming. L’objectif principal est de simuler, traiter et analyser des flux de transactions afin de détecter des comportements suspects et fournir une visualisation dynamique des données.

Le système repose sur Apache Kafka pour la gestion des flux de données, permettant de transmettre en continu les transactions générées par un producteur vers un consommateur. Ce dernier applique des règles simples de détection de fraude avant de stocker les données dans une base PostgreSQL pour un usage analytique et historique.

Les données sont ensuite exploitées dans Power BI, où plusieurs tableaux de bord interactifs ont été conçus pour suivre en temps quasi réel les transactions bancaires.


Ce projet met en œuvre une architecture complète de traitement de données, allant de l’ingestion à la visualisation, en passant par le stockage et l’analyse.

## 🎯 Objectifs

-Simuler un flux de transactions bancaires en temps réel

-Mettre en place un pipeline de traitement avec Kafka

-Implémenter une logique simple de détection de fraude

-Stocker les données dans une base relationnelle

-Construire des dashboards interactifs pour l’analyse


## 🧱 Architecture
Producer → Kafka → Consumer → PostgreSQL → Power BI


- **Producer** : Génère des données de transaction  
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

<img width="633" height="341" alt="image" src="https://github.com/user-attachments/assets/adb57b8f-3529-4d22-aec6-b15cec423ce7" />


**📊 Interprétation du Dashboard 1 : Vue globale des transactions**

Ce tableau de bord offre une vue d’ensemble de l’activité des transactions bancaires en temps réel.

- **Flux de transactions dans le temps**

- **Transactions par région**

- **Nombre de transactions par type**

- **Montant des transactions par heure**

**🎯 Conclusion**

Ce dashboard permet d’identifier rapidement :

- **les périodes d’activité élevée**

- **les zones géographiques dominantes**

- **les types de transactions les plus utilisés**


Il constitue une base essentielle pour la surveillance et la détection d’anomalies dans les flux financiers.





## ▶️ Lancer le projet

```bash
docker-compose up -d
python3 producer/producer.py
python3 consumer/consumer.py

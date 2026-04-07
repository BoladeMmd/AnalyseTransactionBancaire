# 💳 Real-Time Banking Transactions Monitoring

## 📌 Description
Ce projet permet de surveiller des transactions bancaires en temps réel avec Apache Kafka.

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

## 🚀 Fonctionnalités
- Génération de transactions
- Détection de fraude
- Stockage des données
- Visualisation en temps réel


## DASHBOADS
**1ere Page**
La premiere page resume les transactions de facon general 


## ▶️ Lancer le projet

```bash
docker-compose up -d
python3 producer/producer.py
python3 consumer/consumer.py

# 💳 Real-Time Banking Transactions Monitoring

## 📌 Description
Ce projet permet de surveiller des transactions bancaires en temps réel avec Apache Kafka.

## 🧱 Architecture
Producer → Kafka → Consumer → PostgreSQL → Power BI

## ⚙️ Technologies
- Apache Kafka
- Python
- PostgreSQL
- Docker
- Power BI

## 🚀 Fonctionnalités
- Génération de transactions
- Détection de fraude
- Stockage des données
- Visualisation en temps réel

## ▶️ Lancer le projet

```bash
docker-compose up -d
python3 producer/producer.py
python3 consumer/consumer.py

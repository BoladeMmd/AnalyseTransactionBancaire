import random
from datetime import datetime

def generate_transaction(normal=True):
    """
    Génère une transaction bancaire fictive.
    
    Args:
        normal (bool): Si True, transaction normale, sinon transaction suspecte.
    
    Returns:
        dict: transaction
    """
    transaction = {
        "user_id": f"user_{random.randint(1, 100)}",
        "amount": round(random.uniform(10, 20000), 2),
        "location": random.choice(["Dakar", "Paris", "New York", "London"]),
        "transaction_type": random.choice(["payment", "withdrawal", "transfer"]),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Si transaction suspecte, augmenter le montant ou mettre un comportement atypique
    if not normal:
        transaction["amount"] = round(random.uniform(5000, 50000), 2)  # gros montant suspect
        transaction["location"] = random.choice(["Moscow", "Beijing", "Dubai"])  # localisation atypique
        transaction["transaction_type"] = random.choice(["transfer", "withdrawal"])  # type plus critique

    return transaction

# Test rapide
if __name__ == "__main__":
    print("5 transactions normales :")
    for _ in range(5):
        print(generate_transaction(normal=True))
    
    print("\n5 transactions suspectes :")
    for _ in range(5):
        print(generate_transaction(normal=False))

import csv
import json
import random

# A subset of SQL Injection payloads from the SQL Injection Cheat Sheet (example data)
sql_injections_from_cheatsheet = [
    "' OR '1'='1",
    "' OR 'x'='x",
    "' UNION SELECT 1, 2, 3 --",
    "'; DROP TABLE users; --",
    "' AND 1=2 --",
    "1 OR 1=1 --",
    "' HAVING 1=1 --",
    "' OR EXISTS(SELECT * FROM users) --",
    "'; UPDATE users SET password='hacked' --",
    "SELECT * FROM users WHERE id=1 OR 1=1"
]

# List of normal, legitimate SQL queries (Example data)
legitimate_queries = [
    "SELECT * FROM users WHERE username='admin' AND password='password';",
    "SELECT name, age FROM employees WHERE department='HR';",
    "UPDATE users SET password='newpassword' WHERE username='john';",
    "SELECT email FROM customers WHERE id='123';",
    "DELETE FROM orders WHERE order_id=1001;",
    "INSERT INTO orders (user_id, product_id, quantity) VALUES (1, 101, 2);",
    "SELECT COUNT(*) FROM products WHERE price > 100;",
    "SELECT id, username FROM users WHERE status='active';"
]

# Dataset container (List of dictionaries)
dataset = []

# Add SQL injection examples from the Cheat Sheet, label as 1 (malicious)
for payload in sql_injections_from_cheatsheet:
    dataset.append({"query": payload, "label": 1})

# Add legitimate queries, label as 0 (legitimate)
for query in legitimate_queries:
    dataset.append({"query": query, "label": 0})

# Shuffle the dataset (mix legitimate and malicious queries)
random.shuffle(dataset)

# Option 1: Save the dataset in JSON format
def save_to_json(filename="sql_injection_dataset.json"):
    with open(filename, 'w') as json_file:
        json.dump(dataset, json_file, indent=4)
    print(f"Dataset saved to {filename}")

# Option 2: Save the dataset in CSV format
def save_to_csv(filename="sql_injection_dataset.csv"):
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['query', 'label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for data in dataset:
            writer.writerow(data)
    print(f"Dataset saved to {filename}")

# Choose which format to save the dataset in (JSON or CSV)
if __name__ == "__main__":
    # Uncomment the desired option (JSON or CSV)
    save_to_json("sql_injection_dataset.json")  # Option 1: JSON Format
    save_to_csv("sql_injection_dataset.csv")  # Option 2: CSV Format

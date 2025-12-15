import pandas as pd
import numpy as np

# --- 1. Create the 'Orders' Dataframe (The Left Table) ---
# Messy aspects: 
# - 'user_id' is a STRING
# - 'product' has mixed capitalization and whitespace
orders_data = {
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006],
    'user_id': ['1', '2', '  2', '3', '99', '5'],  # Note: Strings, whitespace ('  2'), and a missing user ('99')
    'product': ['Laptop', 'mouse ', 'Mouse', 'Keyboard', 'Monitor', 'Laptop '], 
    'amount': [1200, 25, 25, 75, 300, 1200]
}
df_orders = pd.DataFrame(orders_data)
orders_csv = df_orders.to_csv('orders_data.csv', index=False)

# --- 2. Create the 'Users' Dataframe (The Right Table) ---
# Messy aspects:
# - 'id' is an INTEGER (will conflict with 'user_id' string)
# - DUPLICATE ID: User 2 appears twice with different emails
users_data = {
    'id': [1, 2, 2, 3, 4, 5], 
    'name': ['Alice', 'Bob', 'Bobby', 'Charlie', 'David', 'Eve'],
    'email': ['alice@example.com', 'bob@work.com', 'bob@home.com', 'charlie@example.com', 'david@example.com', 'eve@example.com']
}
df_users = pd.DataFrame(users_data)
users_csv = df_users.to_csv('users_data.csv', index=False)

print("--- df_orders ---")
print(df_orders)
print("\n--- df_users ---")
print(df_users)
import pandas as pd
import numpy as np

#Load the datasets
df_orders = pd.read_csv('E:/PYTHON_PROJECTS/Data Analysis Practice/messy_merger/data/raw/orders_data.csv')
df_users = pd.read_csv('E:/PYTHON_PROJECTS/Data Analysis Practice/messy_merger/data/raw/users_data.csv')

#Display the first and last few rows of each DataFrame

print('--- df_orders Head ---')
print(df_orders.head())
print('--- df_orders Tail ---')
print(df_orders.tail())

print('--- df_users Head ---')
print(df_users.head())
print('--- df_users Tail ---')
print(df_users.tail())

# Display column names so we can plan cleaning steps
print('--- df_orders Columns ---')
print(df_orders.columns)       

print('--- df_users Columns ---')   
print(df_users.columns)

# Display Null or missing data information
print('--- df_orders Info ---') 
print(df_orders.info())

print('--- df_users Info ---')  
print(df_users.info())

# Change datatypoe of 'user_id'in df_orders and 'id' in df_users to string for consistency
df_orders['user_id'] = df_orders['user_id'].astype(str).str.strip()
df_users['id'] = df_users['id'].astype(str).str.strip()

# Merge the DataFrames on the cleaned 'user_id' and 'id' columns
users_orders_merged = pd.merge(df_orders, df_users, how='left', left_on='user_id', right_on='id')
print('--- Merged DataFrame ---')
print(users_orders_merged.head())
# Drop the redundant 'id' column after merge
users_orders_merged = users_orders_merged.drop(columns=['id'])
print('--- Merged DataFrame after dropping redundant id column ---')
print(users_orders_merged.head())

# Clean the product names by stripping whitspaces and standardizing capitalization
users_orders_merged['product'] = users_orders_merged['product'].str.strip().str.lower()
print('--- Cleaned product names ---')
print(users_orders_merged[['product']])  # Display unique product names after cleaning

# Drop duplicate rows based on order_id to ensure each order is unique
users_orders_merged = users_orders_merged.drop_duplicates(subset=['order_id'])
# Reset index after dropping duplicates
users_orders_merged = users_orders_merged.reset_index(drop=True)
print('--- DataFrame after dropping duplicates ---')
print(users_orders_merged)
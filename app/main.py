import pandas as pd
from pathlib import Path

PARENT_DIR = Path.cwd().parent

df=pd.read_csv(str(PARENT_DIR) + '/csv_files/amazon-orders.csv')
df=df.fillna(0)
df["Item Total"] = df["Item Total"].str.replace('$','').astype(float)
first_five_rows=df.head()
columns_and_rows=df.shape

item_total_column=df["Item Total"]
spend_total=item_total_column.sum()

print('this is how much I spent on amazon: $', spend_total)

spend_average_per_order=item_total_column.mean()

print('this is my avg. spend on amazon: $', spend_average_per_order)

median_spend_per_order=item_total_column.median()

print('this is my median spend on amazon: $', median_spend_per_order)

max_spend_per_order=item_total_column.max()

print('this is my max spend on amazon: $', max_spend_per_order)

min_spend_per_order=item_total_column.min()

print('this is my min spend on amazon: $', min_spend_per_order)







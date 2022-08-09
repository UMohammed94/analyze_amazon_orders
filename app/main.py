import pandas as pd
from pathlib import Path

PARENT_DIR = Path.cwd().parent

df=pd.read_csv(str(PARENT_DIR) + '/csv_files/amazon-orders.csv')
df=df.fillna(0)
df["Item Total"] = df["Item Total"].str.replace('$','').astype(float)
first_five_rows=df.head()
columns_and_rows=df.shape

total_charged=df["Item Total"].sum()

print('This is my df: ', '\n\n\n',first_five_rows)
print('this is how much I spent on amazon: $', total_charged)






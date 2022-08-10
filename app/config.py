import pandas as pd
from pathlib import Path

PARENT_DIR = Path.cwd().parent
CSV='/csv_files/amazon-orders.csv'

df=pd.read_csv(str(PARENT_DIR) + CSV)
df=df.fillna(0)

ORDER_TOTAL=df["Item Total"].str.replace('$','',regex=True).astype(float)
ORDER_TAX_CHARGED=df["Item Subtotal Tax"].str.replace('$','',regex=True).astype(float)

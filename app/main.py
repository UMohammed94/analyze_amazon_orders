import pandas as pd
from pathlib import Path
from config import df

order_total=df["Item Total"].str.replace('$','',regex=True).astype(float)

spend_total=order_total.sum()

print('this is how much I spent on amazon: $', spend_total)

spend_average_per_order=order_total.mean()

print('this is my avg. spend on amazon: $', spend_average_per_order)

median_spend_per_order=order_total.median()

print('this is my median spend on amazon: $', median_spend_per_order)

max_spend_per_order=order_total.max()

print('this is my max spend on amazon: $', max_spend_per_order)

min_spend_per_order=order_total.min()

print('this is my min spend on amazon: $', min_spend_per_order)

order_tax_charged=df["Item Subtotal Tax"].str.replace('$','',regex=True).astype(float)

total_tax_charged=order_tax_charged.sum()

print(total_tax_charged)

effective_sales_tax_rate=((total_tax_charged/spend_total)*100)

print('this is my effective sales tax rate: %',effective_sales_tax_rate)





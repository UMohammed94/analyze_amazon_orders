import pandas as pd
from config import df, ORDER_TOTAL, ORDER_TAX_CHARGED

def yourSpendTotal(order):
    spend_total=order.sum()
    print('this is how much I spent on amazon: $', spend_total)
    
    return spend_total

def yourAveragePerOrder(order):
    spend_average_per_order=order.mean()
    print('this is my avg. spend on amazon: $', spend_average_per_order)

    return spend_average_per_order

def yourMedianPerOrder(order):
    median_spend_per_order=order.median()
    print('this is my median spend on amazon: $', median_spend_per_order)

    return median_spend_per_order

def yourMaxPerOrder(order):
    max_spend_per_order=order.max()
    print('this is my median spend on amazon: $', max_spend_per_order)

    return max_spend_per_order

def yourMinPerOrder(order):
    min_spend_per_order=order.max()
    print('this is my min spend on amazon: $', min_spend_per_order)

    return min_spend_per_order

def yourTotalTaxCharged(tax_charged):
    total_tax_charged=tax_charged.sum()
    print('this is total tax charged on amazon: $', total_tax_charged)

    return total_tax_charged

def yourEffectiveSalesTaxRate():
    spend_total=ORDER_TOTAL.sum()
    total_tax_charged=ORDER_TAX_CHARGED.sum
    effective_sales_tax_rate=((total_tax_charged/spend_total)*100)
    print('this is my effective sales tax rate: %',effective_sales_tax_rate)

    return effective_sales_tax_rate


# todo create a function to run all other functions
# todo what time of day do I buy more
# todo how long do I keep something in my cart before I purchase
# todo what day of the week am I more likely to purchase
# todo essential purchase vs none essential purchase - look at your most popular category






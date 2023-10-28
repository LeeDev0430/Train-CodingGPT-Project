import pandas as pd

df = pd.read_csv("input files/BoeingOrdersandDeliveries.csv")

orders_by_customer = df.groupby("Customer Name").size()
max_orders_by_customer = orders_by_customer.max()
customers_with_max_orders = orders_by_customer[
    orders_by_customer == max_orders_by_customer
].index.tolist()

print(
    f"The customers with the most orders are {', '.join(customers_with_max_orders)}, with {max_orders_by_customer} orders each."
)
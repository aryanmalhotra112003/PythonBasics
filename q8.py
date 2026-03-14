import json
import csv

with open("sales.json", "r") as f:
    data = json.load(f)

rows = []

for order in data.get("orders", []):

    order_id = order.get("order_id", "")
    customer_name = order.get("customer", {}).get("name", "")
    shipping_address = order.get("shipping_address", "")
    country_code = "US"   

    items = order.get("items", [])

    for item in items:

        product_name = item.get("name", "")
        price = item.get("price", 0)
        quantity = item.get("quantity", 0)

        total_value = price * quantity

        discount = 0
        if total_value > 100:
            discount = total_value * 0.10

        shipping_cost = quantity * 5

        final_total = total_value - discount + shipping_cost

        rows.append([
            order_id,
            customer_name,
            product_name,
            price,
            quantity,
            round(total_value,2),
            round(discount,2),
            shipping_cost,
            round(final_total,2),
            shipping_address,
            country_code
        ])

rows.sort(key=lambda x: x[8], reverse=True)

header = [
    "Order ID",
    "Customer Name",
    "Product Name",
    "Product Price",
    "Quantity Purchased",
    "Total Value",
    "Discount",
    "Shipping Cost",
    "Final Total",
    "Shipping Address",
    "Country Code"
]

with open("sales_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

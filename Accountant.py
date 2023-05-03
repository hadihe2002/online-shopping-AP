import csv

orders = [{"quantity": 10, "order_num": 10, "fee": 50,
           "delivery_price": 40, "tax": 50*(9/100)}]


def save_order(quantity, order_num, fee, delivery_price):
    orders.append({"quantity": quantity, "order_num": order_num, "fee": fee,
                  "delivery_price": delivery_price, "tax": fee*(9/100)})


def get_orders(type):
    if type == "text":
        with open('orders.txt', 'w') as f:
            for order in orders:
                f.write(', '.join(order))
                f.write('\n')

    if type == "csv":
        with open('names.csv', 'w', newline='') as csvfile:
            fieldnames = ["quantity", "order_num", "fee", "delivery_price", "tax"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for order in orders:
                writer.writerow(order)
                
import csv
import json

orders = []

try:
    file = open("orders.json", 'r')
    orders = json.loads((json.load(file)))
    file.close()
except:
    orders = []


def save_order(quantity, order_num, fee, delivery_price):
    orders.append({"quantity": quantity, "order_num": order_num, "fee": fee,
                  "delivery_price": delivery_price, "tax": fee*(9/100)})

    file = open("orders.json", "w")
    json.dump(orders, file)
    file.close()


def get_orders(type):
    if type == "text":
        f = open('orders.txt', 'w')
        fieldnames = ["quantity", "order_num",
                      "fee", "delivery_price", "tax"]
        f.write(', '.join(fieldnames))
        f.write('\n')
        for order in orders:
            f.write(', '.join(list(map(str, order.values()))))
            f.write('\n')
        f.close()

    if type == "csv":
        with open('orders.csv', 'w', newline='') as csvfile:
            fieldnames = ["quantity", "order_num",
                          "fee", "delivery_price", "tax"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for order in orders:
                writer.writerow(order)

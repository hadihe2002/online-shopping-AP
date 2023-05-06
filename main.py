import Storage
import Order


while True:
    n = input(
        "Do You Want Enter Admin (A) Or Client Side (C) Or You Want To End The Program (E): ")
    if n == "C":
        Order.run_cli()
    elif n == "A":
        Storage.run_cli()
    elif n == "E":
        break

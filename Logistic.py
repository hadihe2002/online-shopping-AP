delivery_times = {"morning": 0, "noon": 0, "afternoon": 0}
counties = {1: "Tehran", 2: "Isfahan", 3: "Tabriz"}
Tehran = {1: "Tehran1", 2: "Tehran2"}
Isfahan = {1: "Isfahan1", 2: "Isfahan2"}
Tabriz = {1: "Tabriz1", 2: "Tabriz2"}


def get_postal_code():
    while True:
        postal_code = input("Enter Your Postal Code: ")
        if len(postal_code) != 10:
            print("Postal Code Should Have 10 Digits. Try Again!")
        break
    return postal_code


def get_delivery_times():
    free_times = []
    for time, order in delivery_times.items():
        if time == "morning":
            free_times.append(time)
        if time == "noon" and order < 3:
            free_times.append(time)
        if time == "afternoon" and order < 3:
            free_times.append(time)
    return free_times


def allocate_delivery():
    results = {"county": 0, "city": 0, "delivery_type": ""}
    county = int(input("Which County Are You In (1: Tehran, 2: Isfahan, 3: Tabriz): "))
    if county == 1:
        city = input("Which City Are You In: (1: Tehran1, 2: Tehran2)")
    if county == 2:
        city = input("Which City Are You In: (1: Isfahan1, 2: Isfahan2)")
    if county == 3:
        city = input("Which City Are You In: (1: Tabriz1, 2: Tabriz2)")

    if county == 1:
        results['delivery_type'] = "BikeDelivery"
    else:
        results['delivery_type'] = "Post"

    results['county'] = county
    results['city'] = city
    return results


def update_delivery_times(time):
    delivery_times[time] += 1
    return delivery_times


def estimate_delivery_time():
    results = {"time": "", "estimate": 0}
    free_delivery_times = ", ".join(get_delivery_times())
    estimate = 0


    while True:
        time = input(f'Enter Time For Delivery({free_delivery_times}): ')
        if time in get_delivery_times():
            delivery_times = update_delivery_times(time)
            break
        else: 
            print("Please Enter Time Between Free Delivery Times: ")

    number = delivery_times[time] // 6

    if time == "morning":
        estimate = 6 + number
    if time == "noon":
        estimate = 12 + number
    if time == "afternoon":
        estimate = 18 + number

    results['estimate'] = estimate
    results['time'] = time

    return results


def allocate_delivery_price(time, delivery):
    if time == "morning":
        if delivery == "BikeDelivery":
            price = 30
        if delivery == "Post":
            price = 20

    if time == "noon":
        if delivery == "BikeDelivery":
            price = 60
        if delivery == "Post":
            price = 40

    if time == "afternoon":
        if delivery == "BikeDelivery":
            price = 100
        if delivery == "Post":
            price = 50

    return price
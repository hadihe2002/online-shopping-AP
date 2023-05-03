delivery_times = {"morning": 0, "noon": 0, "afternoon": 0}
counties = {1: "Tehran", 2: "Isfahan", 3: "Tabriz"}
Tehran = {1: "Tehran1", 2: "Tehran2"}
Isfahan = {1: "Isfahan1", 2: "Isfahan2"}
Tabriz = {1: "Tabriz1", 2: "Tabriz2"}


def check_postal_code(postal_code):
    if len(postal_code) == 10:
        return True
    return False


def get_delivery_times():
    free_times = []
    for time, order in delivery_times:
        if time == "morning":
            free_times.append(time)
        if time == "noon" and order < 3:
            free_times.append(time)
        if time == "afternoon" and order < 3:
            free_times.append(time)
    return free_times


def allocate_delivery(county_number):
    if county_number == 1:
        return "BikeDelivery"
    return "Post"


def update_delivery_times(time):
    delivery_times[time] += 1
    return delivery_times


def estimate_delivery_time(time):
    delivery_times = update_delivery_times(time)

    number = delivery_times[time] // 6
    if time == "morning":
        return 6 + number
    if time == "noon":
        return 12 + number
    if time == "afternoon":
        return 18 + number


def allocate_delivery_price(time, delivery):
    price = 0
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

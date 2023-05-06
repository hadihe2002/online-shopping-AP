from Storage import warehouse
from Logistic import allocate_delivery, estimate_delivery_time, allocate_delivery_price
from Accountant import save_order


class Product:
    # Create attributes.
    def __init__(self, name, size, number, price, code):
        self.name = name
        self.size = size
        self.number = number
        self.price = price
        self.code = code


def run_cli():
    class Market:

        # All products in the Market with attributions in class Product.
        SAMSUNG_A30 = Product('SAMSUNG A30', '6.4 inch',
                              warehouse.warehouse[1], 200, 1)
        SAMSUNG_A50 = Product('SAMSUNG A50', '6.4 inch',
                              warehouse.warehouse[2], 300, 2)
        SAMSUNG_A70 = Product('SAMSUNG A70', '6.7 inch',
                              warehouse.warehouse[3], 500, 3)
        SAMSUNG_S07 = Product('SAMSUNG S07', '5.1 inch',
                              warehouse.warehouse[4], 300, 4)
        SAMSUNG_S10 = Product('SAMSUNG S10', '6.1 inch',
                              warehouse.warehouse[5], 400, 5)
        SAMSUNG_S20 = Product('SAMSUNG S20', '6.2 inch',
                              warehouse.warehouse[6], 600, 6)

        list_products = [SAMSUNG_A30, SAMSUNG_A50,
                         SAMSUNG_A70, SAMSUNG_S07, SAMSUNG_S10, SAMSUNG_S20]

        def Shopping_cart(list_products):
            payable_fee = 0  # Cost of orders.
            end = 1
            order_list = []  # A list of the names of the products we order.
            order_number = []  # A list of the number of the products we order.
            # A list of the price (cost) of the products we order.
            order_price = []

            while end == 1:
                # Create inventory.
                print('       I N V E N T O R Y        ')
                # Spaces are for design.
                print(1*' ', 'PRODUCT', 7*' ', 'SIZE',
                      6*' ', 'QUANTITY', 4*' ', 'PRICE')

                for i in list_products:
                    if i.number == 0:  # If the desired number of products is 0.
                        i.number = 'unavailable'
                    # Spaces are for design.
                    print(i.name, 3*' ', i.size, (8 - len(str(i.number))//2)*' ',
                          i.number, (8 - (len(str(i.number))-1)//2)*' ', i.price)

                # Taking orders.
                request_name = input('Please enter your product: ')
                request_number = int(input('How many do you want: '))

                # We will use this variable when the ordered product is not in the Market.
                x = 0
                for product in list_products:
                    if request_name == product.name:
                        x += 1
                        if product.number != 'unavailable':
                            if request_number <= product.number:
                                # Reduce order quantity from inventory.
                                warehouse.warehouse[product.code] -= request_number
                                product.number = warehouse.warehouse[product.code]
                                # Add the cost of the product to the total cost of the order.
                                payable_fee += request_number * product.price
                                # Add the ordered product to the order list.
                                order_list.append(product.name)
                                # Add the number of ordered product to the product list.
                                order_number.append(request_number)
                                # Add the cost of ordered product to the product list.
                                order_price.append(
                                    product.price * request_number)
                            else:  # If you order an item that is not available in the store in sufficient quantity.
                                print(
                                    "Sorry, We don't have enough of this product. Please check the inventory.")
                                break
                        else:  # If you order a product that is not available.
                            print("This product is unavailable.")

                if x == 0:  # If the ordered product wasn't in the Market.
                    print("Sorry, We don't have this product in our market.")

                # Show the total cost in dollars.
                print('Payable fee = ', payable_fee, '$')

                # Continue or stop the purchase process.
                end = int(input('Continue or Done? (Continue = 1, Done = 0)  '))

            def Checkout(order_list, order_number, order_price, payable_fee):
                print('\nPlease enter your information')
                # Get information about customer.
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                results = allocate_delivery()
                phone_number = input('Phone Number: ')

                delivery_time = estimate_delivery_time()

                delivery_price = allocate_delivery_price(
                    delivery_time['time'], results['delivery_type'])

                # Delivery type: Post or BikeDelivery. We will use it for COSTUMER PURCHASE FACTOR.

                # Delivery Price And Tax
                original_fee = payable_fee
                payable_fee += payable_fee * (9/100) + delivery_price

                def Payment(order_list, order_number, order_price, payable_fee, results=results, request_number=request_number):
                    # Create random order number.
                    from random import randint
                    order_number = randint(10**10, (10**11)-1)
                    print('Order Number: ', order_number)

                    # Get bank card number.
                    card_number = input('Please enter your card number: ')

                    print('\nSHOPPING PORTAL CONFIRMATION WAS SAVED.')
                    # If the number of digits of the card number was 16.
                    if len(card_number) == 16:

                        shopping_portal_confirmation = [
                            'First Name: ' + first_name, 'Last Name: ' + last_name, 'Card Number: ' + card_number]
                        # Create a text file.
                        confirmation_txt = open('confirmation', 'w')
                        confirmation_txt.write(
                            'SHOPPING PORTAL CONFIRMATION\n\n')
                        # Add shopping_portal_confirmation list members line by line to the file.
                        confirmation_txt.write(
                            '\n'.join(shopping_portal_confirmation))
                        confirmation_txt.write('\n\nPayment is Successful')
                        confirmation_txt.close()

                        print('\nCOSTUMER PURCHASE FACTOR WAS SAVED.')
                        order = 'Order:  '
                        # Creating a customer's shopping cart.
                        for i in range(len(order_list)):
                            order += str(order_list[i]) + ' = ' + \
                                str(order_price[i]) + '$  ||  '

                        # Create a text file.
                        factor_txt = open(
                            'COSTUMER PURCHASE FACTOR', 'w')
                        costumer_purchase_factor = [order, 'TOTAL COST = ' + str(payable_fee), 'Order Number: ' + str(
                            order_number), 'Full Name: ' + first_name + ' ' + last_name, 'Address: ' + results['description'], 'Delivery Time: ' + str(delivery_time['estimate']), 'Delivery Type: ' + results['delivery_type']]
                        # Add costumer_purchase_factor list members line by line to the file.
                        factor_txt.write('COSTUMER PURCHASE FACTOR\n\n')
                        factor_txt.write('\n'.join(costumer_purchase_factor))
                        factor_txt.close()

                        # Save Orders In Accountant System
                        save_order(quantity=request_number, order_num=order_number,
                                   fee=original_fee, delivery_price=delivery_price)

                    else:  # If the number of digits of the card number was not 16.
                        shopping_portal_confirmation = [
                            'First Name: ' + first_name, 'Last Name: ' + last_name, 'Card Number: ' + card_number]
                        # Create a text file.
                        confirmation_txt = open('confirmation', 'w')
                        confirmation_txt.write(
                            'SHOPPING PORTAL CONFIRMATION\n\n')
                        # Add shopping_portal_confirmation list members line by line to the file.
                        confirmation_txt.write(
                            '\n'.join(shopping_portal_confirmation))
                        confirmation_txt.write('\n\nPayment is not Successful')
                        confirmation_txt.close()

    # Calling functions.
                Payment(order_list, order_number,
                        order_price, payable_fee)
            Checkout(order_list, order_number, order_price, payable_fee)
        Shopping_cart(list_products)

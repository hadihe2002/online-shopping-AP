class Product:
    #Create attributes.
    def __init__(self, name, size, number, price, code):
        self.name = name
        self.size = size
        self.number = number
        self.price = price
        self.code = code
             

class Market:
    #All products in the Market with attributions in class Product.
    SAMSUNG_A30 = Product('SAMSUNG A30', '6.4 inch', 40, 200, 1)
    SAMSUNG_A50 = Product('SAMSUNG A50', '6.4 inch', 60, 300, 2)
    SAMSUNG_A70 = Product('SAMSUNG A70', '6.7 inch', 90, 500, 3)
    SAMSUNG_S07 = Product('SAMSUNG S07', '5.1 inch', 30, 300, 4)
    SAMSUNG_S10 = Product('SAMSUNG S10', '6.1 inch', 50, 400, 5)
    SAMSUNG_S20 = Product('SAMSUNG S20', '6.2 inch', 80, 600, 6)
    
    list_products = [SAMSUNG_A30, SAMSUNG_A50, SAMSUNG_A70, SAMSUNG_S07, SAMSUNG_S10, SAMSUNG_S20]       #A list of products.
        
    def Shopping_cart(list_products):
        payable_fee = 0      #Cost of orders.
        end = 1
        order_list = []      #A list of the names of the products we order.
        order_number = []    #A list of the number of the products we order.
        order_price = []     #A list of the price (cost) of the products we order.
        
        while end == 1:
            #Create inventory.
            print('               I N V E N T O R Y                    ')
            print(1*' ', 'PRODUCT', 7*' ', 'SIZE', 6*' ', 'QUANTITY', 4*' ', 'PRICE')     #Spaces are for design.
            
            for i in list_products:
                if i.number == 0:       #If the desired number of products is 0.
                    i.number = 'unavailable'
                print(i.name, 3*' ', i.size, (8 - len(str(i.number))//2)*' ', i.number, (8 - (len(str(i.number))-1)//2)*' ', i.price)    #Spaces are for design.

            #Taking orders.    
            request_name = input('Please enter your product: ')
            request_number = int(input('How many do you want: '))
           
            x = 0          #We will use this variable when the ordered product is not in the Market.
            for product in list_products:
                if request_name == product.name:            #Match the requested item with Market items.
                    x += 1
                    if product.number != 'unavailable':
                        if request_number <= product.number:
                            product.number -= request_number            #Reduce order quantity from inventory.
                            payable_fee += request_number * product.price          #Add the cost of the product to the total cost of the order.
                            order_list.append(product.name)         #Add the ordered product to the order list.
                            order_number.append(request_number)          #Add the number of ordered product to the product list.
                            order_price.append(product.price * request_number)          #Add the cost of ordered product to the product list.
                        else:          #If you order an item that is not available in the store in sufficient quantity.
                            print("Sorry, We don't have enough of this product. Please check the inventory.")
                            break
                    else:           #If you order a product that is not available.
                        print("This product is unavailable.")

            if x == 0:          #If the ordered product wasn't in the Market.
                print("Sorry, We don't have this product in our market.")
           
            print('Payable fee = ', payable_fee, '$')        #Show the total cost in dollars.
                
            end = int(input('Continue or Done? (Continue = 1, Done = 0)  '))          #Continue or stop the purchase process.
                    
    
        def Checkout(order_list, order_number, order_price, payable_fee):
            print('\nPlease enter your information')
            #Get information about customer.
            first_name = input('First Name: ')
            last_name = input('Last Name: ')
            address = input('Address: ')
            phone_number = input('Phone Number: ')
            delivery_time = input('Delivery Time: ')
            #Extra:  Show current time.
            import time
            current_time = time.localtime()
            print('\nTime: ', time.strftime("%H:%M:%S", current_time), '\n')
            
            #Delivery type: Post or BikeDelivery. We will use it for COSTUMER PURCHASE FACTOR.
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
                    results['delivery_type'] = "BikeDelivery"         #If you are from Tehran.
                else:
                    results['delivery_type'] = "Post"                 #If you are not from Tehran.

                results['county'] = county
                results['city'] = city
                return results
            
            results = allocate_delivery()
            
            def Payment(order_list, order_number, order_price, payable_fee, results):
                #Create random order number.
                from random import randint
                order_number = randint(10**10, (10**11)-1)
                print('\nOrder Number: ', order_number)
                
                card_number = input('Please enter your card number: ')           #Get bank card number.
                
                print('\nSHOPPING PORTAL CONFIRMATION WAS SAVED.')
                if len(card_number) == 16:        #If the number of digits of the card number was 16.
                    shopping_portal_confirmation = ['First Name: ' + first_name, 'Last Name: ' + last_name, 'Card Number: ' + card_number]
                    confirmation_txt = open('confirmation', 'w')           #Create a text file.
                    confirmation_txt.write('SHOPPING PORTAL CONFIRMATION\n\n')
                    confirmation_txt.write('\n'.join(shopping_portal_confirmation))         #Add shopping_portal_confirmation list members line by line to the file.
                    confirmation_txt.write('\n\nPayment is Successful')
                    confirmation_txt.close()
                    
                    print('\nCOSTUMER PURCHASE FACTOR WAS SAVED.')
                    order = 'Order:  '
                    for i in range(len(order_list)):         #Creating a customer's shopping cart.
                        order += str(order_list[i]) + ' = ' + str(order_price[i]) + '$  ||  '
                    
                    factor_txt = open('COSTUMER PURCHASE FACTOR', 'w')           #Create a text file.
                    costumer_purchase_factor = [order, 'TOTAL COST = ' + str(payable_fee), 'Order Number: ' + str(order_number), 'Full Name: ' + first_name + ' ' + last_name, 'Address: ' + address, 'Delivery Time: ' + delivery_time, 'Delivery Type: ' + results['delivery_type']]
                    factor_txt.write('COSTUMER PURCHASE FACTOR\n\n')         #Add costumer_purchase_factor list members line by line to the file.
                    factor_txt.write('\n'.join(costumer_purchase_factor))
                    factor_txt.close()
                
                else:          #If the number of digits of the card number was not 16.
                    shopping_portal_confirmation = ['First Name: ' + first_name, 'Last Name: ' + last_name, 'Card Number: ' + card_number]
                    confirmation_txt = open('confirmation', 'w')           #Create a text file.
                    confirmation_txt.write('SHOPPING PORTAL CONFIRMATION\n\n')
                    confirmation_txt.write('\n'.join(shopping_portal_confirmation))            #Add shopping_portal_confirmation list members line by line to the file.
                    confirmation_txt.write('\n\nPayment is not Successful')
                    confirmation_txt.close()
                    
#Calling functions.                    
            Payment(order_list, order_number, order_price, payable_fee, results)   
        Checkout(order_list, order_number, order_price, payable_fee)
    Shopping_cart(list_products)

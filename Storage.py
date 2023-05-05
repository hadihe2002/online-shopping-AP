import csv
import sys

class StorageSystem:
    def __init__(self):
        self.warehouse = {
            1: 200,
            2: 300,
            3: 500,
            4: 300,
            5: 400,
            6: 600
        }
    
    def update_storage_after_order(self, product_code, quantity):
        if product_code in self.warehouse:
            self.warehouse[product_code] -= quantity
            if self.warehouse[product_code] == 0:
                print("This product is currently unavailable.")
        else:
            print(f"This product ({product_code}) is not available in our warehouse.")
    
    def update_storage_as_manager_csv(self, file_path):
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                product_code = row[0]
                new_quantity = int(row[1])
                self.update_storage_as_manager(product_code, new_quantity)
    
    def update_storage_as_manager_input(self, product_code, new_quantity):
        self.warehouse[product_code] = new_quantity
    
    def add_to_storage_as_manager(self, product_code, additional_quantity):
        if product_code in self.warehouse:
            self.warehouse[product_code] += additional_quantity
        else:
            self.warehouse[product_code] = additional_quantity
    
    def get_available_products_csv(self):
        with open('available_products.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Product Code", "Available Quantity"])
            for product_code, quantity in self.warehouse.items():
                writer.writerow([product_code, quantity])
            print("The available products have been exported to `available_products.csv`.")
    

end = 1

while end != 0:
    print("Please enter your command and the rest of the required information:")
    print("For updating after an order, enter the product code and the quantity.")
    print("For updating as manager with CSV, enter the file path.")
    print("For updating as manager with input, enter the product code and the new quantity.")
    print("To add to storage as manager, enter the product code and the additional quantity")
    print("To receive a CSV of the storage, enter export CSV")
    command = input().split(" ")
    if command[0] == "order":
        product_code = int(command[1])
        quantity = int(command[2])
        StorageSystem.update_storage_after_order(product_code, quantity)
        print("Storage updated successfully.")
    elif command[0] == "update_csv":
        file_path = command[1]
        StorageSystem.update_storage_as_manager_csv(file_path)
        print("Storage updated successfully.")
    elif command[0] == "update_input":
        product_code = int(command[1])
        new_quantity = int(command[2])
        StorageSystem.update_storage_as_manager_input(product_code, new_quantity)
        print("Storage updated successfully.")
    elif command[0] == "add":
        product_code = int(command[1])
        additional_quantity = int(command[2])
        StorageSystem.add_to_storage_as_manager(product_code, additional_quantity)
        print("Storage updated successfully.")
    elif command[0] == "export_csv":
        StorageSystem.get_available_products_csv()
        print("The available products have been exported to `available_products.csv`.")
    else:
        print("Invalid command")
    
    print("Will there be anything else for today ?  0(No), 1(yes!)")
    end = int(input())


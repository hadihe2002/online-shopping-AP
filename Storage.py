import csv

class StorageSystem:
    def __init__(self):
        self.warehouse = {}
    
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
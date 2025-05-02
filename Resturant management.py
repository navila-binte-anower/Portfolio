class Customer:
    def __init__(self, username, name, email, address):
        self.username = username
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.orders = []

    def view_menu(self, restaurant):
        restaurant.show_menu()

    def add_funds(self, amount):
        self.balance += amount
        print(f"{amount} Tk added. Current balance: {self.balance} Tk")

    def place_order(self, restaurant, item):
        if item in restaurant.menu:
            price = restaurant.menu[item]
            if self.balance >= price:
                self.balance -= price
                self.orders.append(item)
                print(f"Order placed: {item}. Remaining balance: {self.balance} TK")
            else:
                print("Insufficient balance.")
        else:
            print("Item not available.")

    def view_orders(self):
        print("Past Orders:", self.orders)

    def view_balance(self):
        print(f"Current balance: {self.balance}")

class Admin:
    def __init__(self, name):
        self.name = name

    def add_customer(self, restaurant, username, name, email, address):
        restaurant.customers[username] = Customer(username, name, email, address)
        print(f"Customer {name} added with username: {username}")

    def remove_customer(self, restaurant, username):
        if username in restaurant.customers:
            del restaurant.customers[username]
            print("Customer removed.")
        else:
            print("Customer not found.")

    def add_menu_item(self, restaurant, item, price):
        restaurant.menu[item] = price
        print(f"{item} added to menu.")

    def remove_menu_item(self, restaurant, item):
        if item in restaurant.menu:
            del restaurant.menu[item]
            print(f"{item} removed from menu.")
        else:
            print("Item not found.")

class Restaurant:
    def __init__(self):
        self.menu = {}
        self.customers = {}

    def show_menu(self):
        if self.menu:
            print("--- Restaurant Menu ---")
            for item, price in self.menu.items():
                print(f"{item}:{price} Tk")
        else:
            print("Menu is empty.")

    def show_customers(self):
        if self.customers:
            print("--- Registered Customers ---")
            for username, customer in self.customers.items():
                print(f"{customer.name} - {customer.username}")
        else:
            print("No customers found.")

def main():
    restaurant = Restaurant()
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        option = input("Select an option: ")
        
        if option == "1":
            admin_name = input("Enter Admin Name: ")
            admin = Admin(admin_name)
            while True:
                print("\n--- Admin Menu ---")
                print("1. Create Customer Account")
                print("2. Remove Customer Account")
                print("3. View All Customers")
                print("4. Manage Restaurant Menu")
                print("5. Exit")
                choice = input("Select an option: ")
                if choice == "1":
                    username = input("Enter username: ")
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    admin.add_customer(restaurant, username, name, email, address)
                elif choice == "2":
                    username = input("Enter username to remove: ")
                    admin.remove_customer(restaurant, username)
                elif choice == "3":
                    restaurant.show_customers()
                elif choice == "4":
                    while True:
                        print("\n--- Manage Restaurant Menu ---")
                        print("1. Add Menu Item")
                        print("2. Remove Menu Item")
                        print("3. Show Menu")
                        print("4. Back")
                        menu_choice = input("Select an option: ")
                        if menu_choice == "1":
                            item = input("Enter item name: ")
                            price = float(input("Enter price: "))
                            admin.add_menu_item(restaurant, item, price)
                        elif menu_choice == "2":
                            item = input("Enter item name to remove: ")
                            admin.remove_menu_item(restaurant, item)
                        elif menu_choice == "3":
                            restaurant.show_menu()
                        elif menu_choice == "4":
                            break
                        else:
                            print("Invalid option.")
                elif choice == "5":
                    break
                else:
                    print("Invalid option.")
        
        elif option == "2":
            username = input("Enter Customer Username: ")
            customer = restaurant.customers.get(username)
            if customer:
                while True:
                    print(f"\n--- {customer.name}'s Menu ---")
                    print("1. View Restaurant Menu")
                    print("2. View Balance")
                    print("3. Add Balance")
                    print("4. Place Order")
                    print("5. View Past Orders")
                    print("6. Exit")
                    choice = input("Select an option: ")
                    if choice == "1":
                        customer.view_menu(restaurant)
                    elif choice == "2":
                        customer.view_balance()
                    elif choice == "3":
                        amount = float(input("Enter amount to add: "))
                        customer.add_funds(amount)
                    elif choice == "4":
                        item = input("Enter item name to order: ")
                        customer.place_order(restaurant, item)
                    elif choice == "5":
                        customer.view_orders()
                    elif choice == "6":
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Customer not found.")
        
        elif option == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

main()

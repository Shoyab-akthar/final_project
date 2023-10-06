import uuid

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = str(uuid.uuid4())
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Restaurant:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for item in self.food_items:
            if item.food_id == food_id:
                item.name = name
                item.quantity = quantity
                item.price = price
                item.discount = discount
                item.stock = stock
                return True
        return False

    def view_food_items(self):
        for item in self.food_items:
            print(f"FoodID: {item.food_id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}, Discount: {item.discount}, Stock: {item.stock}")

    def remove_food_item(self, food_id):
        for item in self.food_items:
            if item.food_id == food_id:
                self.food_items.remove(item)
                return True
        return False

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.user_id = str(uuid.uuid4())
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class RestaurantApp:
    def __init__(self):
        self.users = []
        self.restaurant = Restaurant()
        self.orders = []

    def register_user(self):
        full_name = input("Enter your full name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")

        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)
        print("Registration successful. Your user ID is", user.user_id)

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None

    def display_menu(self):
        print("Menu:")
        for i, item in enumerate(self.restaurant.food_items, start=1):
            print(f"{i}. {item.name} ({item.quantity}) [INR {item.price}]")

    def place_order(self, user):
        self.display_menu()
        food_selection = input("Enter the numbers of the items you want to order (e.g., 1 2 3): ").split()
        food_selection = [int(x) for x in food_selection]

        selected_items = []
        total_price = 0

        for i in food_selection:
            if 1 <= i <= len(self.restaurant.food_items):
                item = self.restaurant.food_items[i - 1]
                selected_items.append(item)
                total_price += item.price

        print("You have selected the following items:")
        for item in selected_items:
            print(f"- {item.name} ({item.quantity}) [INR {item.price}]")

        print(f"Total Price: INR {total_price}")

        option = input("Do you want to place the order? (yes/no): ")
        if option.lower() == 'yes':
            order_details = {"user_id": user.user_id, "items": selected_items, "total_price": total_price}
            self.orders.append(order_details)
            print("Order placed successfully.")
        else:
            print("Order not placed.")

    def view_order_history(self, user):
        print("Order History for User ID", user.user_id)
        for order in self.orders:
            if order["user_id"] == user.user_id:
                print("Order:")
                for item in order["items"]:
                    print(f"- {item.name} ({item.quantity}) [INR {item.price}]")
                print(f"Total Price: INR {order['total_price']}")

    def update_profile(self, user):
        full_name = input("Enter your updated full name: ")
        phone_number = input("Enter your updated phone number: ")
        email = input("Enter your updated email: ")
        address = input("Enter your updated address: ")
        password = input("Enter your updated password: ")

        user.full_name = full_name
        user.phone_number = phone_number
        user.email = email
        user.address = address
        user.password = password
        print("Profile updated successfully.")

if __name__ == "__main__":
    app = RestaurantApp()
    app.restaurant.add_food_item("Tandoori Chicken", "4 pieces", 240, 10, 50)
    app.restaurant.add_food_item("Vegan Burger", "1 piece", 320, 15, 30)
    app.restaurant.add_food_item("Truffle Cake", "500gm", 900, 5, 40)

    while True:
        print("\n------ Restaurant Application ------")
        print("1. Register")
        print("2. Log in")
        print("3. Place New Order")
        print("4. Order History")
        print("5. Update Profile")
        print("6. Add Food Item")
        print("7. Edit Food Item")
        print("8. View Food Items")
        print("9. Remove Food Item")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            app.register_user()
        elif choice == 2:
            user = app.login()
            if user:
                print("Login successful.")
            else:
                print("Invalid credentials. Please try again.")
        elif choice == 3:
            if user:
                app.place_order(user)
            else:
                print("Please log in first.")
        elif choice == 4:
            if user:
                app.view_order_history(user)
            else:
                print("Please log in first.")
        elif choice == 5:
            if user:
                app.update_profile(user)
            else:
                print("Please log in first.")
        elif choice == 6:
            if user:
                pass
        elif choice == 7:
            if user:
                pass
        elif choice == 8:
            if user:
                app.restaurant.view_food_items()
            else:
                print("Please log in first.")
        elif choice == 9:
            if user:
                pass
        elif choice == 10:
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Restaurant Application. Goodbye!")
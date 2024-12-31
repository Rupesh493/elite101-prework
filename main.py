import random

def chatbot():
    print("Welcome to the food ordering chatbot!")

    # Collecting user's name and age
    name = input("What is your name? ")
    while True:
        try:
            age = int(input(f"Nice to meet you, {name}! How old are you? "))
            break
        except ValueError:
            print("Please enter a valid age.")

    print(f"Thanks, {name}! It's great to have you here.")

    order_history, order_status, order_time = [], {}, {}

    # Menu of options
    options = ["1. View the menu", "2. Place an order", "3. Check how much longer your food will take", "4. Exit"]
    
    while True:
        print("\n".join(options))
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("Menu: Burritos, Pizzas, Burgers, Tacos, Pasta")
        
        elif choice == "2":
            current_order = []
            print("Type 'done' to finish your order.")
            while True:
                print("What would you like to order?")
                order = input("Enter your choice: ").strip().lower()
                if order == "done": break
                if order in ["pizza", "burritos", "burgers", "tacos", "pasta"]:
                    current_order.append(order.capitalize())
                    print(f"Added {order.capitalize()} to your order.")
                else:
                    print("Invalid item.")
            
            if current_order:
                print(f"You've ordered: {', '.join(current_order)}")
                if input("Confirm order? (yes/no): ").strip().lower() == "yes":
                    order_id = len(order_history) + 1
                    time = random.randint(1, 3)
                    order_history.append(current_order)
                    order_status[order_id] = random.choice(["Pending", "In Progress", "Completed"])
                    order_time[order_id] = time
                    print(f"Order {order_id} placed. Ready in {time} minutes.")
        
        elif choice == "3":
            if order_history:
                last_order_id = len(order_history)
                print(f"Your most recent order will be ready in {order_time[last_order_id]} minutes.")
            else:
                print("No orders yet.")
        
        elif choice == "4":
            print("Thank you for chatting with me! Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    chatbot()

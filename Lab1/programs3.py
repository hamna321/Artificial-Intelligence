def show_menu(menu_items):
    try:
        print("Enter the Number of Your Choice 😊.")
        for i, item in enumerate(menu_items, 1):
            print(f"{i}. {item}")
        
        choice = int(input("Which Number you would like to Order? "))
        
        if 1 <= choice <= len(menu_items):
            print(f"You Choose {choice}.{menu_items[choice - 1]}")
        else:
            print("Invalid choice. Please enter a number from the menu.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("Your choice was invalid:", e)

menu = ["Soup and Salad", "Pasta with Meat Sauce", "Chef's Special"]

show_menu(menu)

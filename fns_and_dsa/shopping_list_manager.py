def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    status = True
    while status:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            new_item = input("Add a new item to the menu: ")
            shopping_list.append(new_item)
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Add a new item to the menu: ")
            shopping_list.remove(remove_item)
        elif choice == '3':
            # Display the shopping list
            print(".................Shopping List ..................")
            for item in shopping_list:
                print(item)
        elif choice == '4':
            status = False
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
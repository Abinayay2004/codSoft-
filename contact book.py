contact = {}

def view_contact():
    print("Name\t\tContact Number")
    print("-" * 30)
    for key, value in contact.items():
        print(f"{key}\t\t{value}")

while True:
    print("\n1. Add new contact")
    print("\n2. Search contact")
    print("\n3. View contact")
    print("\n4. Update contact")
    print("\n5. Delete contact")
    print("\n6. Exit")
    choice = input("Enter your choice 1/2/3/4/5/6: ")

    if choice == '1':
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
        print(f"Contact {name} added successfully.")

    elif choice == '2':
        search_name = input("Enter the contact name to be searched: ")
        if search_name in contact:
            print(f"{search_name}'s contact number is {contact[search_name]}")
        else:
            print(f"{search_name} is not found in the contact book.")

    elif choice == '3':
        if not contact:
            print("Your contact book is empty.")
        else:
            view_contact()

    elif choice == '4':
        update_contact = input("Enter the contact name to be updated: ")
        if update_contact in contact:
            new_phone = input("Enter the new mobile number: ")
            contact[update_contact] = new_phone
            print("Contact updated successfully.")
            view_contact()
        else:
            print("Name is not found in the contact book.")

    elif choice == '5':
        delete_contact = input("Enter the contact name to be deleted: ")
        if delete_contact in contact:
            confirm = input("Do you want to delete this contact yes/no?: ")
            if confirm.lower() == "yes":
                contact.pop(delete_contact)
                print(f"{delete_contact} is deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"{delete_contact} is not found in the contact book.")

    elif choice == '6':
        print("Exiting the contact book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
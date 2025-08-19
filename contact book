contacts = {}

def add_contact():
    """Add a new contact"""
    name = input("Enter Name: ").strip().title()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts[phone] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    print(f" Contact '{name}' added successfully!\n")

def view_contacts():
    """View all contacts"""
    if not contacts:
        print(" No contacts available.\n")
        return
    
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts.values(), 1):
        print(f"{idx}. {contact['Name']} - {contact['Phone']}")
    print()

def search_contact():
    """Search contact by name or phone"""
    search = input(" Enter Name or Phone Number to search: ").strip().title()

    found = False
    for contact in contacts.values():
        if contact["Name"] == search or contact["Phone"] == search:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}\n")
            found = True
            break
    if not found:
        print(" Contact not found.\n")

def update_contact():
    """Update contact details"""
    phone = input("Enter the Phone Number of the contact to update: ").strip()

    if phone in contacts:
        print("\nLeave blank if you don't want to change a field.")
        name = input("New Name: ").strip().title()
        email = input("New Email: ").strip()
        address = input("New Address: ").strip()

        if name: contacts[phone]["Name"] = name
        if email: contacts[phone]["Email"] = email
        if address: contacts[phone]["Address"] = address

        print(" Contact updated successfully!\n")
    else:
        print(" Contact not found.\n")

def delete_contact():
    """Delete a contact"""
    phone = input("Enter the Phone Number of the contact to delete: ").strip()
    if phone in contacts:
        del contacts[phone]
        print(" Contact deleted successfully!\n")
    else:
        print(" Contact not found.\n")

def contact_book():
    """Main menu for Contact Book"""
    while True:
        print("===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


contact_book()

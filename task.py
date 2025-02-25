def display_menu():
    print("\n" + "=" * 40)
    print("     📇 Contact List Application     ")
    print("=" * 40)
    print("1. ➕ Add new contact")
    print("2. 📜 View all contacts")
    print("3. 🔍 Search for a contact (Optional)")
    print("4. ❌ Delete a contact (Optional)")
    print("5. 🚪 Exit")
    print("=" * 40)

def add_contact(contacts):
    print("\n--- Adding a New Contact ---")
    while True:
        name = input("Enter contact name: ").strip()
        if name:
            break
        else:
            print("⚠️ Name cannot be empty. Please enter a valid name.")

    while True:
        phone = input("Enter contact phone number: ").strip()
        if phone.isdigit():
            break
        else:
            print("⚠️ Phone number must contain only digits. Please enter a valid phone number.")

    contacts.append({'name': name, 'phone': phone})
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("📭 No contacts available.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(contacts):
    print("\n--- Search For a Contact ---")
    name = input("Enter the name to search: ").strip()
    if not name:
        print("⚠️ Name cannot be empty.")
        return

    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"🔍 Found: Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
            break
    if not found:
        print("🚫 Contact not found.")

def delete_contact(contacts):
    print("\n--- Delete a Contact ---")
    name = input("Enter the name to delete: ").strip()
    if not name:
        print("⚠️ Name cannot be empty.")
        return

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"❌ Contact '{name}' deleted successfully!")
            return
    print("🚫 Contact not found.")

def main():
    contacts = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice in ['1', '2', '3', '4', '5']:
            if choice == '1':
                add_contact(contacts)
            elif choice == '2':
                view_contacts(contacts)
            elif choice == '3':
                search_contact(contacts)
            elif choice == '4':
                delete_contact(contacts)
            elif choice == '5':
                print("👋 Exiting application. Goodbye!")
                break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

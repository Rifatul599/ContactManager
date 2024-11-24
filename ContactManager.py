class ContactManager:
    def __init__(self):
        # Initialize an empty dictionary to store contacts
        self.contacts = {}

    def add_contact(self, name, phone, email):
        """
        Adds a new contact with the given name, phone, and email.
        If the contact already exists, it updates the contact instead.
        """
        if name in self.contacts:
            print(f"Contact for '{name}' already exists. Updating the contact.")
        # Add or update the contact in the dictionary
        self.contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact for {name} added/updated.")

    def remove_contact(self, name):
        """
        Removes a contact by the name.
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} removed.")
        else:
            print(f"No contact found for '{name}'.")

    def search_contact(self, name):
        """
        Searches for a contact by name and returns the details.
        """
        contact = self.contacts.get(name)
        if contact:
            return contact
        else:
            return f"No contact found for '{name}'."

    def list_contacts(self):
        """
        Lists all stored contacts.
        """
        if not self.contacts:
            print("No contacts stored.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    def update_contact(self, name, phone=None, email=None):
        """
        Updates the contact details for the given name.
        Only the provided fields (phone or email) will be updated.
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print(f"Contact for {name} updated.")
        else:
            print(f"No contact found for '{name}'.")

    def count_contacts(self):
        """
        Returns the total number of contacts.
        """
        return len(self.contacts)


# Example usage
if __name__ == "__main__":
    # Create an instance of the ContactManager
    cm = ContactManager()

    # Add contacts
    cm.add_contact("John Doe", "555-1234", "john@example.com")
    cm.add_contact("Jane Smith", "555-5678", "jane@example.com")

    # List contacts
    cm.list_contacts()

    # Search for a contact
    print(cm.search_contact("John Doe"))

    # Update a contact
    cm.update_contact("John Doe", phone="555-4321")

    # List contacts again to see the update
    cm.list_contacts()

    # Remove a contact
    cm.remove_contact("Jane Smith")

    # List contacts after removal
    cm.list_contacts()

    # Count contacts
    print(f"Total contacts: {cm.count_contacts()}")



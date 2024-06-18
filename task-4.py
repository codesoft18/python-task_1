import tkinter as tk
from tkinter import messagebox

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Contacts dictionary to store contacts
        self.contacts = {}

        # Create UI elements
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, sticky="e")
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=4, column=0, sticky="e")
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=4, column=1)

        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(root, text="Update", command=self.update_contact)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_contact)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name.strip() == '' or phone.strip() == '':
            messagebox.showerror("Error", "Name and Phone fields cannot be empty.")
            return
        self.contacts[name] = phone
        messagebox.showinfo("Success", "Contact added successfully.")
        self.clear_entries()

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        search_term = self.search_entry.get()
        if search_term.strip() == '':
            messagebox.showerror("Error", "Search field cannot be empty.")
            return
        if search_term in self.contacts:
            messagebox.showinfo("Contact Found", f"{search_term}: {self.contacts[search_term]}")
        else:
            messagebox.showinfo("Contact Not Found", f"No contact found for '{search_term}'.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name.strip() == '' or phone.strip() == '':
            messagebox.showerror("Error", "Name and Phone fields cannot be empty.")
            return
        if name in self.contacts:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact updated successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No contact found with name '{name}'.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name.strip() == '':
            messagebox.showerror("Error", "Name field cannot be empty.")
            return
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No contact found with name '{name}'.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

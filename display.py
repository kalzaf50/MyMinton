import sqlite3
import tkinter as tk
from tkinter import ttk

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to display data in the treeview
def display_data():
    for row in tree.get_children():
        tree.delete(row)
    rows = fetch_data()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Create the main window
root = tk.Tk()
root.title("Players Data")

# Create a treeview widget
tree = ttk.Treeview(root, columns=("ID", "Name", "Country", "Rank", "Category", "Created At"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Country", text="Country")
tree.heading("Rank", text="Rank")
tree.heading("Category", text="Category")
tree.heading("Created At", text="Created At")

tree.pack(fill=tk.BOTH, expand=True)

# Create a button to refresh the data
refresh_button = tk.Button(root, text="Refresh Data", command=display_data)
refresh_button.pack(pady=10)

# Display the data initially
display_data()

# Run the application
root.mainloop()

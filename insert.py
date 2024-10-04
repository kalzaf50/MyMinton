import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to insert data into the database
def insert_data():
    name = entry_name.get()
    country = entry_country.get()
    rank = entry_rank.get()
    category = entry_category.get()

    if name and country and rank and category:
        try:
            conn = sqlite3.connect('players.db')
            cursor = conn.cursor()
            insert_query = '''
            INSERT INTO players (name, country, rank, category)
            VALUES (?, ?, ?, ?);
            '''
            cursor.execute(insert_query, (name, country, rank, category))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data inserted successfully!")
            entry_name.delete(0, tk.END)
            entry_country.delete(0, tk.END)
            entry_rank.delete(0, tk.END)
            entry_category.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Country must be unique.")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Create the main window
root = tk.Tk()
root.title("Insert Player Data")

# Create and place the labels and entry widgets
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Country").grid(row=1, column=0, padx=10, pady=5)
entry_country = tk.Entry(root)
entry_country.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Rank").grid(row=2, column=0, padx=10, pady=5)
entry_rank = tk.Entry(root)
entry_rank.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Category").grid(row=3, column=0, padx=10, pady=5)
entry_category = tk.Entry(root)
entry_category.grid(row=3, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=insert_data)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

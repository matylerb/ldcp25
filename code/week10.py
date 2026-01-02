import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# --- DATABASE SETUP ---
def setup_database():
    conn = sqlite3.connect("session_data.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS musicians")
    cursor.execute('''CREATE TABLE musicians (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        instrument TEXT,
                        skill_level INTEGER)''')
    
    # Adding sample data
    sample_musicians = [
        ('Aoife', 'Fiddle', 8),
        ('Liam', 'Guitar', 6),
        ('Máire', 'Flute', 9),
        ('Tom', 'Bodhrán', 4),
        ('Siobhán', 'Uilleann Pipes', 10),
        ('Paddy', 'Banjo', 7)
    ]
    cursor.executemany("INSERT INTO musicians (name, instrument, skill_level) VALUES (?, ?, ?)", sample_musicians)
    conn.commit()
    conn.close()

# --- GUI CLASS ---
class MusicDBApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Irish Music Session Database")
        self.root.geometry("600x400")

        # 1. Search Section
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Search Name/Instrument:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_btn = tk.Button(search_frame, text="Filter", command=self.load_data)
        self.search_btn.pack(side=tk.LEFT, padx=5)

        # 2. Treeview (Table) Section
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Defining Columns
        columns = ("id", "name", "instrument", "skill")
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Musician Name")
        self.tree.heading("instrument", text="Instrument")
        self.tree.heading("skill", text="Skill Level")

        self.tree.column("id", width=50)
        self.tree.column("name", width=150)
        self.tree.column("instrument", width=150)
        self.tree.column("skill", width=100)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load initial data
        self.load_data()

    def load_data(self):
        """Connects to SQL and filters data based on the entry field."""
        # Clear existing rows in the Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        search_query = self.search_var.get()

        try:
            conn = sqlite3.connect("session_data.db")
            cursor = conn.cursor()
            
            # Use SQL LIKE for partial matching
            query = "SELECT * FROM musicians WHERE name LIKE ? OR instrument LIKE ?"
            params = (f'%{search_query}%', f'%{search_query}%')
            cursor.execute(query, params)
            
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)
            
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load data: {e}")

# --- MAIN ---
if __name__ == "__main__":
    setup_database() # Create DB and table
    root = tk.Tk()
    app = MusicDBApp(root)
    root.mainloop()
import tkinter as tk

class Page1Screen(tk.Frame):
    def __init__(self, master, proceed_callback):
        super().__init__(master)
        
        # Set the main background
        self.pack(expand=True, fill='both')
        self.configure(bg='white')

        # Header label
        tk.Label(self, text="*Is this information correct? If not, please tap the boxes to update it.", 
                 bg='white', font=("Arial", 14)).pack(pady=20)

        # Input fields label and entry
        self.id_number_label = tk.Label(self, text="ID Number", bg='white', font=("Arial", 12))
        self.id_number_label.pack(pady=(5, 0))
        self.id_number_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.id_number_entry.pack(pady=5)

        self.course_label = tk.Label(self, text="Course", bg='white', font=("Arial", 12))
        self.course_label.pack(pady=(5, 0))
        self.course_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.course_entry.pack(pady=5)

        self.name_label = tk.Label(self, text="Name", bg='white', font=("Arial", 12))
        self.name_label.pack(pady=(5, 0))
        self.name_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.name_entry.pack(pady=5)

        self.year_level_label = tk.Label(self, text="Year Level", bg='white', font=("Arial", 12))
        self.year_level_label.pack(pady=(5, 0))
        self.year_level_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.year_level_entry.pack(pady=5)

        # Confirm button
        tk.Button(self, text="Confirm", command=proceed_callback, font=("Arial", 12), 
                  bg='blue', fg='white').pack(pady=20)



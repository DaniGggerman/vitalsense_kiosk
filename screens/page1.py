import tkinter as tk

class Page1Screen(tk.Frame):
    def __init__(self, master, proceed_callback):
        super().__init__(master)
        self.pack(expand=True, fill='both')
        tk.Label(self, text="Page 1", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Proceed to Page 2", command=proceed_callback).pack(pady=10)
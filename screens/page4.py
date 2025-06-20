import tkinter as tk

class Page4Screen(tk.Frame):
    def __init__(self, master, logout_callback):
        super().__init__(master)
        self.pack(expand=True, fill='both')
        tk.Label(self, text="Page 4", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Logout", command=logout_callback).pack(pady=10)
import tkinter as tk

class Page2Screen(tk.Frame):
    def __init__(self, master, proceed_callback):
        super().__init__(master)
        self.pack(expand=True, fill='both')
        tk.Label(self, text="Page 2", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Proceed to Page 3", command=proceed_callback).pack(pady=10)
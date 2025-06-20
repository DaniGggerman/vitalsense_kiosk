import tkinter as tk

class Page3Screen(tk.Frame):
    def __init__(self, master, proceed_callback):
        super().__init__(master)
        self.pack(expand=True, fill='both')
        tk.Label(self, text="Page 3", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Proceed to Page 4", command=proceed_callback).pack(pady=10)
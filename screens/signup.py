import tkinter as tk

class SignupScreen(tk.Frame):
    def __init__(self, master, on_back):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        tk.Label(self, text="Signup Page", font=("Arial", 24)).pack(pady=40)
        tk.Button(self, text="Back to Login", command=on_back).pack(pady=20)

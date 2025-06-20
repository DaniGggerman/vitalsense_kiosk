# screens/dashboard_screen.py
import tkinter as tk

class DashboardScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        tk.Label(self, text="Welcome to the Dashboard!", font=("Arial", 24)).pack(pady=100)
        tk.Button(self, text="Logout", command=self.logout).pack(pady=20)

    def logout(self):
        self.master.show_login()

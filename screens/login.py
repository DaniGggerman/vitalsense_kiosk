import tkinter as tk

USERNAME = "admin"
PASSWORD = "password"

class LoginScreen(tk.Frame):
    def __init__(self, master, on_login_success, on_signup):
        super().__init__(master)
        self.on_login_success = on_login_success
        self.pack(fill="both", expand=True)

        tk.Label(self, text="ID Number:").pack(pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:").pack(pady=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.message = tk.Label(self, text="", fg="red")
        self.message.pack(pady=5)

        tk.Button(self, text="Login", command=self.validate_login).pack(pady=20)
        tk.Button(self, text="Sign Up", command=on_signup).pack(pady=10)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == USERNAME and password == PASSWORD:
            self.on_login_success()
        else:
            self.message.config(text="Invalid credentials!")

import tkinter as tk

class Page2Screen(tk.Frame):
    def __init__(self, master, proceed_callback):
        super().__init__(master, bg='#ADD8E6') # Light blue background for the entire page, can be changed or removed

        self.pack(expand=True, fill='both')

        # --- Blood Pressure Frame ---
        self.bp_frame = tk.Frame(self, bg='black', bd=0, relief='solid', highlightbackground="white", highlightthickness=0)
        self.bp_frame.pack(pady=(150, 20), padx=50, fill='x')
        self.bp_frame.pack_propagate(False) # Prevent the frame from shrinking to fit its contents
        self.bp_frame.config(height=100) # Set a fixed height for the frame

        tk.Label(self.bp_frame, text="Blood Pressure", fg='white', bg='black', font=("Arial", 20, "bold")).pack(pady=(10, 0))
        tk.Label(self.bp_frame, text="120/80", fg='white', bg='black', font=("Arial", 28)).pack(pady=(0, 10))

        # --- Heart Rate Frame ---
        self.hr_frame = tk.Frame(self, bg='black', bd=0, relief='solid', highlightbackground="white", highlightthickness=0)
        self.hr_frame.pack(pady=20, padx=50, fill='x')
        self.hr_frame.pack_propagate(False)
        self.hr_frame.config(height=100)

        tk.Label(self.hr_frame, text="Heart Rate", fg='white', bg='black', font=("Arial", 20, "bold")).pack(pady=(10, 0))
        tk.Label(self.hr_frame, text="72 Bpm", fg='white', bg='black', font=("Arial", 28)).pack(pady=(0, 10))

        # --- Temperature Frame ---
        self.temp_frame = tk.Frame(self, bg='black', bd=0, relief='solid', highlightbackground="white", highlightthickness=0)
        self.temp_frame.pack(pady=20, padx=50, fill='x')
        self.temp_frame.pack_propagate(False)
        self.temp_frame.config(height=100)

        tk.Label(self.temp_frame, text="Temperature", fg='white', bg='black', font=("Arial", 20, "bold")).pack(pady=(10, 0))
        tk.Label(self.temp_frame, text="37C", fg='white', bg='black', font=("Arial", 28)).pack(pady=(0, 10))

        tk.Button(self, text="Confirm", command=proceed_callback, font=("Arial", 12), 
                  bg='blue', fg='white').pack(pady=20)
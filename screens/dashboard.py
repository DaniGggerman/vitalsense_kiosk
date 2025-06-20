import tkinter as tk

consent = "Do you agree to share your recorded health and emotional status data with the University Clinic and the Office of Guidance and Counseling Services to help monitor your well-being while enrolled at USTP?"

class DashboardScreen(tk.Frame):
    def __init__(self, master, proceed_callback):
        super().__init__(master)
        self.pack(expand=True, fill='both')

        main_frame = tk.Frame(self)
        main_frame.pack(expand=True)

        consent_label = tk.Label(main_frame, text=consent, wraplength=600, font=("Arial", 18), justify='center')
        consent_label.pack(pady=(0, 30))

        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)

        yes_button = tk.Button(button_frame, text="Yes", command=lambda: self.handle_consent(True), font=("Arial", 16), padx=10, pady=10)
        yes_button.pack(side='left', padx=20)

        no_button = tk.Button(button_frame, text="No", command=lambda: self.handle_consent(False), font=("Arial", 16), padx=10, pady=10)
        no_button.pack(side='left', padx=20)

        confirm_button = tk.Button(main_frame, text="Confirm", command=proceed_callback, font=("Arial", 18), padx=20, pady=10)
        confirm_button.pack(pady=(20, 0))

    def handle_consent(self, consent_given):
        if consent_given:
            print("User agreed to share data.")
        else:
            print("User did not agree to share data.")


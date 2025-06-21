import tkinter as tk

class Page4Screen(tk.Frame):
    def __init__(self, master, logout_callback):
        super().__init__(master, bg='#ADD8E6') # Light blue background, consistent
        self.pack(expand=True, fill='both')

        # Thank you message
        tk.Label(self,
                 text="Thank you for using VITALSENSE!",
                 font=("Arial", 36, "bold"), # Larger, bold font
                 fg="black", # Or whatever color contrasts well with your background
                 bg=self['bg']
                ).pack(pady=(200, 20)) # Top padding to position it down, some space below

        # Press anywhere message
        tk.Label(self,
                 text="Press anywhere to continue",
                 font=("Arial", 18), # Smaller font
                 fg="black",
                 bg=self['bg']
                ).pack(pady=10)

        # Bind any mouse click event on this frame to the logout_callback
        self.bind("<Button-1>", lambda event: logout_callback()) # Left mouse click
        # To make sure clicks on the labels also trigger it, bind them too
        for widget in self.winfo_children():
            widget.bind("<Button-1>", lambda event: logout_callback())
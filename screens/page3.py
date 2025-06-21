import tkinter as tk

class Page3Screen(tk.Frame):
    def __init__(self, master, proceed_callback, on_back):
        super().__init__(master, bg='#ADD8E6') # Light blue background, consistent with Page2, can be changed or removed
        self.pack(expand=True, fill='both')

        # Frame to hold the emotion buttons, to center them horizontally
        self.emotion_frame = tk.Frame(self, bg=self['bg']) # Use the same background as the parent frame
        self.emotion_frame.pack(pady=150) # Adjust pady to position the emotion buttons vertically

        emotions = ["Happy", "Nothing", "Sad", "Worried", "Anxious"]

        # Create buttons for each emotion
        for emotion in emotions:
            # We're creating a simple button for now, as direct circular buttons are complex with default Tkinter.
            # We'll use a larger font and padding to make them appear prominent.
            btn = tk.Button(self.emotion_frame,
                            text=emotion,
                            font=("Arial", 16),
                            width=10, # Fixed width for uniformity
                            height=2, # Fixed height for uniformity
                            bg="lightgray", # A neutral background for the button
                            fg="black", # Text color
                            command=lambda e=emotion: self.select_emotion(e)) # Command to handle selection
            btn.pack(side=tk.LEFT, padx=20, pady=10) # Arrange horizontally with padding

        # Frame for Back and Confirm buttons at the bottom
        self.bottom_buttons_frame = tk.Frame(self, bg=self['bg'])
        self.bottom_buttons_frame.pack(side=tk.BOTTOM, fill='x', pady=50) # Position at the bottom, fill horizontally

        # Back Button

        self.back_button = tk.Button(self.bottom_buttons_frame,
                                     text="Back",
                                     font=("Arial", 18),
                                     bg="black",
                                     fg="white",
                                     width=10,
                                     height=2,
                                     command=on_back) # Now calls the provided back_callback
        self.back_button.pack(side=tk.LEFT, padx=(50, 0))

        # Confirm Button
        self.confirm_button = tk.Button(self.bottom_buttons_frame,
                                        text="Confirm",
                                        font=("Arial", 18),
                                        bg="black",
                                        fg="white",
                                        width=10, # Adjust width as needed
                                        height=2, # Adjust height as needed
                                        command=proceed_callback) # Use the provided proceed_callback for Confirm
        self.confirm_button.pack(side=tk.RIGHT, padx=(0, 50)) # Pack to the right with right padding

    def select_emotion(self, emotion):
        """Callback function when an emotion button is pressed."""
        print(f"Emotion selected: {emotion}")
        # Here you can add logic to store the selected emotion or change button appearance


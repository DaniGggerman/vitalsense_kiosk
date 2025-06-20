import tkinter as tk
from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.signup import SignupScreen
from screens.page1 import Page1Screen
from screens.page2 import Page2Screen
from screens.page3 import Page3Screen
from screens.page4 import Page4Screen

class KioskApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.current_screen = None
        self.bind("<Escape>", self.exit_fullscreen) 
        self.show_login()

    def show_login(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = LoginScreen(self, self.show_dashboard, self.show_signup)

    def show_signup(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = SignupScreen(self, self.show_login)

    def show_dashboard(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = DashboardScreen(self, self.show_page1)

    def show_page1(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = Page1Screen(self, self.show_page2)

    def show_page2(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = Page2Screen(self, self.show_page3)

    def show_page3(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = Page3Screen(self, self.show_page4)

    def show_page4(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = Page4Screen(self, self.show_login)

    def exit_fullscreen(self, event=None):
        self.destroy()
    
    def on_close(self):
        self.destroy()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class LoginView:
    def __init__(self):
        self.presenter = None
        self.login_window = tk.Tk()
        self.login_window.title("Login")
        self.login_window.geometry("300x150")

        style = ttk.Style()
        style.theme_use("clam")

        # Contenedor principal
        main_frame = ttk.Frame(self.login_window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Username:").grid(row=0, column=0, sticky="w")
        self.username_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.username_var).grid(row=0, column=1)

        ttk.Label(main_frame, text="Password:").grid(row=1, column=0, sticky="w")
        self.password_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.password_var, show='*').grid(row=1, column=1)

        login_button = ttk.Button(main_frame, text="Login", command=self.on_login_clicked)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def set_presenter(self, presenter):
        self.presenter = presenter

    def get_credentials(self):
        return self.username_var.get(), self.password_var.get()

    def show_error(self, message):
        messagebox.showerror("Login Failed", message)

    def close(self):
        self.login_window.destroy()

    def on_login_clicked(self):
        if self.presenter:
            self.presenter.on_login()

    def run(self):
        self.login_window.mainloop()

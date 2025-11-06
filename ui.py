import functions
from tkinter import *
import tkinter as tk
import random
import ctypes

# Pallet
bg = "White"
contrast = "#1B2198"
contrast_text = "White"
contrast_2 = "#CED1FB"
contrast_2_text = "Black"

font = "Monoton"


class login_window(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.geometry(f"{size[0]}x{size[1]}")
        self.title(title)
        self.resizable(width = False, height = False)
        self.config(bg = bg)

        self.menu = login_frame(self)

        self.mainloop()

class login_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg = bg)

        self.pack(expand = True, fill = "x", padx = 50, pady = 50)

        self.create_widgets()

    def create_widgets(self):
        self.username_text = Label(self, text = "Username:", font = (font, 20, "bold"), bg = bg)
        self.username_entry = Entry(self, font = (font, 15), bg = bg)
        self.password_text = Label(self, text = "Password:", font = (font, 20, "bold"), bg = bg)
        self.password_entry = Entry(self, font = (font, 15), bg = bg)
        self.submit_button = Button(self, text = "Submit", font = (font, 20, "bold"), command = self.__submit, bg = contrast, fg = contrast_text, border = 0)
        self.create_account_button = Button(self, text = "Create Account", font = (font, 20, "bold"), command = lambda : create_account_window("Create New Account", (350, 500)), bg = contrast_2, fg = contrast_2_text, border = 0)
        self.fail_text = Label(self, text = "Your username or password is incorrect.", font = (font, 10), fg = bg, bg = bg)

        self.draw_widgets()
        

    def draw_widgets(self):
        self.rowconfigure((0,1,2,3,4,5,6), weight = 1)
        self.columnconfigure(0, weight = 1)

        self.username_text.grid(row = 0, column = 0, sticky = N+S+W, pady = 5)
        self.username_entry.grid(row = 1, column = 0, sticky = N+S+E+W, pady = 5)
        self.password_text.grid(row = 2, column = 0, sticky = N+S+W, pady = 5)
        self.password_entry.grid(row = 3, column = 0, sticky = N+S+E+W, pady = 5)
        self.submit_button.grid(row = 4, column = 0, sticky = N+S+E+W, pady = 5)
        self.create_account_button.grid(row = 5, column = 0, sticky = N+S+E+W, pady = 5)
        self.fail_text.grid(row = 6, column = 0, sticky = N+S+E+W, pady = 5)

    def __submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        passing = functions.check_password(username, password)

        if passing:
            ctypes.windll.user32.MessageBoxW(0, "Successfully Logged In", "Correct", 1)
            self.fail_text.config(fg = bg)
        else:
            self.fail_text.config(fg = "Red")


class create_account_window(tk.Toplevel):
    def __init__(self, title, size):
        super().__init__()
        self.config(bg = bg)
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(width = False, height = False)

        self.menu = account_frame(self)

        self.mainloop()

class account_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg = bg)

        self.pack(expand = True, fill = "x", padx = 50, pady = 50)

        self.create_widgets()

    def create_widgets(self):
        self.create_username_text = Label(self, text = "Username:", font = (font, 20, "bold"), bg = bg)
        self.create_username_entry = Entry(self, font = (font, 15), bg = bg)
        self.password_text = Label(self, text = "Password:", font = (font, 20, "bold"), bg = bg)
        self.create_password_entry = Entry(self, font = (font, 15), bg = bg)
        self.create_random_pass_button = Button(self, text = "Random Password", font = (font, 20, "bold"), command = self.__random_password, bg = contrast_2, fg = contrast_2_text, border = 0)
        self.create_submit_button = Button(self, text = "Submit", font = (font, 20, "bold"), command = self.__create_account, bg = contrast, fg = contrast_text, border = 0)
        self.create_fail_text = Label(self, text = "That username is already taken.", font = (font, 10), fg = bg, bg = bg)

        self.draw_widgets()

    def draw_widgets(self):
        self.rowconfigure((0,1,2,3,4,5,6), weight = 1)
        self.columnconfigure(0, weight = 1)

        self.create_username_text.grid(row = 0, column = 0, sticky = N+S+W, pady = 5)
        self.create_username_entry.grid(row = 1, column = 0, sticky = N+S+E+W, pady = 5)
        self.password_text.grid(row = 2, column = 0, sticky = N+S+W, pady = 5)
        self.create_password_entry.grid(row = 3, column = 0, sticky = N+S+E+W, pady = 5)
        self.create_random_pass_button.grid(row = 4, column = 0, sticky = N+S+E+W, pady = 5)
        self.create_submit_button.grid(row = 5, column = 0, sticky = N+S+E+W, pady = 5)
        self.create_fail_text.grid(row = 6, column = 0, sticky = N+S+E+W, pady = 5)

    def __create_account(self):
        username = self.create_username_entry.get()
        password = self.create_password_entry.get()

        passing = functions.make_account(username, password)

        if passing:
            self.master.destroy()
        else:
            self.create_fail_text.config(fg = "Red")

    def __random_password(self):
        temp_string = ""

        characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        for i in range(15):
            temp_string = f"{temp_string}{random.choice(characters)}"

        self.create_password_entry.delete(0, END)
        self.create_password_entry.insert(0,temp_string)


login_window("Login", (350, 500))
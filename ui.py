import functions
from tkinter import *

# Pallet
bg = "White"
contrast = "#1B2198"
contrast_text = "White"
contrast_2 = "#CED1FB"
contrast_2_text = "Black"

font = "Monoton"

def submit():
    username = username_entry.get()
    password = password_entry.get()

    passing = functions.check_password(username, password)

    if passing:
        pass
    else:
        fail_text.config(fg = "Red")

def create_account_window():
    global create_username_entry, create_password_entry, create_root, create_fail_text

    create_root = Tk()
    create_root.geometry("350x500")
    create_root.title("Login")
    create_root.resizable(width = False, height = False)
    create_root.config(bg = bg)

    create_frame = Frame(create_root, bg = bg)

    create_frame.rowconfigure(0, weight = 1) # Username label
    create_frame.rowconfigure(1, weight = 1) # Username field
    create_frame.rowconfigure(2, weight = 1) # Password label
    create_frame.rowconfigure(3, weight = 1) # Password field
    create_frame.rowconfigure(4, weight = 1) # Submit button
    create_frame.rowconfigure(5, weight = 1) # Random Password Button
    create_frame.rowconfigure(6, weight = 1) # Fail text

    create_frame.columnconfigure(0, weight = 1)

    # Username label
    create_username_text = Label(create_frame, text = "Username:", font = (font, 20, "bold"), bg = bg)
    create_username_text.grid(row = 0, column = 0, sticky = N+S+W, pady = 5)

    # Username entry
    create_username_entry = Entry(create_frame, font = (font, 15), bg = bg)
    create_username_entry.grid(row = 1, column = 0, sticky = N+S+E+W, pady = 5)

    # Password label
    password_text = Label(create_frame, text = "Password:", font = (font, 20, "bold"), bg = bg)
    password_text.grid(row = 2, column = 0, sticky = N+S+W, pady = 5)

    # Password entry
    create_password_entry = Entry(create_frame, font = (font, 15), bg = bg)
    create_password_entry.grid(row = 3, column = 0, sticky = N+S+E+W, pady = 5)

    # Submit Button
    create_random_pass_button = Button(create_frame, text = "Random Password", font = (font, 20, "bold"), command = random_password, bg = contrast_2, fg = contrast_2_text)
    create_random_pass_button.grid(row = 4, column = 0, sticky = N+S+E+W, pady = 5)

    # Submit Button
    create_submit_button = Button(create_frame, text = "Submit", font = (font, 20, "bold"), command = create_account, bg = contrast, fg = contrast_text)
    create_submit_button.grid(row = 5, column = 0, sticky = N+S+E+W, pady = 5)

    # Fail Label
    create_fail_text = Label(create_frame, text = "That username is already taken.", font = (font, 10), fg = bg, bg = bg)
    create_fail_text.grid(row = 6, column = 0, sticky = N+S+E+W, pady = 5)

    create_frame.pack(expand = True, fill = "x", padx = 50, pady = 50)
    create_root.mainloop()

def random_password():
    pass

def create_account():
    username = create_username_entry.get()
    password = create_password_entry.get()

    passing = functions.make_account(username, password)

    if passing:
        create_root.quit()
    else:
        create_fail_text.config(fg = "Red")

#Make page
root = Tk()
root.geometry("350x500")
root.title("Login")
root.resizable(width = False, height = False)
root.config(bg = bg)

frame = Frame(root, bg = bg)

frame.rowconfigure(0, weight = 1) # Username label
frame.rowconfigure(1, weight = 1) # Username field
frame.rowconfigure(2, weight = 1) # Password label
frame.rowconfigure(3, weight = 1) # Password field
frame.rowconfigure(4, weight = 1) # Submit button
frame.rowconfigure(5, weight = 1) # Create button
frame.rowconfigure(6, weight = 1) # Fail text

frame.columnconfigure(0, weight = 1)

# Username label
username_text = Label(frame, text = "Username:", font = (font, 20, "bold"), bg = bg)
username_text.grid(row = 0, column = 0, sticky = N+S+W, pady = 5)

# Username entry
username_entry = Entry(frame, font = (font, 15), bg = bg)
username_entry.grid(row = 1, column = 0, sticky = N+S+E+W, pady = 5)

# Password label
password_text = Label(frame, text = "Password:", font = (font, 20, "bold"), bg = bg)
password_text.grid(row = 2, column = 0, sticky = N+S+W, pady = 5)

# Password entry
password_entry = Entry(frame, font = (font, 15), bg = bg)
password_entry.grid(row = 3, column = 0, sticky = N+S+E+W, pady = 5)

# Submit Button
submit_button = Button(frame, text = "Submit", font = (font, 20, "bold"), command = submit, bg = contrast, fg = contrast_text)
submit_button.grid(row = 4, column = 0, sticky = N+S+E+W, pady = 5)

# Create Button
submit_button = Button(frame, text = "Create Account", font = (font, 20, "bold"), command = create_account_window, bg = contrast_2, fg = contrast_2_text)
submit_button.grid(row = 5, column = 0, sticky = N+S+E+W, pady = 5)

# Fail Label
fail_text = Label(frame, text = "Your username or password is incorrect.", font = (font, 10), fg = bg, bg = bg)
fail_text.grid(row = 6, column = 0, sticky = N+S+E+W, pady = 5)


frame.pack(expand = True, fill = "x", padx = 50, pady = 50)


root.mainloop()
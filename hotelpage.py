from tkinter import *
from tkinter import messagebox
from login import window

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def show_mainpage():
    clear_window()  
    
    # Add new content for the main page
    welcome_label = Label(window, text="Welcome, you have successfully logged in!", font=("Arial", 16))
    welcome_label.pack(pady=20)
    
    # Example of adding more widgets (you can modify this with actual main page content)
    logout_button = Button(window, text="Logout", font=("Arial", 12), fg="white", bg="red", command=window.quit)
    logout_button.pack(pady=10)

    # Add more widgets as needed
    main_content = Label(window, text="This is the main page. Add your content here.", font=("Arial", 12))
    main_content.pack(pady=10)

    # Update window title to reflect main page
    window.title("Main Page")
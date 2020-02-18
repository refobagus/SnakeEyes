import tkinter as tk
from PIL import ImageTk, Image
import cv2 as cv

"""Creates another window for the owner database"""
def owner_window():
    root3 = tk.Toplevel()

    """Goes to the previous window"""
    def goBackEdit():
        root3.destroy()

    canvas = tk.Canvas(root3, width=330, height=199, bd=0, highlightthickness=0, relief='ridge')
    canvas.create_rectangle(-1,-1,330,199,fill='#1D2733')
    canvas.pack()
    back_button = tk.Button(root3, text=" Back ", command=goBackEdit)
    back_window = canvas.create_window(280, 20, anchor='nw', window=back_button)
    root3.mainloop()

def edit_window():
    root2 = tk.Toplevel()

    """
    This is were the add friend implementation would go
    """
    def add_friend():
        print("added friend")

    """
    This is were the delete friend implementation would go
    """
    def delete_friend():
        print("deleted friend")

    """Go back to the previous window"""
    def goBack():
        root2.destroy()

    """Sets up canvas"""
    canvas = tk.Canvas(root2, width=330, height=199, bd=0, highlightthickness=0, relief='ridge')
    canvas.create_rectangle(-1,-1,330,199,fill='#e9ebed')
    canvas.pack()

    """Sets up Button and the commands"""
    back_button = tk.Button(root2,text=" Back ", command=goBack)
    add_friend = tk.Button(root2, text=" Add Friend ",command=add_friend)
    delete_friend = tk.Button(root2, text="Delete Friend",command=delete_friend)
    owner_settings = tk.Button(root2,text="Owner Settings",command=owner_window)

    """Sets up window for the buttons so it gets put on top of the background """
    back_window = canvas.create_window(280, 20, anchor='nw', window=back_button)
    add_window = canvas.create_window(230, 65, anchor='nw', window=add_friend)
    delete_window = canvas.create_window(230, 100, anchor='nw', window=delete_friend)
    owner_windows = canvas.create_window(220, 130, anchor='nw', window=owner_settings)
    root2.mainloop()


"""Implements start function for the security"""
def start():
    print("Start")

def quit_window():
    startWindow.destroy();


# Color Codes
MYRED = "#F42334"
MYDARKRED = "#e21c2c"
MYBLUE = "#253F51"
MYGRAY = "#e9ebed"
imageLogo = Image.open("SnakeEyes.png")

# Sets up bannar and start window
startWindow = tk.Tk()
#startWindow.iconbitmap("SnakeEyes.ico")
startWindow.configure(background=MYGRAY)
startWindow.title("Welcome to SnakeEyes")
startWindow.resizable(0, 0)
startWindow.image = imageLogo.resize((232, 100), Image.ANTIALIAS)
startWindow.banner = ImageTk.PhotoImage(startWindow.image)
startWindow.bannarCanvas = tk.Canvas(startWindow, width=300, height=120, bg=MYGRAY)
startWindow.bannarCanvas.create_image(0, 0, anchor="nw", image=startWindow.banner)
startWindow.bannarCanvas.grid(rowspan=4, columnspan=7)

# Start Button
startWindow.start_button = tk.Button(startWindow, text="Start", fg=MYRED, bg=MYBLUE, font=("Courier", 12, "bold"), command=start)
startWindow.start_button.grid(row=3, column=2)

# Edit Database button
startWindow.edit_database = tk.Button(startWindow, text="Edit Database", fg=MYRED, bg=MYBLUE, font=("Courier", 12, "bold"), command=edit_window)
startWindow.edit_database.grid(row=3, column=3)


# Quit Program button
startWindow.edit_database = tk.Button(startWindow, text="Quit Program", fg=MYRED, bg=MYBLUE, font=("Courier", 12, "bold"), command=quit_window)
startWindow.edit_database.grid(row=3, column=4)
startWindow.mainloop()


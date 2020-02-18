import tkinter as tk
from tkinter import filedialog
import camera as camera
import Data.person as Data
from PIL import ImageTk, Image


#my rework

#Color Codes
MYRED = "#F42334"
MYDARKRED = "#e21c2c"
MYBLUE = "#253F51"
MYGRAY = "#e9ebed"
imageLogo = Image.open(".\\images\\SnakeEyes.png")

def OpenMain(): #                                           Gal: Main menu code here this function will get called after the registered button is pushed
    def Data():
        MainMenu.destroy()
        OpenDataWindow()
    def start():
        MainMenu.destroy()
        camera.DrawfaceBoxTest1()
    MainMenu= tk.Tk()
    MainMenu.iconbitmap(".\\images\\SnakeEyes.ico")
    MainMenu.configure(background = MYGRAY)
    MainMenu.resizable(0,0)
    #logo
    MainMenu.image = imageLogo.resize((400,172), Image.ANTIALIAS)
    MainMenu.banner = ImageTk.PhotoImage(MainMenu.image)
    MainMenu.bannarCanvas = tk.Canvas(MainMenu, width=400, height=172, bg=MYGRAY)
    MainMenu.bannarCanvas.create_image(0, 0, anchor="nw", image=MainMenu.banner)
    MainMenu.bannarCanvas.grid(row=1, columnspan=3)
    MainMenu.title("SnakeEyes")
    #Main Menu Button# Start Button
    MainMenu.start_button = tk.Button(MainMenu, text="Start System", fg=MYRED, bg=MYBLUE, font=("Courier", 12, "bold"), command=start)
    MainMenu.start_button.grid(row=2, column=0)

    # Edit Database button
    MainMenu.edit_database = tk.Button(MainMenu, text="Edit Database", fg=MYRED, bg=MYBLUE, font=("Courier", 12, "bold"), command=Data)
    MainMenu.edit_database.grid(row=2, column=2)
    MainMenu.mainloop()

def OpenDataWindow():
    def GetPhoto():
        DataWindow.photo_path.set(filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))))
    def main():
        DataWindow.destroy()
        OpenMain()
    def remove():
        if(DataWindow.name_entry.get() == ""):
            DataWindow.Error.configure(text="Error: Please enter a Name from the list")
        if(Data.CurrentUser is None):
            print("No logged in user")
        elif(DataWindow.name_entry.get() == Data.CurrentUser.name):
            DataWindow.Error.configure(text="Error: Cannot delete logged in owner")
        for person in Data.Master:
            if(person.name == DataWindow.name_entry.get()):
                print("found")
                Data.RemoveFromDatabase(person.name)
                DataWindow.Error.configure(text=str(DataWindow.name_entry.get())+" Removed from DataBase")
                resetlist()
                return

    def resetlist():
        count = 1
        DataWindow.list_view.delete(0, tk.END)
        DataWindow.list_view.insert(tk.END, "No.     Status         Name")
        for person in Data.Master:
            DataWindow.list_view.insert(tk.END, str(count)+"       " +person.status +"     "+ person.name)
            count = count + 1


        
    def add():
        if(DataWindow.enter_status.get() == "Owner"):
            if(DataWindow.user_entry.get() == "" or DataWindow.pass_entry.get() == ""):
                DataWindow.Error.configure(text="Owners Need a username and password")
                return
        
        if(DataWindow.name_entry.get() != "" and DataWindow.photo_path.get() != ""):
            Data.AddToDataBase(DataWindow.name_entry.get(), DataWindow.photo_path.get(),DataWindow.enter_status.get(), DataWindow.user_entry.get(), DataWindow.pass_entry.get())
            DataWindow.Error.configure(text=DataWindow.name_entry.get() + "added to database as " + DataWindow.enter_status.get())
            resetlist()
            
        else:
            DataWindow.Error.configure(text="Please fill all relevent fields")
            return

    DataWindow = tk.Tk()
    DataWindow.title("SnakeEyes:DataBase")
    DataWindow.iconbitmap(".\\images\\SnakeEyes.ico")
    #DataWindow.resizable(0,0)
    #DataBase List
    DataWindow.list_scrollbar = tk.Scrollbar(DataWindow, bg=MYBLUE)
    DataWindow.list_view = tk.Listbox(DataWindow, yscrollcommand=DataWindow.list_scrollbar.set, bg=MYGRAY, fg=MYRED, font=("Courier", 12), width = 40)
    DataWindow.list_view.insert(tk.END, "No.     Status     Name")
    count = 1
    for person in Data.Master:
        if(person.status == "Friend"):
            DataWindow.list_view.insert(tk.END, str(count)+"       " +person.status +"     "+ person.name)
        else:
            DataWindow.list_view.insert(tk.END, str(count)+"       " +person.status +"      "+ person.name)
        count = count + 1
    DataWindow.list_view.grid(rowspan = 3, columnspan=5)
    DataWindow.list_scrollbar.configure(command=DataWindow.list_view.yview)
    #other information

    #Username Label
    DataWindow.name_entry_label = tk.Label(DataWindow, text="Name: ", bg=MYGRAY, fg=MYRED,font=("Courier", 12))
    DataWindow.name_entry_label.grid(row=4, column=1)
    #Username Entry Box
    DataWindow.name_entry = tk.Entry(DataWindow, width=40)                        
    DataWindow.name_entry.grid(row=4, column=2, columnspan=2)
    #Username Label
    DataWindow.user_entry_label = tk.Label(DataWindow, text="Username: ", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.user_entry_label.grid(row=5, column=1)
    #Username Entry Box
    DataWindow.user_entry = tk.Entry(DataWindow, width=40)                        
    DataWindow.user_entry.grid(row=5, column=2, columnspan=2)
    #Password Label
    DataWindow.pass_entry_label = tk.Label(DataWindow, text="Password: ", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.pass_entry_label.grid(row=6, column=1)
    #Password Entry Box
    DataWindow.pass_entry = tk.Entry(DataWindow, width=40, show="*")                        
    DataWindow.pass_entry.grid(row=6, column=2, columnspan=2)
    #Password Label
    DataWindow.pass_entry_label2 = tk.Label(DataWindow, text="Confirm Password: ", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.pass_entry_label2.grid(row=7, column=1)
    #Password Entry Box
    DataWindow.pass_entry2 = tk.Entry(DataWindow, width=40, show="*")                        
    DataWindow.pass_entry2.grid(row=7, column=2, columnspan=2)
    #Photo Button
    DataWindow.photo_path = tk.StringVar()
    DataWindow.photo_butt = tk.Button(DataWindow, text="Load Photo", fg=MYRED, bg=MYBLUE, font=("Courier",12, "bold"), command=GetPhoto)
    DataWindow.photo_butt.grid(row=8, column=1)
    #photo Entry Box
    DataWindow.photo_entry = tk.Entry(DataWindow, width=40, textvariable=DataWindow.photo_path)                        
    DataWindow.photo_entry.grid(row=8, column=2, columnspan=2)
    
    
    #Status Label
    DataWindow.status_entry_label = tk.Label(DataWindow, text="Status ", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.status_entry_label.grid(row=9, column=1)
    #Pick Status drop down
    DataWindow.enter_status = tk.StringVar()
    DataWindow.status = {'Owner', 'Friend', 'Enemy'}
    DataWindow.enter_status.set('Owner')
    DataWindow.status_menu = tk.OptionMenu(DataWindow, DataWindow.enter_status, *DataWindow.status)
    DataWindow.status_menu.configure(fg=MYRED, bg=MYBLUE,font=("Courier", 12, "bold"), width=20)
    DataWindow.status_menu.grid(row = 9, column = 2, columnspan=2)

    #space
    DataWindow.Error = tk.Label(DataWindow, text="", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.Error.grid(row=10, columnspan=3)
    
    #add button
    DataWindow.add_butt = tk.Button(DataWindow, text="Add",command=add, fg=MYDARKRED, bg=MYBLUE, font=("Courier",12, "bold"))
    DataWindow.add_butt.grid(row=11, column=1)

    #addbutton Lable
    DataWindow.add_label1 = tk.Label(DataWindow, text="Please Fill all", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.add_label2 = tk.Label(DataWindow, text="relivent fields", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.add_label1.grid(row=12, column=1)
    DataWindow.add_label2.grid(row=13, column=1)

    #remove button
    DataWindow.remove_butt = tk.Button(DataWindow, text="Remove",command=remove, fg=MYDARKRED, bg=MYBLUE, font=("Courier",12, "bold"))
    DataWindow.remove_butt.grid(row=11, column=2)
    
    #remove button lable
    DataWindow.remove_label1 = tk.Label(DataWindow, text="Only Name", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.remove_label2 = tk.Label(DataWindow, text="required", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    DataWindow.remove_label1.grid(row=12, column=2)
    DataWindow.remove_label2.grid(row=13, column=2)

    #Main Menu Button
    DataWindow.Main_butt = tk.Button(DataWindow, text="Main",command=main, fg=MYDARKRED, bg=MYBLUE, font=("Courier",12, "bold"))
    DataWindow.Main_butt.grid(row=11, column=3)

    #start window
    DataWindow.mainloop()

def CameraWindow():
    cameraWindow = tk.Tk()
    cameraWindow.title("SnakeEyes:Camera")
    cameraWindow.geometry("750x500")
    cameraWindow.mainloop()


def OpenLogin():
    def Login():
        loginWindow.withdraw()
        username = loginWindow.user_entry.get()
        password = loginWindow.pass_entry.get()
        print(username + ", " + password)
        if(Data.CheckPassword(username, password)):
            loginWindow.destroy()
            OpenMain()
        else:
            loginWindow.deiconify()

    
    loginWindow = tk.Tk()
    loginWindow.iconbitmap(".\\images\\SnakeEyes.ico")
    loginWindow.configure(background = MYGRAY)
    loginWindow.title("SnakeEyes:Login")
    loginWindow.resizable(0,0)
    #image = Image.open(".\\images\\SnakeEyes.png")
    loginWindow.image = imageLogo.resize((300,129), Image.ANTIALIAS)
    #loginWindow.image = loginWindow.image.resize((300,129), Image.ANTIALIAS)
    loginWindow.banner = ImageTk.PhotoImage(loginWindow.image)
    loginWindow.bannarCanvas = tk.Canvas(loginWindow, width=300, height=129, bg=MYGRAY)
    loginWindow.bannarCanvas.create_image(0, 0, anchor="nw", image=loginWindow.banner)
    loginWindow.bannarCanvas.grid(row=0, columnspan=3)
    #Username Label
    loginWindow.user_entry_label = tk.Label(loginWindow, text="Username: ", bg=MYGRAY, fg=MYRED)
    loginWindow.user_entry_label.grid(row=1, column=1)
    #Username Entry Box
    loginWindow.user_entry = tk.Entry(loginWindow)                        
    loginWindow.user_entry.grid(row=1, column=2)
    #Password Label
    loginWindow.pass_entry_label = tk.Label(loginWindow, text="Password: ", bg=MYGRAY, fg=MYRED)
    loginWindow.pass_entry_label.grid(row=2, column=1)
    #Password Entry Box
    loginWindow.pass_entry = tk.Entry(loginWindow, show="*")                        
    loginWindow.pass_entry.grid(row=2, column=2)
    #Sign In Button
    loginWindow.sign_in_butt = tk.Button(loginWindow, text="Sign In",command=Login, fg=MYDARKRED, bg=MYBLUE)
    loginWindow.sign_in_butt.grid(row=5, column=2)
    loginWindow.mainloop()
    loginWindow.withdraw()


#register window
def OpenRegister():
    def GetPhoto():
        registerWindow.photo_path.set(filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))))

    def Register():
        if(registerWindow.pass_entry.get() != registerWindow.pass_entry2.get()):
            registerWindow.WelcomeText2.configure(text="Passwords didn't match")
            return
        if(registerWindow.name_entry.get() != "" and registerWindow.pass_entry.get() != "" and registerWindow.pass_entry2.get() != "" and registerWindow.user_entry.get() != "" and registerWindow.photo_path.get() != ""):
            registerWindow.withdraw()
            Data.AddToDataBase(registerWindow.name_entry.get(), registerWindow.photo_path.get(), "Owner", registerWindow.user_entry.get(), registerWindow.pass_entry.get())
            Data.CurrentUser = Data.Owners[0]
            registerWindow.destroy()
            OpenMain()
        else:
            registerWindow.WelcomeText2.configure(text="Please fill in all fields")

    registerWindow = tk.Tk()
    registerWindow.iconbitmap(".\\images\\SnakeEyes.ico")
    registerWindow.configure(background = MYGRAY)
    registerWindow.title("Welcome to SnakeEyes")
    registerWindow.resizable(0,0)
    registerWindow.image = imageLogo.resize((500,215), Image.ANTIALIAS)
    registerWindow.banner = ImageTk.PhotoImage(registerWindow.image)
    registerWindow.bannarCanvas = tk.Canvas(registerWindow, width=500, height=215, bg=MYGRAY)
    registerWindow.bannarCanvas.create_image(0, 0, anchor="nw", image=registerWindow.banner)
    registerWindow.bannarCanvas.grid(row=0, columnspan=3)
    #resgister Text
    registerWindow.WelcomeText = tk.Label(registerWindow, text="Welcome to SnakeEyes!", font=("Courier", 20), bg=MYGRAY, fg=MYRED)
    registerWindow.WelcomeText2 = tk.Label(registerWindow, text="Please fill out the following information to register this computer to you.", font=("Courier", 12), bg=MYGRAY, fg=MYRED)
    registerWindow.WelcomeText2.grid(row=2, columnspan=3)
    registerWindow.WelcomeText.grid(row=1, columnspan=3)
    #Username Label
    registerWindow.name_entry_label = tk.Label(registerWindow, text="Name: ", bg=MYGRAY, fg=MYRED,font=("Courier", 12))
    registerWindow.name_entry_label.grid(row=3, column=1)
    #Username Entry Box
    registerWindow.name_entry = tk.Entry(registerWindow, width=40)                        
    registerWindow.name_entry.grid(row=3, column=2)
    #Username Label
    registerWindow.user_entry_label = tk.Label(registerWindow, text="Username: ", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    registerWindow.user_entry_label.grid(row=4, column=1)
    #Username Entry Box
    registerWindow.user_entry = tk.Entry(registerWindow, width=40)                        
    registerWindow.user_entry.grid(row=4, column=2)
    #Password Label
    registerWindow.pass_entry_label = tk.Label(registerWindow, text="Password: ", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    registerWindow.pass_entry_label.grid(row=5, column=1)
    #Password Entry Box
    registerWindow.pass_entry = tk.Entry(registerWindow, width=40, show="*")                        
    registerWindow.pass_entry.grid(row=5, column=2)
    #Password Label
    registerWindow.pass_entry_label2 = tk.Label(registerWindow, text="Confirm Password: ", bg=MYGRAY, fg=MYRED, font=("Courier", 12))
    registerWindow.pass_entry_label2.grid(row=6, column=1)
    #Password Entry Box
    registerWindow.pass_entry2 = tk.Entry(registerWindow, width=40, show="*")                        
    registerWindow.pass_entry2.grid(row=6, column=2)
    #Photo Button
    registerWindow.photo_path = tk.StringVar()
    registerWindow.photo_butt = tk.Button(registerWindow, text="Load Photo", fg=MYRED, bg=MYBLUE, font=("Courier",12, "bold"), command=GetPhoto)
    registerWindow.photo_butt.grid(row=7, column=1)
    #photo Entry Box
    registerWindow.photo_entry = tk.Entry(registerWindow, width=40, textvariable=registerWindow.photo_path)                        
    registerWindow.photo_entry.grid(row=7, column=2)
    #Sign In Button
    registerWindow.sign_in_butt = tk.Button(registerWindow, text="Register", fg=MYRED, bg=MYBLUE, font=("Courier",12, "bold"), command=Register)
    registerWindow.sign_in_butt.grid(row=9, column=2)
    registerWindow.mainloop()
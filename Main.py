import camera
import Data.person as DataBase
import gui_AC as gui



def main():
    DataBase.BuildDataBase()
    if not DataBase.Owners:
        gui.OpenRegister()
    else:
        gui.OpenLogin()
     

if __name__ == "__main__":
    main()
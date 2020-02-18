import face_recognition
import os
from shutil import copyfile

Friends = []
Enemies = []
Owners = []
Master = []
CurrentUser = None

friendsFolder = '.\\Data\\Friends\\'
OwnerFolder = '.\\Data\\Owners\\'
Enemyfolder = '.\\Data\\Enemies\\'

class Person():
   
    def __init__(self, inName, inPhoto, inStatus):
        self.name = inName
        self.photo = inPhoto
        self.status = inStatus
        temp = face_recognition.load_image_file(self.photo)
        self.encode = face_recognition.face_encodings(temp)

class Owner(Person):
    def __init__(self, inName, inPhoto, userName, password):
        Person.__init__(self, inName, inPhoto, "Owner")
        self.password = password
        self.userName = userName
        

class Friend(Person):
     def __init__(self, inName, inPhoto):
        Person.__init__(self, inName, inPhoto, "Friend")


class Enemy(Person):
     def __init__(self, inName, inPhoto):
        Person.__init__(self, inName, inPhoto, "Enemy")


def LoadFriends():
    for files in os.listdir(friendsFolder):
        filename = files
        name = filename.split('.')
        name = name[0]
        Friends.append(Friend(name, (friendsFolder+files)))

def LoadOwners():
    for files in os.listdir(OwnerFolder):
            filename = files
            namelist = filename.split('.')
            name = namelist[0]
            if(namelist[1] == "SE"):
                    continue
            userPass = LoadUserNamePassword(name)
            print(str(userPass[0]) + "," + str(userPass[1]))
            Owners.append(Owner(name, (OwnerFolder + files),str(userPass[0]), str(userPass[1])))

def LoadEnemies():
        for files in os.listdir(Enemyfolder):
                filename = files
                namelist = filename.split('.')
                name = namelist[0]
                Enemies.append(Enemy(name, (Enemyfolder + files)))
                
def BuildDataBase():
        LoadEnemies()
        LoadFriends()
        LoadOwners()
        for person in Owners:
                Master.append(person)
        for person in Friends:
              Master.append(person)
        for person in Enemies:
         Master.append(person)



def AddToDataBase(name, path, status, username = "", password = ""):
        pathtemp = path
        print(pathtemp)
        nameignore, ext = os.path.splitext(pathtemp)
        destination = name + ext
        if(status == "Friend"):
                #copy photo to correct folder
                destination = friendsFolder + destination
                copyfile(path, destination)
                temp = Friend(name, destination)
                Friends.append(temp)
                Master.append(temp)
        elif(status == "Owner"):
                #get username and password
                destination = OwnerFolder + destination
                copyfile(path, destination)
                temp = Owner(name, destination, username, password)
                passFile = OwnerFolder + name + ".SE"
                filestream = open(passFile, "w+")
                filestream.write(username+"\n")
                filestream.write(password+"\n")
                filestream.close()
                Owners.append(temp)
                Master.append(temp)
        elif(status == "Enemy"):
                #copy photo to correct folder
                destination = Enemyfolder + destination
                copyfile(path, destination)
                temp = Enemy(name, destination)
                Enemies.append(temp)
                Master.append(temp)
                
def RemoveFromDatabase(name):
        for person in Master:
                if(person.name == name):
                        if(person.status == "Owner"):
                                seFile = OwnerFolder + person.name + ".SE"
                                os.remove(seFile)
                        os.remove(person.photo)
                        Master.remove(person)
                        if(person.status == "Owner"):
                                Owners.remove(person)
                        elif(person.status == "Friend"):
                                Friends.remove(person)
                        else:
                                Enemies.remove(person)
                        

def CheckPassword(username, password):
        for person in Owners:
                if(person.userName == username):
                        if(person.password == password):
                                global CurrentUser
                                CurrentUser = person
                                return True
                
        return False

def LoadUserNamePassword(Name):
        filename = OwnerFolder + Name + ".SE"
        fStream = open(filename, "r")
        username = fStream.readline()
        password = fStream.readline()
        print(username[:-1] + ", " + password[:-1])
        temp = (username[:-1], password[:-1])
        fStream.close
        return temp
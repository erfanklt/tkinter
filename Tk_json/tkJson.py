# Import required libraries
from tkinter import *
from json import *

# Function to add a new user to the JSON file
def add(name , age):
    with open(r"C:\Users\kalantari\Desktop\tkinter\Tk_json\list.json" , "r") as f:
        data = load(f)
        x = {"name" : name , "age" : age}
        data.append(x)
    with open(r"C:\Users\kalantari\Desktop\tkinter\Tk_json\list.json" , "w") as jf:
        dump(data , jf , indent=4)

# Function to display all users from the JSON file
def show():
    with open(r"C:\Users\kalantari\Desktop\tkinter\Tk_json\list.json" , "r") as f :
        data = load(f)
        txt.delete("1.0" , "end")
        for myDict in data:
            name = myDict["name"]
            age = myDict["age"]
            nameAndAge = name + ":" + age + "\n"
            txt.insert(END , nameAndAge)

# Function to search for a specific user by name
def search(usersname) :
    with open(r"C:\Users\kalantari\Desktop\tkinter\Tk_json\list.json" , "r") as f :
        data = load(f)
        txt.delete("1.0" , "end")
        myUser = []
        myUserLength = 0
        for myDict in data:
            name = myDict["name"]
            if name == usersname:
                name = myDict["name"]
                age = myDict["age"]
                nameAndAge = name + ":" + age + "\n"
                txt.insert(END , nameAndAge)
                myUser.append(name)
                myUserLength = len(myUser)
        if myUserLength == 0:
            txt.insert(END , "user not found!!!")
        
# Create the main window
win = Tk()
win.geometry("600x500")

# Create and place the name input field and label
inp1 = Entry()
inp1.place(x = 200 , y = 10 , width=165)
nameLable1 = Label(text="Name")
nameLable1.place(x = 200 , y = 30)

# Create and place the age input field and label
inp2 = Entry()
inp2.place(x = 200 , y = 60 , width=165)
nameLable2 = Label(text="Age")
nameLable2.place(x = 200 , y = 80)

# Create and place the action buttons (show, search, add)
showBtn = Button(text="show" , width=5 , command= lambda : show())
showBtn.place(x=200 , y=110)
searchBtn = Button(text="search" , width=5 , command= lambda : search(inp1.get()))
searchBtn.place(x=260 , y=110)
addBtn = Button(text="add" , width=5 , command= lambda : add(inp1.get() , inp2.get()))
addBtn.place(x=320 , y=110)

# Create and place the text display area
txt = Text()
txt.place(x=200 , y=150 , width=165 , height=100)

# Start the main event loop
win.mainloop()
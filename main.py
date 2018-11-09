
from tkinter import *
from tkinter import ttk
from github import Github
username = ""
password = ""

def github():
    print("TEST")
    # using username and password
    g = Github(username, password)
    root=Tk()
    root.title("GITHUB API")
    for repo in g.get_user().get_repos():
        theLabel = Label(root, text=repo.name)
        theLabel.pack()

    root.mainloop()

def login():
    gui = Tk()
    gui.geometry("400x400")
    #make sure first is capital and second is not
    gui.title("Github API Login")
    userTxt = Label(gui ,text="username").grid(row=0,column = 0)
    passTxt = Label(gui ,text="password").grid(row=1,column=0)
    username = Entry(gui).grid(row=0,column=1)
    password = Entry(gui).grid(row=1,column=1)

    c = ttk.Button(gui ,text="Submit", command="github").grid(row=2,column=0)
    gui.mainloop()

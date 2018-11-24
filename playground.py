from tkinter import *
from tkinter import ttk
from github import Github
import csv

class Commit(object):
    author = ""
    #insertions = 0
    #deletions = 0
    date = ""


    # The class "constructor" - It's actually an initializer
    def __init__(self, author,date):
        self.author = author
        #self.insertions = insertions
        #self.deletions = deletions
        self.date = date



g = Github("JackDCollins", "@ppl3Inc")
repos =  g.get_user().get_repos()
#print(getLangSkills(g))
#for repo in repos:
repo = g.get_repo("SeanFitz1997/EBII1819--Trinity_Module_Review")
#print(dir(repos))
c = repo.get_commits()

l = list()
for ci in c:
        #print(dir(ci))
        #print(dir(ci.author))
    if ci.author!= None:
        date = ci.commit.author.date
        author = ci.author.login
        commit = Commit(author,date)
        l.append(commit)
        #print(dir(ci))

dict = {}
for c in l :
        if dict.get(c.author) == None:
            dict[c.author] = 1
        else :
            dict[c.author] = dict[c.author]+1

print(dict)

with open('commits.csv', 'w') as csvfile:
    fieldnames = ['name', 'val']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for key, val in dict.items() :
        writer.writerow({'name': key, 'val': val})

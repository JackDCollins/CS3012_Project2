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


def doCommitHistory(github,repos):
    l = list()
    for commit in repos:
        if commit.author!= None:
            date = commit.commit.author.date
            author = commit.author.login
            commitObject = Commit(author,date)
            l.append(commitObject)

    dict = {}
    for commit in l :
            if dict.get(commit.author) == None:
                dict[commit.author] = 1
            else :
                dict[commit.author] = dict[c.author]+1

    with open('commits.csv', 'w') as csvfile:
        fieldnames = ['name', 'val']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key, val in dict.items() :
            writer.writerow({'name': key, 'val': val})



g = Github("b94cfbadca124937e3a619bcc3a90b3c4fb119e0")
repos =  g.get_user().get_repos()
repo = g.get_repo("SeanFitz1997/EBII1819--Trinity_Module_Review")
c = repo.get_commits()
doCommitHistory(g,c)

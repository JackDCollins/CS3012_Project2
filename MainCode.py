from tkinter import *
from tkinter import ttk
from github import Github
import Grapher as gra
import csv

class Commit(object):
    author = ""
    date = ""

    def __init__(self, author,date):
        self.author = author
        self.date = date

class CommitChurn(object):
    author = ""
    insertions=0
    deletions=0
    date = ""

    def __init__(self, author,date,insertions, deletions):
        self.author = author
        self.date = date
        self.insertions = insertions
        self.deletions = deletions



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
                dict[commit.author] = dict[commit.author]+1

    gra.doCommitGraph(dict)

    with open('commits.csv', 'w') as csvfile:
        fieldnames = ['name', 'val']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key, val in dict.items() :
            writer.writerow({'name': key, 'val': val})


def doCodeChurn(github,repos):
    l = list()
    for commit in repos:
        if commit.author!= None:
            date = commit.commit.author.date
            author = commit.author.login
            ins = commit.stats.additions
            dels = commit.stats.deletions
            commitObject = CommitChurn(author,date,ins,dels)
            l.append(commitObject)

    tmp = 0
    dict = {}
    for commit in l :
            change = commit.insertions - commit.deletions
            dict[commit.date] = tmp + change
            tmp = tmp + change


    with open('codechurn.csv', 'w') as csvfile:
        fieldnames = ['date', 'close']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key, val in dict.items() :
            writer.writerow({'date': key.strftime("%m/%d/%y"), 'close': val})



g = Github("b94cfbadca124937e3a619bcc3a90b3c4fb119e0")
#repos =  g.get_user().get_repos()
repo = g.get_repo("SeanFitz1997/EBII1819--Trinity_Module_Review")
c = repo.get_commits()
#doCommitHistory(g,c)
#doCodeChurn(g,c)
doCommitHistory(g,c)

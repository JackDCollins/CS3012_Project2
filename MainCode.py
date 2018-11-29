from tkinter import *
from tkinter import ttk
from github import Github
import Grapher as gra
import csv
import requests
import Contributor as cont




class CommitObject(object):
    author = ""
    insertions=0
    deletions=0
    date = ""

    def __init__(self, author,date,insertions, deletions):
        self.author = author
        self.date = date
        self.insertions = insertions
        self.deletions = deletions

repoList = list()

def doCommitHistory(github,repos):
    l = list()

    if len(repoList) == 0 :
        for commit in repos:
            if commit.author!= None:
                date = commit.commit.author.date
                author = commit.author.login
                ins = commit.stats.additions
                dels = commit.stats.deletions
                commitObject = CommitObject(author,date,ins,dels)
                repoList.append(commitObject)

    l = repoList

    dict = {}
    for commit in l :
            if dict.get(commit.author) == None:
                dict[commit.author] = 1
            else :
                dict[commit.author] = dict[commit.author]+1

    gra.doCommitGraph(dict)

    #with open('commits.csv', 'w') as csvfile:
    #    fieldnames = ['name', 'val']
    #    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #    writer.writeheader()
    #    for key, val in dict.items() :
    #        writer.writerow({'name': key, 'val': val})


def doCodeChurn(github,repos):
    l = list()
    if len(repoList) == 0 :
        for commit in repos:
            if commit.author!= None:
                date = commit.commit.author.date
                author = commit.author.login
                ins = commit.stats.additions
                dels = commit.stats.deletions
                commitObject = CommitObject(author,date,ins,dels)
                repoList.append(commitObject)


    l = repoList
    tmp = 0
    dict = {}

    t = list(reversed(l))
    for commit in t:
            change = commit.insertions - commit.deletions
            dict[commit.date] = tmp + change
            tmp = tmp + change

    gra.doCodeGraph(dict)

    #with open('codechurn.csv', 'w') as csvfile:
    #    fieldnames = ['date', 'close']
    #    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #    writer.writeheader()
    #    for key, val in dict.items() :
    #        writer.writerow({'date': key.strftime("%m/%d/%y"), 'close': val})



g = Github("b94cfbadca124937e3a619bcc3a90b3c4fb119e0")
#repos =  g.get_user().get_repos()
repo = g.get_repo("SeanFitz1997/EBII1819--Trinity_Module_Review")
c = repo.get_commits()
cont.doContributors(g,c,repo)



doCommitHistory(g,c)
doCodeChurn(g,c)
#doCommitHistory(g,c)
#doCodeChurn(g,c)

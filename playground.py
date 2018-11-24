from tkinter import *
from tkinter import ttk
from github import Github
import csv

def getRepoDetails(user):

    if user is None:
        return None

    userDetails = {
        'UserName' : user.get_user().login,
        'Name' : user.get_user().name,
        'Repos' : []
    }

    for repo in user.get_user().get_repos():
        repoDetails = {
            'Name' : repo.name,
            'Toppics' : repo.get_topics(),
            'Branchs' : list(repo.get_branches()),
            'Commits' : list(repo.get_commits()),
            'Collaburators' : list(repo.get_collaborators()),
            'Stars' : repo.stargazers_count
        }
        userDetails['Repos'].append(repoDetails)

    return userDetails


def getLangSkills(user) :

    if user == None:
        return None

    #Map for file extentions to programing language
    proLang = {
        '.ML' :	'ML',
        '.CS' : 'C#',
        '.HPP':	'C++',
        '.CLASS' : 'Java',
        '.CPP' : 'C++',
        '.ERB' : 'Ruby',
        '.CP' : 'C++',
        '.MF' : 'Java',
        '.DMD' : 'SQL',
        '.JAVA' : 'Java',
        '.PY' : 'Python',
        '.RES' : 'C++',
        '.SWIFT' : 'Swift',
        '.ASM' : 'Assembly',
        '.XSD' : 'XML',
        '.RBW' : 'Ruby',
        '.CLW' : 'C++',
        '.NCB' : 'C++',
        '.FSX' : 'F#',
        '.SH' : 'Shell',
        '.C' : 'C',
        '.PL' : 'Perl',
        '.FS' : 'F#',
        '.INO' : 'Arduino',
        '.RPY' : 'Python',
        '.VCPROJ' : 'C++',
        '.HH' :	'C++',
        '.CC' : 'C++',
        '.PYD' : 'Python',
        '.R' : 'R',
        '.APS' : 'C++',
        '.HS' : 'Haskell',
        '.PM' : 'Perl',
        '.PH' : 'Perl',
        '.CSX' : 'Visual C#',
        '.JS' : 'JavaScript',
        '.HTML' : 'HTML',
        '.CSS' : 'CSS',
        '.PHP' : 'PHP'
    }
    userDetails = { 'Name' : 'User',
                    'Total' : 0    }
    userInfo = []
    repos = user.get_user().get_repos()
    for repo in repos:
        repoDetails = { 'Name' : repo.name,
                        'Total' : 0         }
        #Traverse through repo
        contents = repo.get_contents("")
        while len(contents) > 1:
            file_content = contents.pop(0)

            #* Special case to not include bootstrap or jquery lib *
            if re.search(r'bootstrap|jquery|cryptonate', file_content.path, re.IGNORECASE):
                continue

            if file_content.type == 'dir':
                contents.extend(repo.get_contents(file_content.path))
            else:
                #Get file extention
                extention = re.search(r'.+(\..+)$', file_content.name, re.IGNORECASE)
                #If proramming file
                if extention and extention.group(1).upper() in proLang:

                    lang = proLang[extention.group(1).upper()]
                    #Add to user totals
                    userDetails['Total'] += file_content.size
                    if lang in userDetails:
                        userDetails[lang] += file_content.size
                    else:
                        userDetails[lang] = file_content.size
                    #Add to repo totals
                    repoDetails['Total'] += file_content.size
                    if lang in repoDetails:
                        repoDetails[lang] += file_content.size
                    else:
                        repoDetails[lang] = file_content.size

        #Add repo_details to userInfo
        userInfo.append(repoDetails)

    #Add user to start of userInfo
    userInfo = [userDetails] + userInfo
    return userInfo


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

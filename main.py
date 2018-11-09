from github import Github
p = "collinj6@tcd.ie"
u = "@ppl3Inc"






# using username and password
g = Github(p, u)

for repo in g.get_user().get_repos():
    print("%s - %d",repo.name,repo.additions)

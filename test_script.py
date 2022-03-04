import commands

res=commands.add_two_nos(5,8)
print(res)

repo='http://gitlab.zycus.net/gocd-pipelines/cicd/java-maven-app.git'
folder_name = repo.split("/")[-1].split(".")[0]
print(folder_name)
from bs4 import BeautifulSoup
import requests
import pandas

res=requests.get("http://www.first-names-meanings.com/country-indian-names.html")
# print(res.content)

data=BeautifulSoup(res.content,"html.parser")
tds=data.findAll("td")
# print(tds)
names=[each.text for each in tds]
for i in range(len(names)):
    if "\xa0" in names[i]:
        names[i]=names[i][:names[i].index(" ")]
names=names[:-4]
names.insert(0,"aashish")
start=0
end=len(names)
correct=False
csv=pandas.read_csv("male.csv")
csv=csv.dropna()
names=csv["makename"].tolist()
for i in range(len(names)):
    if " " in names[i]:
        names[i]=names[i][:names[i].index(" ")]
for i in range(len(names)):
    for j in range(len(names)-1-i):
        if names[j]>names[j+1]:
            names[j],names[j+1]=names[j+1],names[j]
f=open("datam.txt","w")
for each in names:
    f.write(names+"\n")
# while True:
#     print(input() in names)
while(start<=end):
    mid=(start+end)//2
    print("Name : ",names[mid])
    users=input("Enter 1 if your name is greater.\n 2 if name is smaller.\n 3 if this is your name\n")
    users=int(users)
    if(users==1):
        start=mid+1
    elif(users==2):
        end=mid-1
    elif(users==3):
        print("computer won your name is ",names[mid])
        correct=True
        break
    else:
        print("Enter correct choice")
if not correct:
    print("You won")
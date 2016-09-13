names=[]

while(1):
    r=str(input("Enter name (yes/no) : "))
    r=r[0].lower()

    if r=='y':
        name,last=input("Enter name (firstname lastname) : ").split(" ")
        names.append({"name":name,"last":last})

    else :
        break

print('Following are the names : ')

for i in names:
    print(i["name"],i['last'])
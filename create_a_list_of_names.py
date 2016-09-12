customer=[]

while(1):
    r=str(input("Enter name (yes/no) : "))
    r=r[0].lower()

    if r=='y':
        name,last=input("Enter name (firstname lastname) : ").split(" ")
        customer.append({"name":name,"last":last})

    else :
        break

print('Following are the names : ')

for cust in customer:
    print(cust["name"],cust['last'])

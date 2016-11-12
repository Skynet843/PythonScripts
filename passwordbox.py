import getpass
import os
import sys,pyperclip

# create two files names "pass.txt" and "pass.txt" 

passwords = {}
maspass = " "

if os.stat("pass.txt").st_size == 0:
    print("Enter a master password : ",end="")
    maspass1 = input()
    print("Confirm passowrd: ",end="")
    maspass2 = input()

    if(maspass1==maspass2):
        maspass = maspass1
        p = open("pass.txt",'w')
        p.write("master-"+maspass)

    else:
        print("Password doesn't match Try again.")

if len(sys.argv) <2:
    print("You forget to arguments in command line")
    sys.exit()

p = open("pass.txt")
linep = p.readline()
linenew,pas = linep.split('-')
maspass = pas

f = open("database.txt")
line = f.readline()

if not len(line.strip()) == 0 :
    data = passwords
    with open('database.txt') as raw_data:
        for item in raw_data:
            if ':' in item:
                key,value = item.split(':', 1)
                data[key]=value

if len(sys.argv) <2:
    print("You forget to add arguments in command line")
    sys.exit()

if sys.argv[1]=='add':
    master = getpass.getpass("Enter master password: ")
    if master != maspass:
        print("Wrong passowrd")
        exit()

    while(1):
        print("Enter account: ",end="")
        newacc = input()
        print("Enter password for the account: ",end="")
        newpass = input()
        passwords.update({newacc:newpass})
        print("Do you want to add more(y/n): ",end='')
        passwords.update({newacc:newpass})

        f= open('database.txt', 'w')
        for key, value in passwords.items():
            f.write('%s:%s\n' % (key, value))

        status = input()
        if(status=='y'):
            continue
        else:
            break

else:
    account = sys.argv[1]
    master = getpass.getpass("Enter master password: ")
    if master == maspass:
        if account in passwords:
            pyperclip.copy(passwords[account])
            print("Password for your ",account,"is coppied to clipboard")
        else:
            print("We dont have password for ",account)
    else:
        print("Wrong password")

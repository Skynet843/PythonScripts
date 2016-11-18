import getpass
import os
import sys,pyperclip

# create two files named  'database.txt' and "pass.txt" 

passwords = {}
maspass = " "

def help():
    print("NOTE:Firstly create two files named  \"database.txt\" and \"pass.txt\" in same directory")
    print("add       \t ---  to setup master password(first time users)\n\t\t\t\t\t and add an account")
    print("mchange   \t ---  to change master password")
    print("add       \t ---  to add new account")
    print("del       \t ---  to delete existing account")
    print("mchange   \t ---  to change master password")
    print("update    \t ---  to change password of existing account")


def updatedatabase():
    f= open('database.txt', 'w')
    for key, value in passwords.items():
        f.write('%s:%s\n' % (key, value))


def update(acc):
    print("Enter new password for",acc,": ",end='')
    new = input()
    passwords[acc] = new
    print("Password successfully updated")
    updatedatabase()
    exit()

def deleteaccount(account):
    del passwords[account]
    print("Account successfully deleted")

def changemaster():
    maspass1 = getpass.getpass("Enter a master password : ")
    maspass2 = getpass.getpass("Confirm password: ")

    if(maspass1==maspass2):
        maspass = maspass1
        p = open("pass.txt",'w')
        p.write("master-"+maspass)

    else:
        print("Password doesn't match Try again.")
        exit()

def checkpassfile():
    p = open("pass.txt")
    linep = p.readline()
    linenew,pas = linep.split('-')
    maspass = pas
    return maspass
    
if sys.argv[1]=='--help':
    help()
    exit()

if len(sys.argv) <2:
    print("You forget to add arguments in command line")
    help()
    sys.exit()

if os.stat("pass.txt").st_size == 0:
    changemaster()
    
if sys.argv[1]=='mchange':
    master = getpass.getpass("Enter current master password: ")
    if checkpassfile()==master:
        changemaster()
        print("Password successfully changed")
        exit()
    else:
        print("You entered wrong password")
        exit()

f = open("database.txt")
line = f.readline()

if not len(line.strip()) == 0 :
    with open('database.txt') as raw_data:
        for item in raw_data:
            if ':' in item:
                key,value = item.split(':', 1)
                passwords[key]=value

if sys.argv[1]=='del':
    print("Enter account: ",end='')
    acc = input()
    temp = getpass.getpass("Enter master password: ")
    if temp != checkpassfile():
        print("Wrong password")
        exit()
    deleteaccount(acc)
    updatedatabase()
    exit()

if sys.argv[1]=='update':
    master = getpass.getpass("Enter master password: ")
    if master != checkpassfile():
        print("Wrong password")
        exit()
    acc = input("Enter account: ")
    update(acc)


if sys.argv[1]=='add':
    master = getpass.getpass("Enter master password: ")
    if master != checkpassfile():
        print("Wrong password")
        exit()

    while(1):
        print("Enter account: ",end="")
        newacc = input()
        print("Enter password for the account: ",end="")
        newpass = input()
        passwords.update({newacc:newpass})
        print("Do you want to add more(y/n): ",end='')
        passwords.update({newacc:newpass})
        updatedatabase()
        status = input()
        if(status.lower() == 'y'):
            continue
        else:
            break

else:
    account = sys.argv[1]
    master = getpass.getpass("Enter master password: ")
    if master == checkpassfile():
        if account in passwords:
            pyperclip.copy(passwords[account])
            print("Password for your",account,"is copied to clipboard")
        else:
            print("We don't have password for ",account)
    else:
        print("Wrong password")
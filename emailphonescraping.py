#Intall Following Command
#pip install bs4
#pip install requests
from bs4 import BeautifulSoup
import re
import requests

web_name=input("Please Enter The Name Of Website:")
print("*****************************************************************")
print("Please Choose The Option:")
print("1) Find All Emails")
print("2) Find All Phone Numbers")
ch=input("Enter Your choice:")

f = requests.get(web_name)

s = BeautifulSoup(f.text, 'html.parser')
s = s.get_text()

if ch=="1":
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)
    print('-----------------------------------------------------')
    print()

    if len(emails) == 0:
        print("Sorry, no email address found.")
        print('------------')
        print()
    else:
        count = 1
        for item in emails:
            print(count, ' email address(es) found : ', item)
            count += 1
elif ch=="2":
    phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)

    if len(phone) == 0:
        print ("Sorry, no phone number found.")

        print('------------')
        print ()
    else :
        print('-----------------------------------------------------')
        count = 1
        for item in phone:
            print ( count, ' phone number(s) found : ',item )
            count += 1





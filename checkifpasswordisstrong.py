import re
import sys,pyperclip

try:
	password = sys.argv[1]
	
except:
	password = pyperclip.paste()

i=6
space = re.compile(r'\s')
numeric = re.compile(r'\d')
scharacter = re.compile(r'\W')
upper = re.compile(r'[A-Z]')
low = re.compile(r'[a-z]')

if len(password) < 8 :
	print("Password is too short")
	i-=1

if space.search(password) is not None:
	print("Password should not contain any spaces")
	i-=1

if numeric.search(password) is None:
	print('Your password should contain digits')
	i-=1

if scharacter.search(password) is None or space.search(password) is not None:
	print('Your password should contain special characters')
	i-=1

if upper.search(password) is None:
	print("Your password should contain uppercase leters")
	i-=1

if low.search(password) is None:
	print("Your password should contain lowercase leters")
	i-=1

if i==6:
	print("Strong password")

else:
	print("Password rating : {}/6".format(i))


	

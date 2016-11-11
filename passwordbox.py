passwords = {'website':'4739hrhh3','blog':'1y36y8464t','twitter':'p0poe846'}
maspass = "letmein"

import sys,pyperclip

if len(sys.argv) <2:
	print("You forget to enter account in command line")
	sys.exit()

account = sys.argv[1]

master = input("Enter master password: ")

if master == maspass:
	if account in passwords:
		pyperclip.copy(passwords[account])
		print("Password for your ",account,"is coppied to clipboard")

	else:
		print("We dont have password for ",account)

else:
	print("Wrong password")


	
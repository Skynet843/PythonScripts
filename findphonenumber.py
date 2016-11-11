def ifphonenumber(no):
	if len(no)!= 10:
		return False

	for i in range(len(no)):
		if no[i].isspace():
			return False
			
	try: 
		no = int(no)

	except:
		return False

	return True

mesaage = input()

for i in range(len(mesaage)):
	temp = mesaage[i:i+10]
	if ifphonenumber(temp):
		print("Phone number found :" + temp)








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

message = input()
for i in range(len(message)):
	temp = message[i:i+10]
	if ifphonenumber(temp):
		print("Phone number found :" + temp)








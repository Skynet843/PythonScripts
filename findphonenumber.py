import re

phoneno = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
message = input()
new = phoneno.findall(message)

for i in new:
	print("phone number found : "+i)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printtable(table):
	maxstr = []
	for j in range(len(table)): # to find maximum in each innrer list
		flag = 0
		for i in range(len(table[j])):
			if flag < len(table[j][i]):
				flag = len(table[j][i])

		maxstr.append(flag)


	for li in range(4):
		for i in range(len(tableData)):
			print(tableData[i][li].ljust(maxstr[i]), end =" ") #rjust
		print()

	'''for i in range(len(table[0])):
		for j in range(len(table[i])):
			print(table[j][i].rjust(maxstr[i]),end=' ')
		print('\n',end='')
        // this code deoen't work :(
		'''

printtable(tableData)

'''
Hint: Your code will first have to find the longest
string in each of the inner lists so that the whole column 
can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers.
The printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the number of inner lists in tableData. 
That way, colWidths[0] can store the width of the longest string in tableData[0], 
colWidths[1] can store the width of the longest string in tableData[1], and so on.
You can then find the largest value in the colWidths list to find out what integer
width to pass to the rjust() string method.'''

 

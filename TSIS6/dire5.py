fruits = ['Banana', 'Orange', 'Apple', 'Cherry']
file = open('file.py','w')
for  item in fruits:
	file.write(item+"\n")
file.close()
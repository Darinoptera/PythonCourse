with open ("a.txt", 'r') as file:
    a=file.read()
a.replace('\n','')
a=a.split()
c=[]
for i in range (0,len(a[0])-len(a[1])):
	if a[0][i:i+len(a[1])]==a[1]:
		c.append(i+1)
for i in c:
	print(i,end=' ')	

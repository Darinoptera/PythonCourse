with open ("a.txt", 'r') as file:
    a=file.read()
a.replace('\n','')
a=a.split()
b=[1,1]
for i in range(2,int(a[0])):
	b.append(b[i-2]*int(a[1])+b[i-1])
print(b[int(a[0])-1])

a=[]
i=0
while i!='':
	a.append(int(i))
	for j in range (1,len(a)):
		if int(i)<a[j]:
			print(a[j])
	i=input()

a=input()
if int(a)>0:
	a=list(a)
	s=0
	pr=1
	for i in a:
		s+=int(i)
		pr*=int(i)
	print (s,pr)
else: 
	print('Введите положительное число')

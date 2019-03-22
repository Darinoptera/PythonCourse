a=[]
for i in range(3):
	i=float(input())
	a.append(i)
d=(a[1])*(a[1])-4*a[0]*a[2]
if d<0:
	print('Нет действительных корней:(')
elif d>0:
	d=(d)**0.5
	print((-a[1]-d)/(2*a[0]), (-a[1]+d)/(2*a[0]))
else:
	print(-a[1]/2)

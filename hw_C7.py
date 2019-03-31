from math import *
a=int(input())
b=int(input())
n=int(input())
#функция интеграл arctgx
#интегрируем по Симпсону
I=0
for i in range (1,2*n,2):
    I+=atan(a+((b-a)*i)/(2*n))
I*=4
for i in range(2,2*n-1,2):
    I+=2*atan(a+((b-a)*i)/(2*n))
I+=atan(a)
I+=atan(b)
I*=(b-a)/(6*n)
It=b*atan(b)-a*atan(a)+0.5*log((1+a**2)/(1+b*b))
print('Примерное значение: '+str(round(I,5))+"\n"+"Точное значение: "+str(round(It,5))+"\n"+'Погрешность, %: '+str((fabs(I-It))/It*100))

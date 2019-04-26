a = [int(i) for i in input('Введите последовательность чисел через пробел: ').split()]
b=[]
for i in range (1,len(a)):
    if a[i-1]<a[i]:
        b.append(a[i])
print(b)

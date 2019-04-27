def prosto(start, end):
    current = start
    while current <= end:
        s=0
        for i in range(1,current):
           if current%i==0:
               s+=1
        if s==1:
            yield current
        current +=1
for number in prosto(int(input('Введите через enter интервал для простых чисел: ')), int(input())):
    print(number, end=' ')

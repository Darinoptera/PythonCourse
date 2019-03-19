import random
a=random.randint(1,100)
i=int(input())
while i!=a:
    if i<a:
        print(str(i)+' меньше, чем загаданное число')
    else:
        print(str(i)+' больше, чем загаданное число')
    i=int(input())
print('Угадали:)')

with open ("a.txt", 'r') as file:
    a=file.readlines(0)
out=0
a=list(a)
b=list(a[1])
a=list(a[0])
a.pop()
for i in range (len(a)):
    if a[i]!=b[i]:
        out+=1
with open ("b.txt", 'w') as file:
    file.write(str(out))

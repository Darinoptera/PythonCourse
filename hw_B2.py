with open ("a.txt", 'r') as file:
    a=file.read()
a=list(a)
b=a[::-1]
out=[]
for i in b:
    if i=="A":
        out.append("T")
    elif i=="T":
        out.append('A')
    elif i=="G":
        out.append('C')
    else:
        out.append("G")
end=''.join(out)
with open ("b.txt", 'w') as file:
    file.write(end)

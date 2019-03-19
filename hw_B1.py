with open ("a.txt", 'r') as file:
    a=file.read()
out=a.replace("T","U")
with open ("b.txt", 'w') as file:
    file.write(out)

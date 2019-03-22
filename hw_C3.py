s=input()
for j in '.',',',':','?','!',' -',';':
	s=s.replace(j,'')
s=s.split()
for i in range(len(s)):
	s[i]=int(len(s[i]))
print(min(s))

import re
f1=open('access.log')
s=[]
i=-1
j=0
for line in f1.readlines():
	a=re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line)
	i=1
	for w in a:
		s.insert(i,w)
		i=i+1 
sx=[]
for i in range(0,len(s)):
	a=re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.)',s[i])
	j=1
	for w in a:
		sx.insert(j,w)
		j=j+1 						
sx=list(set(sx))
group={}
k=0
for i in range(0,len(sx)):
	print()
	for j in range(0,len(s)):
		if s[j].find(sx[i])!=-1:
			group[i,k]=s[j]
			print(group[i,k])
			k=k+1

	
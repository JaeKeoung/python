
s1=0
s2=0
n1=5
n2=13
while n1<=n2:
	s1=s1+n1
	n1+=1
	if n1%3==0:
		s2=s2+(n1*n1)
print (s1,s2)

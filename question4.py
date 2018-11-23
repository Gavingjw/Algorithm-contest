a=[1,9,10,5,11,2,13]  #imput 
c=[]
s=[1]*len(a)
for i in range(1,len(a)):
	b=[]
	for j in range(i):

		if a[j] < a[i] and s[j]+1 > s[i]:
			s[i]=s[j]+1
			b.append(a[j])
		print('i:',i,'j:',j,'s[i]',s[i],'s[j]',s[j],a[j] < a[i],s[j]+1 > s[j])
	c.append(b+[a[i]])
print('the max lenght subqueue:',max(s),' and it is ',c[-1])

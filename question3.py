def FBLQ1(n): # method 1
	'n is input vary'
	if n<=2:
		return 1
	else:
		return FBLQ(n-1)+FBLQ(n-2)

def FBLQ2(n): #method 2
	a=[0]*n
	for i in range(1,n):
		if i is 1 or i is 2:
			a[i]=1
		elif i >2:
			a[i]=a[i-1]+a[i-2]
	return a

if __name__ == '__main__':
	n=100

	if n<1:
		print('input error ,please input again !')
	else:
		print('n=',n,FBLQ2(n))
		'''
		for i in range(1,n):
			print('i=',i, FBLQ(i))
		'''
		pass

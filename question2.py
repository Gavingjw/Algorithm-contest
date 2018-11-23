from sympy import *
def huayuan(b):
	return [str(b),int(b)][int(b)==b]
def compute(m,n):
	'm:foots n:heads'
	if m<0 or n<0:
		print('The input Error, please inpur again')
		return False

	x,y,z=symbols('x,y,z')
	z=solve([x+y-n,2*x+4*y-m],[x,y])
	if z[x]<0 or z[y]<0 or (not isinstance(huayuan(z[x]),int))or not (isinstance(huayuan(z[y]),int)):
		print('NO ANSWER')
		print(z,huayuan(z[x]),huayuan(z[y]))
		pass
	else:
		return z
if __name__ == '__main__':
	#m=input('m')
	#n=input('n')
	m=5  # m is the sum foots of habits and chicken

	n=2  # n is the sum heads of habits and chicken 
	print(compute(m,n))

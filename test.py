#3个空瓶=1瓶汽水
#5罐汽水。5+5%3+3*5/
#
def drink(a=0,b=0,c=0):
	'a为水瓶，b为空瓶,c喝了几瓶水'
	drinkafter=a# a 为喝完的水瓶
	unwaterbottle=drinkafter+b  #leave behind bottle
	if unwaterbottle <2:
		return (0,unwaterbottle,c+drinkafter)
	elif unwaterbottle is 2:
		return(1,0,c+drinkafter+1)
	else:
		buybottle=int(unwaterbottle/3)  #  buy water
		leaveunwbottle=unwaterbottle%3   
		return drink(buybottle,unwaterbottle%3,c+drinkafter)
 
print([drink(b=a) for a in range(1,81)])

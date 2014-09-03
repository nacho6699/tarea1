def suma(a,b):
	c=int(a)
	d=int(b)
	sum=c+d
	print sum

def suma2(a,b):
	c=str(a)
	d=str(b)
	print c+d

def suma3(a,b):
	print a+b

print "inserte el inciso entre a-f"
dato=raw_input()
if dato=='a':
	lista=range(1,21)
	print lista
elif dato=='b':
	lista=range(1,21)
	i=1
	while i< 21:
		print lista[20-i],
		i=i+1
elif dato=='c':
	 suma('20','10')
elif dato=='d':
	 suma2(20,10)
elif dato=='e':
	 suma3(20,0.5) 
raw_input()


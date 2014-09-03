
print "inserte rango incial"
a=int(raw_input())
print "inserte rango final"
b=int(raw_input())
lista=range(a,b+1)
i=1
while i< 21:
	if lista[i-1]%2==0:
		lista2[i-1]=lista[i-1]
		i=i+1
	else:
		i=i+1	
print lista
print lista2
raw_input()
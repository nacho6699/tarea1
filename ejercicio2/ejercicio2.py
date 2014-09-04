
print "inserte rango incial"
a=int(raw_input())
print "inserte rango final"
b=int(raw_input())
lista=range(a,b+1)

for i in lista:
	if lista[i]%2==0:
		lista2[i]=lista[i]
		
print lista
print lista2
raw_input()
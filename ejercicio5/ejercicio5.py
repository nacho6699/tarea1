import re
print "inserta frace"
lista=raw_input()
lista2=re.sub("\D", "", lista)	

print "letras :"+str (len(lista)-len(lista2))
print "numeros :"+str (len(lista2))
raw_input() 
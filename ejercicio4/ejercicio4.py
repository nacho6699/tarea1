def ValorCadena(cadena1,cadena2):
	if len(cadena1)>len(cadena2):
		print cadena1
	elif len(cadena1)<len(cadena2):
		print cadena2
	else:
		print cadena1+cadena2

print "inserta primera cadena"
a=raw_input()
print "inserta segunda cadena"
b=raw_input()
ValorCadena(a,b)
raw_input()					
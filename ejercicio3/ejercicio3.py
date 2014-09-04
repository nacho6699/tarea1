def es_palindromo(a):
	b=a[::-1]
	if a==b:
		print True
	else:
		print False	

print "inserte palabra"
n=raw_input()
es_palindromo(n)
raw_input()	
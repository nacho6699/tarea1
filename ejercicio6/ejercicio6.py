print "intro nro"
n=int(raw_input())
i=1
j=1
while i<=n:
    
	while j<=i:
		print i,
		j=j+1
	
	print ""
	print ""
	if i==n:
		j=1
		while j<=i:
			while i!=0:
				print i-1,
				i=i-1
			j=j+1
		break	

	j=1	
	i=i+1

	
raw_input()
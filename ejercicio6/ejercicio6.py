print "intro nro"
n=int(raw_input())
i=1
j=1
while i<=n:
    
	while j<=i:
		print i,
		j=j+1
	
	
	if i==n:
		while i!=0:
    
			while j<=i:
				print i,
				j=j+1
	
			print ""
			print ""
	
			j=1	
			i=i-1	
	 	break
	print ""
	print ""	
	j=1	
	i=i+1

	
raw_input()
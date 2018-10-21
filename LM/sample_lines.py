import sys,random
line_count=0
with open(sys.argv[1]) as f:
    for line_count,line in enumerate(f):
        pass
    indices=set(random.sample(range(line_count), int(sys.argv[2])))
	#print (indices)
    f.seek(0)
    for i,line in enumerate(f):
        #print (i)
        #if i%10000==0:
         #   print (i)
        if i in indices:
            #print (i)
            print (line,end='')
		

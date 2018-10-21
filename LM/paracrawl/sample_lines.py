#/usr/bin/env python3
import sys,random
if len(sys.argv)!=3:
    sys.stderr.write("Randomly samples NUMBER_OF_LINES from a file a prints them to stdout. \nUsage: ./{} FILE NUMBER_OF_LINES\n".format(sys.argv[0]))
    exit(-1)
with open(sys.argv[1]) as f:
    for line_count,line in enumerate(f):
        pass
    indices=set(random.sample(range(line_count), int(sys.argv[2])))
    f.seek(0)
    for i,line in enumerate(f):
        if i in indices:
            print (line,end='')
		

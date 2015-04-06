import sys,getopt

inputfile=''
outputfile=''
try:
	myopt,args=getopt.getopt(sys.argv[1:],"i:o:")
        print myopt
except getopt.GetoptError as e:
	print str(e)
	print "Usage: %s -i input -o output"%sys.argv[0]
        sys.exit(2)

for o,a in myopt:
	if o=='-i':
		inputfile=a
	else:
		outputfile=a

print "Your command is \n %s -i %s -o %s"%(sys.argv[0],inputfile,outputfile)


import sys,getopt
# store input and output filename

ifile=''
ofile=''

myopt,args=getopt.getopt(sys.argv[1:],"i:o:")
print myopt

for o,a in myopt:
	if o=="-i":
		ifile=a
	elif o=="-o":
		ofile=a
	else:
		print "Usage -i input -o output"
print "%s -i %s -o %s"%(sys.argv[0],ifile,ofile)


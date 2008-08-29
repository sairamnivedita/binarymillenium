import math
import array
import csv
import sys
import operator
import os

def checkfloats(fbin):
	for i in range(3):
		if not((abs(fbin[i]) > 1e-10) and (abs(fbin[i]) < 1e10)): return False
	
	return True;



fraw = open(sys.argv[1]) 

filesize= os.path.getsize(sys.argv[1])

bsize = 14
offset = filesize - (int(filesize/bsize) -1)*bsize


bin = array.array('B')

#bin.byteswap()

#fout = open(outname,'wb')

# print the header
bin = array.array('B')
bin.fromfile(fraw, offset) # 15)
#for j in range(15):
#	sys.stdout.write(str(bin[j]) + '\t')
#print('\n');				


fbin = array.array('f')
fbin.fromfile(fraw, 3)

bin = array.array('H')
bin.fromfile(fraw, 1)

count = 0;
while(True): 
	#sys.stdout.write(str(count) + ',\t')

	fbin.byteswap()

	# in multipart files the header is very huge, I'm not sure how to parse it
	# but I do know that it generates bad floats, so just screen for bad floats:

	if checkfloats(fbin):
		for j in range(3):
			sys.stdout.write(str(fbin[j]) + ',\t')
	
		bin.byteswap()
		red = 	(bin[0] >> 11) & 0x1f
		green = (bin[0] >> 6)  & 0x1f
		blue =  (bin[0] >> 0)  & 0x1f
		
		sys.stdout.write( str(red) + ',\t' + str(green) + ',\t' + str(blue) )	

	#	sys.stdout.write("%#x \t" % v1)
	#	sys.stdout.write("%#x \t" % v2)
		sys.stdout.write('\n')

	fbin = array.array('f')

	try:
		fbin.fromfile(fraw, 3)
	except: 
		break

	bin = array.array('H')
	bin.fromfile(fraw, 1)

	count = count+1
	

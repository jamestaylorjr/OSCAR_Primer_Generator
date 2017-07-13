
def getSequence(numbers, contents):
        sequences = []
        #get number of sequences
        seqnumber = len(numbers)
        
        #compile sequence into one variable
        b = 0
        while(b < seqnumber):
                c = numbers[b]
                lines = []
                try:
                        while(c < numbers[b+1]):
                                if contents[c].startswith(">"):
                                        c = c+1
                                else:
                                        lines.append(contents[c])
                                        c = c+1
                except IndexError as exception:
                        while(c < len(contents)):
                                lines.append(contents[c])
                                c = c+1

 
                b = b+1
                newseq = "".join(lines)
                clean = newseq.strip('\n')
 		sequences.append(clean)
	return sequences

def getFasta():
	filename = raw_input("What is the file path? \n")
	try:
		f1 = open(filename,'r')
	except OSError as e:
		if e.errno == errno.ENOENT:
			print("Wrong file or file path")
		else:
			raise

	test = f1.readlines()

	a = 0
	numbers = []
	names = []
	outName = []
	while(a < len(test)):
		if test[a].startswith('>'):
			names.append(test[a])
			a = a+1
			numbers.append(a)
			
		else:
			a = a+1
			
	sequences = getSequence(numbers,test)
	output = zip(names,sequences)
	return output


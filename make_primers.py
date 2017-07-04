from fasta import *


primers = getFasta()

a = 0
newPrimers = []
while(a < len(primers)):
	if "5fF" in primers[a][0]:
		primer = "GGGGACAGCTTTCTTGTACAAAGTGGAA"+primers[a][1]
		fixed = [primers[a][0],primer]
		newPrimers.append(fixed)
	elif "5fR" in primers[a][0]:
                primer = "GGGGACTGCTTTTTTGTACAAACTTGT"+primers[a][1]
                fixed = [primers[a][0],primer]
                newPrimers.append(fixed)
	elif "3fF" in primers[a][0]:
                primer = "GGGGACAACTTTGTATAGAAAAGTTGTTT"+primers[a][1]
                fixed = [primers[a][0],primer]
                newPrimers.append(fixed)
	elif "3fR" in primers[a][0]:
                primer = "GGGGACAACTTTGTATAATAAAGTTGT"+primers[a][1]
                fixed = [primers[a][0],primer]
                newPrimers.append(fixed)
	else:
		print("Error with " + primers[a][0])
		print("One or more of your primers is not named correctly. Please use the standard naming scheme.")

	a = a+1

output = raw_input("Please name your complete primer file. Ex: output.fasta \n")

target = open(output, 'w')

for item in newPrimers:
	print>>target, item[0]
	print>>target, item[1]
	print>>target, "\n"

target.close()
print("Primers printed to " + output + " in fasta format.")

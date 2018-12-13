import sys
# COMMAND: python errorHandler.py 'similarityThreshold' 'windowSize' 'InputPos(file)'
# INPUT: Pathway to text based files.
# OUTPUT: Boolean. 0 = good to go, 1 = system abort.

def WriteToFile(fileName,PacBioRead):
	f=open(fileName, "a+")
	f.write(PacBioRead)
	f.close()
	return None

def main():
	check = 0
	score = float(sys.argv[1])
	window = int(sys.argv[2])
	inputPos = sys.argv[3]

	necSet = ['A','T','C','G']
	f = open(inputPos)
	Refline = f.readline()
	line = Refline
	if "\t" not in line:
		ReftmpRead = Refline.split(' ')
	else:
		ReftmpRead = Refline.split('\t')
	Refpos = ReftmpRead[0].split(':')
	#print (ReftmpRead)
	check = 1
	Refnec = ReftmpRead[1].split()
	for n in necSet:
		if Refnec[0] == n:
			check = 0
			break
	if check == 1:
		print("System aborted: Not correct alternative neculotide: neculotide should be captial A,T,C or G \n")
	if int(Refpos[1]) < 0:
		print("System aborted: chromosome position should be positive value\n")
		check = 1
	if score > 1.0 or score < 0.0:
		print("System aborted: similiarity threshold value not within the range of 0 to 1\n")
		check = 1
	if window < 1:
		print("System aborted: window size below 1\n")
		check = 1
	#print(nec[0])
	#print(pos)
	#print(tmpRead)
	#print(line)
	while line and check == 0:
		line = f.readline()
		if "\t" not in line:
			tmpRead = line.split(' ')
		else:
			tmpRead = line.split('\t')
		if line == '':
			break
		pos = tmpRead[0].split(':')
		nec = tmpRead[1].split()
		#print(nec)
		check = 1
		for n in necSet:
			if nec[0] == n:
				check = 0
				#print("correct")
				break
		if check == 1:
			print("System aborted: Not correct alternative neculotide: neculotide should be captial A,T,C or G \n")
		if pos[0] != Refpos[0]:
			print("System aborted: Not the same chromosome names in the list\n")
			check = 1
			break
		if int(pos[1]) < 0:
			print("System aborted: chromosome position should be positive value \n")
			check = 1
			break
	f.close()
	print(check)
	return
main()

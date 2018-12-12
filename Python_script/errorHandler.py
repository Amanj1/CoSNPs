import sys
# COMMAND: python errorHandler.py 'scoreValue' 'windowSize' 'InputPos' 
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
	ReftmpRead = Refline.split(' ')
	Refpos = ReftmpRead[0].split(':')
	Refnec = ReftmpRead[1].split()
	for n in necSet:
		if Refnec[0] == n:
			check = 0
			break
	if int(Refpos[1]) < 0:
		print("System aborted: \n")
		check = 1
	if score > 1.0 or score < 0.0:
		print("System aborted: score value not within the range of 0 to 1\n")
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
		tmpRead = line.split(' ')
		if line == '':
			break
		pos = tmpRead[0].split(':')
		nec = tmpRead[1].split()
		print(nec)
		check = 1
		for n in necSet:
			if nec[0] == n:
				check = 0
				print("correct")
				break
		if check == 1:
			print("System aborted: nec \n")
		if pos[0] != Refpos[0]:
			print("System aborted: \n")
			check = 1
			break
		if int(pos[1]) < 0:
			print("System aborted: \n")
			check = 1
			break		
	f.close()
	print(check)
	return
main()

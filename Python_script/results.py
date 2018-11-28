import sys
# COMMAND: python results.py 'secondFilteredBlasrFile' 'OutputFile'
# INPUT: Pathway to text based files.
# OUTPUT: Table representation
Alt = 0
Ref = 0

def WriteToFile(PacBio):
	f=open(sys.argv[2], "a+")
	f.write(PacBio)
	f.close()
	return None

def CheckMutation(PacBioRead):
	tmpMutation = []
	name = ''
	for x in PacBioRead:
		y = x.split('\t')
		name = y[7]
		tmpMutation.append(y[0])
		#if int(y[0]) == 1:
			#Alt = Alt + 1
		#else:
			#Ref = Ref + 1
	for n in tmpMutation:
		name = name + '\t' +n
	name = name + '\n'
	return name

def main():
	tmpRead = []
	currContent = []
	tmpLine = []
	tmpCounter = 0
	f = open(sys.argv[1])
	line = f.readline()
	prevline = line
	tmpRead = line.split('\t')
	#print(tmpRead)
	while line:
		line = f.readline()
		currContent = line.split('\t')
		if line == '':
			tmpLine.append(prevline)
			stringName = CheckMutation(tmpLine)
			WriteToFile(stringName)
			print(tmpLine)
			print('\n')
			tmpLine = []
			tmpRead = currContent
			prevline = line
			break
		if currContent[7] == tmpRead[7]:
			tmpLine.append(prevline)
			tmpRead = currContent
			prevline = line
		if currContent[7] != tmpRead[7]:
			tmpLine.append(prevline)
			stringName = CheckMutation(tmpLine)
			WriteToFile(stringName)
			print(tmpLine)
			print('\n')
			tmpLine = []
			tmpRead = currContent
			prevline = line
	f.close()
	#print(Alt)
	#print(Ref)
	return
main()

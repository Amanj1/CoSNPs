import sys
# COMMAND: python Filter_Blasr.py 'NumberOfSNPs' 'BlasrResults' 'OutputFileNameAndPAthWay' 'InputForFilter'
# INPUT: Pathway to text based files.
# OUTPUT: Saves only data that contains all SNP positions and avoids bad data.

def WriteToFile(fileName,arrPacBio):
	f=open(fileName, "a+")
	for x in arrPacBio:
		f.write(x)
	f.close()
	return None

def CheckMiniMatch(PacBioRead, score):
	check = 1
	x = float(PacBioRead[2])
	y = float(PacBioRead[13])
	#print (x)
	#print (y)
	val = y/x
	#set as user input
	#if float(val) < score:
		#print(float(sys.argv[4]))
	#	check = 0
	return check

def main():
	score = float(sys.argv[4])
	tmpRead = []
	finalTmp = []
	currContent = []
	tmpLine = []
	tmpCounter = 0
	f = open(sys.argv[2])
	line = f.readline()
	prevline = line
	tmpRead = line.split('\t')
	FileName = sys.argv[3]
	numOfPos = int(sys.argv[1])
	while line:
		line = f.readline()
		currContent = line.split('\t')
		#print(currContent)
		if line == '' and CheckMiniMatch(tmpRead, score)==1:
			if tmpCounter == numOfPos-1:
				tmpCounter = 0
				tmpLine.append(prevline)
				WriteToFile(FileName,tmpLine)
			break
		elif line == '':
			print ('empty line for second filter')
			break
		elif currContent[7] == tmpRead[7] and CheckMiniMatch(tmpRead, score)==1:
			tmpCounter = tmpCounter + 1
			tmpLine.append(prevline)
			tmpRead = currContent
			prevline = line
		elif currContent[7] != tmpRead[7] and CheckMiniMatch(tmpRead, score)==1:
			if tmpCounter == numOfPos-1:
				tmpCounter = 0
				tmpLine.append(prevline)
				WriteToFile(FileName,tmpLine)
				tmpLine = []
			tmpRead = currContent
			prevline = line
		else:
			tmpRead = currContent
			prevline = line
			tmpCounter = 0
			tmpLine = []
			if currContent == ['']: #If next line is empty store current
				break
	f.close()

	return
main()

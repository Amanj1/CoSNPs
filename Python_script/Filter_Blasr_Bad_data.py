import sys
# COMMAND: python Filter_Blasr.py 'NumberOfSNPs' 'BlasrResults' 'OutputFileNameAndPAthWay'
# INPUT: Pathway to text based files.
# OUTPUT: Saves only data that contains all SNP positions and avoids bad data.

def WriteToFile(fileName,arrPacBio): 
	f=open(fileName, "a+")
	for x in arrPacBio:
		f.write(x)
	f.close()
	return None

def CheckMiniMatch(PacBioRead):
	check = 1
	x = PacBioRead[2]
	y = PacBioRead[13]
	val = y/x
	if val < 0.8:
		check = 0
	return check

def main():
	tmpRead = []
	finalTmp = []
	currContent = []
	tmpLine = []
	tmpCounter = 0
	f = open(sys.argv[2])
	line = f.readline()
	line = line.strip()
	prevline = line
	tmpRead = line.split(' ')
	FileName = sys.argv[3]
	numOfPos = sys.argv[1]
	while line:
		line = line.strip()
		line = f.readline()
		currContent = line.split(' ')
		
		if currContent == [' '] and CheckMiniMatch(tmpRead)==1:
			if tmpCounter == numOfPos-1:
				tmpCounter = 0
				tmpLine.append(prevline)
				WriteToFile(FileName,tmpLine)
			break
		if currContent[7] == tmpRead[7] and CheckMiniMatch(tmpRead)==1:
			tmpCounter = tmpCounter + 1
			tmpLine.append(prevline)
			tmpRead = currContent
			prevline = line
		elif currContent[6] != tmpRead[6] and CheckMiniMatch(tmpRead)==1:
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

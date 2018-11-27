import sys
# COMMAND: python Filter_Blasr.py 'BlasrResults' 'OutputFileNameAndPAthWay'
# INPUT: Pathway to text based files.
# OUTPUT: New file containing filtered PacBio Reads based on nMatch score and ccomparing Ref and Alt score greedy algorithm

def WriteToFile(fileName,arrPacBio): 
	#refSeq = refSeq+'\n'
	Read = arrPacBio[0]
	f=open(fileName, "a+")
	leng= len(arrPacBio)-1
	for i in range(leng):
		Read = Read + '\t' + arrPacBio[i+1]
	f.write(Read)
	f.close()
	return None

def CheckAlt(RefQuery, AltQuery):
	check = 0
	stR = ''
	if "Alt" in AltQuery:
		stR = AltQuery.replace("Alt", "Ref")
		if stR == RefQuery:
			check = 1
	return check

def CheckMutation(PacBioRead):
	check = 0
	stR = ''
	if "Alt" in PacBioRead[0]:
		check = 1
	check = str(check)
	PacBioRead = [check] + PacBioRead[:]
	return PacBioRead

def main():
	tmpRead = []
	finalTmp = []
	currContent = []
	f = open(sys.argv[1])
	line = f.readline()
	#line = line.strip()
	tmpRead = line.split(' ')
	FileName = sys.argv[2]
	while line:
		line = line.strip()
		line = f.readline()
		currContent = line.split(' ')
		
		if currContent == ['']: #If next line is empty store current
			finalTmp = CheckMutation(tmpRead)
			WriteToFile(FileName,finalTmp)
			break
		if currContent[0] == tmpRead[0] and currContent[6] == tmpRead[6]:
			#print(tmpRead[12])
			if int(currContent[12]) > int(tmpRead[12]):
				tmpRead = currContent
		elif CheckAlt(tmpRead[0],currContent[0]) == 1 and currContent[6] == tmpRead[6]:
			if int(currContent[12]) > int(tmpRead[12]):
				tmpRead = currContent
		elif CheckAlt(tmpRead[0],currContent[0]) == 0 and currContent[6] == tmpRead[6]:
			finalTmp = CheckMutation(tmpRead)
			WriteToFile(FileName,finalTmp)
			tmpRead = currContent
		elif currContent[6] != tmpRead[6]:
			finalTmp = CheckMutation(tmpRead)
			WriteToFile(FileName,finalTmp)
			tmpRead = currContent
			
	f.close()	

	return
main()

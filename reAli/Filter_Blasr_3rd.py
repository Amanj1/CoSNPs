#!/usr/bin/python
import sys
# COMMAND: python Filter_Blasr_3rd.py '2ndFilterOutput' 'OutputFileNameFor3rdFilter'
# INPUT: Pathway to text based files.
# OUTPUT: If nMatch are equal in then Mutation equal to '*'

def WriteToFile(fileName,PacBioRead):
	f=open(fileName, "a+")
	f.write(PacBioRead)
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

def genNewString(arrPacBio):
	str1 = ''
	#if nMatch is equal in both ref and alt sequence
	for x in range(len(arrPacBio)):
		if x == 0:
			str1 = str1 + '*'
		else:
			str1 = str1 + arrPacBio[x]
	return str1

def main():
	tmpRead = []
	finalTmp = []
	currContent = []
	tmpLine = []
	tmpCounter = 0
	f = open(sys.argv[1])
	line = f.readline()
	prevline = line
	tmpRead = line.split('\t')
	FileName = sys.argv[2]

	line = f.readline()
	currContent = line.split('\t')
	while line:

		if currContent[7] == tmpRead[7]:
			if CheckAlt(tmpRead[1],currContent[1]) == 1:
				if tmpRead[13] < currContent[13]:
					WriteToFile(FileName,line)
					line = f.readline()
					prevline = line
					tmpRead = line.split('\t')
					line = f.readline()
					currContent = line.split('\t')
				elif tmpRead[13] == currContent[13]:
					prevline = genNewString(line)
					WriteToFile(FileName,prevline)
					line = f.readline()
					prevline = line
					tmpRead = line.split('\t')
					line = f.readline()
					currContent = line.split('\t')
				elif tmpRead[13] > currContent[13]:
					WriteToFile(FileName,prevline)
					line = f.readline()
					prevline = line
					tmpRead = line.split('\t')
					line = f.readline()
					currContent = line.split('\t')
			else:
				WriteToFile(FileName,prevline)
				prevline = line
				tmpRead = currContent
				line = f.readline()
				currContent = line.split('\t')
				if currContent == [''] or line == '': #If next line is empty store current
					WriteToFile(FileName,prevline)
					break
		else:
			WriteToFile(FileName,prevline)
			prevline = line
			tmpRead = currContent
			line = f.readline()
			currContent = line.split('\t')
			if currContent == [''] or line == '': #If next line is empty store current
				WriteToFile(FileName,prevline)
				break
	f.close()
	return
main()

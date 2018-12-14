import sys
# COMMAND: python graph.py 'InputPositions' 'resultT2' 
# INPUT: Pathway to text based files.
# OUTPUT: Removes all reads that have '*'

def WriteToFile(fileName,PacBioRead):
	f=open(fileName, "a+")
	f.write(PacBioRead)
	f.close()
	return None

def genNewString(arrPacBio):
	strPacBio = ''
	tmp = ''
	for i in range(len(arrPacBio)):
		if i != 0:
			tmp = tmp+'\t'+arrPacBio[i]
	arrTmp = tmp.split('\t')
	for i in range(len(arrTmp)):
		if arrTmp[i] == '1' or arrTmp[i] == '0' or arrTmp[i] == '1\n' or arrTmp[i] == '0\n':
			if strPacBio == '':
				strPacBio = strPacBio+arrTmp[i]
			else:
				strPacBio = strPacBio+'\t'+arrTmp[i]
	strPacBio = strPacBio+'\n'
	return strPacBio

def main():
	f = open(sys.argv[1])
	countArr = []
	absPos = []
	freq = []
	ID = []
	comboArr = []
	check = 1
	numPos = 0
	sumCount = 0
	#FileName = sys.argv[2]
	#check = 0
	while line:
	line = f.readline()
	if "\t" not in line:
		tmpRead = line.split(' ')
	else:
		tmpRead = line.split('\t')
	absPos.append(tmpRead[0])
	f.close()
	
	f = open(sys.argv[2])
	while line:
	line = f.readline()
	tmpRead = line.split('\t')
	countArr.append(tmpRead[0])
	freq.append(int(tmpRead[0])
	tmpRead = tmpRead[1:]
	if check != 0:
		numPos = len(tmpRead)
		check = 0
	for x in tmpRead:
		comboArr.append(x)
	f.close()
	
	for i in range(len(comboArr)):
		ID.append(i+1)
		sumCount = sumCount + freq[i]
				
	for i in range(len(freq)):
		freq[i] = freq[i] / sumCount
	
	print(countArr)
	print(absPos)
	print(freq)
	print(ID)
	print(comboArr)
	print(check)
	print(numPos)
	print(sumCount)
	return
main()
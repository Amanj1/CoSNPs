import sys
# COMMAND: python filter_2ndresult.py 'ResultOutput' 'OutputForFilter'
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
	line = f.readline()
	tmpRead = line.split('\t')
	FileName = sys.argv[2]
	check = 0
	while line:
		if line == '':
			break
		for x in tmpRead:
			if x == '*' or x == '*\n':
				check = 1
		if check == 0:
			strLine = genNewString(tmpRead)
			WriteToFile(FileName,strLine)
		check = 0
		line = f.readline()
		tmpRead = line.split('\t')
	f.close()
	return
main()
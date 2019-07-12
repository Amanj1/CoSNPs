#!/usr/bin/python
import sys
# COMMAND: python filter_result.py 'numSNP' 'ResultOutput' 'OutputForFilter'
# INPUT: Pathway to text based files.
# OUTPUT: If nMatch are equal in then Mutation equal to '*'

def WriteToFile(fileName,PacBioRead):
	f=open(fileName, "a+")
	f.write(PacBioRead)
	f.close()
	return None

def main():
	snp = int(sys.argv[1])
	snpTab = snp*2 + 1
	f = open(sys.argv[2])
	line = f.readline()
	tmpRead = line.split('\t')
	tmplen = len(tmpRead)
	FileName = sys.argv[3]
	while line:
		if snpTab == tmplen:
			WriteToFile(FileName,line)
		line = f.readline()
		tmpRead = line.split('\t')
		tmplen = len(tmpRead)
	f.close()
	return
main()

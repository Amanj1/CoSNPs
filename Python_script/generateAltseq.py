import sys
# COMMAND: Python generateAltseq.py 'nucleotide' 'TmpReferenceSequence' 'pos of mutation' 'suffix'
# Input file refSeq with header
# OUTPUT: A file containing both refseq and altseq with header for both' 

def readFileRefseq(fname):
	data = []
	with open(fname) as file:
		data = file.readlines()
	return data

def WriteToFile(fileName,HeaderRef,HeaderAlt,refSeq,altSeq):
	refSeq = refSeq+'\n'
	altSeq = altSeq+'\n'
	fileName = fileName +".fasta"
	f=open(fileName, "a+")
	f.write(HeaderRef)
	f.write(refSeq)
	f.write(HeaderAlt)
	f.write(altSeq)
	f.close()
	return None

def StringToArray(x):
	seq = [y for y in x]
	return seq

def ArrayToString(x):
	str1 = ''.join(str(e) for e in x)
	return str1

def FindPosMid(x):
	#Sequences are always odd numbers (windowSize*2+1)
	#Assumtion sequences will never start from position in the begining of chr or the end of it. 
	pos = (len(x)/2)
	return pos

def InsertInSeq(seq,pos,n):
	pos = int(pos)
	seq[pos] = n
	return seq

def main():
	nucleotide = sys.argv[1]
	sequenceFile = sys.argv[2]
	positionMutation = sys.argv[3]
	suffix = sys.argv[4]
	prevData = readFileRefseq(sequenceFile)
	Header = prevData[0]
	#print(prevData)
	seqArr = StringToArray(prevData[1])
	p = FindPosMid(seqArr)
	newSeqArr = InsertInSeq(seqArr,p,nucleotide)
	altSeq = ArrayToString(newSeqArr)
	HeaderRef = ">Pos"+positionMutation+"Ref_"+Header
	HeaderAlt = ">Pos"+positionMutation+"Alt_"+Header
	NameOfNewFile = "query_Up"+suffix+"bp_Down"+suffix+"bp"
	refSeq = prevData[1]
	WriteToFile(NameOfNewFile,HeaderRef,HeaderAlt,refSeq,altSeq)
	#print(str1)
	#print(altSeq)
	return
main()
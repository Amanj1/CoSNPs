import sys
# COMMAND: Python generateAltseq.py 'nucleotide' 'ReferenceSequence'
# OUTPUT: String with new necleotide inserted in posisiton 'window+position+window' 

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
	sequence = sys.argv[2]
	seqArr = StringToArray(sequence)
	p = FindPosMid(seqArr)
	newSeqArr = InsertInSeq(seqArr,p,nucleotide)
	altSeq = ArrayToString(newSeqArr)
	print(altSeq)
	return
main()











































































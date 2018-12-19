#!/usr/bin/python
import sys
# COMMAND: Python generateAltseq.py 'nucleotide' 'ReferenceSequence'
# OUTPUT: String with new necleotide inserted in posisiton 'window+position+window'
# python generateRefseq.py tmpUP_1.bed tmpDown_1.bed

def ReadFile(Fname):
#Read file within a specific line
	file = open(Fname,"r")
	str1 = file.readline()
	file.close()
	return str1

def StringToArrayByChar(x):
	x.rstrip()
	seq = [y for y in x]
	return seq

def StringToArrayBySplit(x,split):
	x.rstrip()
	seq = x.split(split)
	return seq

def ArrayToString(x):
	str1 = ''.join(str(e) for e in x)
	return str1

def distance(x, y):
	d = int(y) - int(x)
	return d

def FindPosMid(x):
	return x

def GenerateSeq(startValue, startValueFile, startStr, stopValue, stopValueFile, endStr, totStr):
	tmpArr = []
	newArr = []
	totStart = startValueFile - startValue
	totStop = stopValueFile - stopValue

	totArr = StringToArrayByChar(totStr)
	RtotArr = totArr[::-1]

	print("totstart and totStop and length of totARR")
	print(totStart)
	print(totStop)
	print(len(totArr))
	print(totArr)
	print(totStr)
	print(RtotArr)

	for i in range(len(totArr)):
		if(i >= totStart):
			tmpArr.append(totArr[i])
		if(i == (totStart+totStart+totStop-2)):
		   break
	#newArr = newArr[::-1]


	print(len(tmpArr))
	print(ArrayToString(tmpArr))

	#totArr = rev[::-1]
	#arr = StringToArrayByChar(seq)
	#newArr = arr[start:stop]
	return None

def ReadFileByLine(Fname,start,stop):
	str1 = ""
	c = 0
	control = 0
	posCalc = 0
	prevPosCalc = 0
	with open(Fname, 'rU') as f:
		for line in f:
			if c > 0:
				posCalc = posCalc + len(StringToArrayByChar(line))
				if posCalc >= start:
					str1 = str1 + line
					if control == 0:
						startPos = posCalc
						startStr = line.rstrip()
						prevPosCalc = posTmp
						control = 1
				if posCalc > stop:
					endPos = posCalc
					endStr = line
					break
				posTmp = posCalc
			c = 1
	f.close()
	s = startPos - len(startStr)
	print("start value")
	print(start)
	print("starting posistion in readLine")
	print(startPos)
	print("previous starting posistion in readLine")
	print(prevPosCalc)
	print("string from startPos")
	print(startStr)
	print("stop value")
	print(stop)
	print("ending posistion in readLine")
	print(endPos)
	print("string from endPos")
	print(endStr)
	print("total length of string of intrest")
	print(str1)
	GenerateSeq(start, startPos, startStr, stop, endPos, endStr, str1)
	return None

def main():
	upFile = sys.argv[1]
	downFile = sys.argv[2]
	sequenceFile = sys.argv[3]

	UpPosStr = ReadFile(upFile)
	UpPosArr = StringToArrayBySplit(UpPosStr,'\t')

	DownPosStr = ReadFile(downFile)
	DownPosArr = StringToArrayBySplit(DownPosStr,'\t')

	dist = distance(DownPosArr[2], UpPosArr[2])
	print(DownPosArr[2])
	print(UpPosArr[2])
	print(dist)
	print("\n")
	chrSeq = ReadFileByLine(sequenceFile,int(DownPosArr[2]),int(UpPosArr[2])+1)
	#refSeq = GenerateSeq(chrSeq,DownPosArr[2],UpPosArr[2])
	#print(chrSeq)

	return
main()

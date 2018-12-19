#!/usr/bin/python
import sys

# python scriptWindow chr1:20 5 1 ########example####
# Python scriptWindow 'position in chr' 'window size' 'index when generating tmp files' 'position of mutation'
# WriteToFile("tmpUP", outputUP, suffix) - Generates positions for PacBio reads UpStream
# WriteToFile("tmpDown", outputDown, suffix)  - Generates positions for PacBio reads DownStream
# WriteToFile("tmpPosRef", CoverRegion, suffix) - Generates positions for reference sequence
# When using COMMAND after generating files
# bedtools getfasta -fi sequenceHG19.fasta -bed tmpPosRef_'suffix'.bed -fo 'nameForRefSeq'.fa


def WriteToFile(fileName, strData, s):
	fileName = fileName +"_" + s +".bed"
	f=open(fileName, "a+")
	f.write(strData)
	f.close()
	return None


def main():
	Pos = sys.argv[1]
	window = sys.argv[2]
	suffix = sys.argv[3]
	arrPos = Pos.split(':')
	Up = int(arrPos[1]) + int(window)
	Down = int(arrPos[1]) - int(window) -1
	Down1 = Down +1
	Up1 = Up+1
	outputUP = str(arrPos[0]) + '\t' + str(Up)  +'\t' + str(Up1)
	outputDown = str(arrPos[0]) + '\t' + str(Down)  +'\t' + str(Down1)
	CoverRegion = str(arrPos[0]) + '\t' + str(Down)  +'\t' + str(Up)
	WriteToFile("tmpPosRef", CoverRegion, suffix)
	return

main()

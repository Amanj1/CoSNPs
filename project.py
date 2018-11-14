import sys # for exiting on errors
import numpy as np
import string
import random
import pysam
#import matplotlib.pyplot as plt
import BamProcess as bam

def readFile(name):#empty now
	return temp

def printGenes(seq):
	print("\nGene sequences: \n")
	n = len(seq)-1
	print("number of genes: ", n+1)
	for i in range(len(seq)):
		print(i)
		print(seq[i])
		print("\n")
	return None

def printOneGene(seq,index):
	"""Prints out a specific gene within an array of genes."""
	print("\nGene sequence in index\n", index)
	print(seq[index])
	print("\n")
	return None

def main():
	#fileName = "pb_467_2_sr_blasr.bam"
	fileName = "my_sorted.bam"
	myseq=bam.datafile(file=fileName,chr="chr17")
	myseq.seq
	
	myseq.FetchChrPos()
	return

main()


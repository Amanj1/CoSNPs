import pysam
import sys
import numpy as np

class datafile():
	
	def __init__(self,file,chr):
		self.fname = file
		self.fname = self.sortBam()
		self.samfile = pysam.AlignmentFile(self.fname,"rb")
		self.seq= []
		self.chr = chr
		return None

	def sortBam(self):
		name = "output.bam"
		pysam.sort("-o",name,self.fname)
		return name
				   
	def FetchChrPos(self):
		x = []
		for read in self.samfile.fetch(self.chr,until_eof=True):
			x.append(read)
			print(read)
			print("\n")
		self.seq = x
		return None
    
  




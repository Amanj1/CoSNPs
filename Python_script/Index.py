import pybam

bam_data = pybam.read('./pb_467_2_sr_blasr.bam')
bam_rowData = []
for alignment in bam_data:
	bam_rowData.append(alignment.sam_seq)
        #print alignment.sam_seq
		#print alignment.sam_mapq

print bam_rowData[0]
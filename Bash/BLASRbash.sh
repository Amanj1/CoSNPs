#!/bin/bash
#rm results.sam
rm blasrResult.txt
inBAM='../PacBioRead/120bpSelected.bam'
x="$(samtools view $inBAM|wc -l)"
y=48
z=38
query='../Query/query_seqRef_Up20_down20.fa'
samtools view -H $inBAM > Header.sam
for (( c=$z; c<=$y; c++ ))
do
   echo $c
   cat Header.sam > tmp.sam
   samtools view $inBAM | awk '{if((NR=='$c')) print $0}' >> tmp.sam
   #samtools view -h -b tmp.sam > tmp.bam
   samtools view tmp.sam | awk '{print $1}'
   samtools bam2fq tmp.sam > tmp.fastq
   awk ' NR %4 == 1' tmp.fastq
   cat tmp.fastq  | paste - - - - | awk -F '\t' '{print ">"$1 ; print $2;}' > tmp.fasta
   blasr $query tmp.fasta --minMatch 8 --minSubreadLength 1 --minReadLength 1 --maxScore 400 -m 0 \
    >> blasrResult.txt
    sleep 1
    rm -f tmp*
done

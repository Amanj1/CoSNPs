#!/bin/bash
rm results.sam
inBAM='../PacBioRead/120bpSelected.bam'
x="$(samtools view $inBAM|wc -l)"
y=40
z=35
query='../Query/query_15bpUP_15bpDown.fasta'
samtools view -H $inBAM > Header.sam
for (( c=$z; c<=$y; c++ ))
do
   echo $c
   cat Header.sam > tmp.sam
   samtools view $inBAM | awk '{if((NR=='$c')) print $0}' >> tmp.sam
   samtools view tmp.sam | awk '{print $1}'
   samtools bam2fq tmp.sam > tmp.fastq
   awk ' NR %4 == 1' tmp.fastq
   blasr -r tmp.fastq -q $query -o tmpResult.sam
   samtools view tmpResult.sam | awk '{print $1,$2,$3,$4}'
   #TODO add header for results.bam

   samtools view tmpResult.sam >> results.sam
   sleep 1
   rm -f tmp*
   #rm -f tmp.sam
   #rm -f tmp.fastq
done
rm -f Header.sam

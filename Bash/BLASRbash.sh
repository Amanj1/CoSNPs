#!/bin/bash
#rm results.sam
#rm blasrResult.txt
mkdir -p ../output
#TODO remove the same name file
#rm blasrResult.txt
#inBAM='../PacBioRead/120bpSelected.bam'
inBAM=$3
x="$(samtools view $inBAM|wc -l)"
y=40
z=30
#auto add query in command line
query=$1
WindowSize=$2
#remove the output file it already exist
#rm -f ../Output/blasrResult_halfWin${WindowSize}.txt
rm -f ../output/Dec6_minMatch12_blasrResult_halfWin${WindowSize}.txt
#read header of the input PacBioRead
samtools view -H $inBAM > Header.sam
for (( c=$z; c<=$y; c++ )) #starting with 0? test
do
   echo $c
   cat Header.sam > tmp.sam
   samtools view $inBAM | awk '{if((NR=='$c')) print $0}' >> tmp.sam
   #samtools view -h -b tmp.sam > tmp.bam
   #print input PacBio read name each loop
   #samtools view tmp.sam | awk '{print $1}'
   samtools bam2fq tmp.sam > tmp.fastq
   #awk ' NR %4 == 1' tmp.fastq
   #convert fastQ to fasta
   cat tmp.fastq  | paste - - - - | awk -F '\t' '{print ">"$1 ; print $2;}' > tmp.fasta
   blasr $query tmp.fasta --minMatch 12 --minSubreadLength 1 --minReadLength 1 --maxScore 400 -m 5 \
    >> ../output/Dec6_minMatch12_blasrResult_halfWin${WindowSize}.txt
    #sleep 1
    rm -f tmp*
done
rm $query

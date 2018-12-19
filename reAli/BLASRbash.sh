#!/bin/bash
#rm results.sam
#rm blasrResult.txt
#mkdir -p ../output
#TODO remove the same name file
#rm blasrResult.txt
#inBAM='../PacBioRead/120bpSelected.bam'
inBAM=$3
x="$(samtools view $inBAM|wc -l)"
y=$x
z=1
#auto add query in command line
query=$1
WindowSize=$2
#remove the output file it already exist
rm -f BlasrResult_halfWin${WindowSize}.txt
#read header of the input PacBioRead
samtools view -H $inBAM > Header.sam
for (( c=$z; c<=$y; c++ )) #starting with 0? test
do
   echo "Realigning read: $c"
   cat Header.sam > tmp.sam
   samtools view $inBAM | awk '{if((NR=='$c')) print $0}' >> tmp.sam
   #print input PacBio read name each loop
   samtools bam2fq tmp.sam > tmp.fastq
   #convert fastQ to fasta
   cat tmp.fastq  | paste - - - - | awk -F '\t' '{print ">"$1 ; print $2;}' > tmp.fasta
   #TODO: finalize the parameters for realignments
   blasr $query tmp.fasta --minMatch 8 --minSubreadLength 1 --minReadLength 1 --maxScore 200 -m 5 \
    >> BlasrResult_halfWin${WindowSize}.txt
    #sleep 1
    rm -f tmp*
done
rm $query

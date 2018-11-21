#!/bin/bash
pos1 = chr17:7578263
altNec1 = A
pos2 = chr17:7579312
altNec2 = T
WindowSize = 20
posM1 = 1
posM2 = 2
chrSeq = sequence.fasta

python scriptWindow $pos1 $WindowSize $posM1
python scriptWindow $pos2 $WindowSize $posM2
bedtools getfasta -fi $chrSeq -bed tmpPosRef_1.bed -fo tmpFasta.fasta
python generateAltseq.py $altNec1 tmpFasta.fasta $posM1 $WindowSize
rm tmpFasta.fasta
bedtools getfasta -fi $chrSeq -bed tmpPosRef_2.bed -fo tmpFasta.fasta
python generateAltseq.py $altNec2 tmpFasta.fasta $posM2 $WindowSize
rm tmpFasta.fasta


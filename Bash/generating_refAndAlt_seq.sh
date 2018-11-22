#!/bin/bash
echo "Type the half-window size (Intenger) that you want, followed by [ENTER]:"
read WindowSize
pos1='chr17:7578263'
altNec1='A'
pos2='chr17:7579312'
altNec2='T'
#WindowSize='20'
#TODO more dynamic, only for 1 and 2 for now
posM1='1'
posM2='2'
chrSeq='../hg19/hg19_chr17_changeName.fasta'

python ../Python_script/scriptWindowRef.py $pos1 $WindowSize $posM1
python ../Python_script/scriptWindowRef.py $pos2 $WindowSize $posM2
bedtools getfasta -fi $chrSeq -bed tmpPosRef_1.bed -fo tmpFasta.fasta
python ../Python_script/generateAltseq.py $altNec1 tmpFasta.fasta $posM1 $WindowSize
rm tmpFasta.fasta
bedtools getfasta -fi $chrSeq -bed tmpPosRef_2.bed -fo tmpFasta.fasta
python ../Python_script/generateAltseq.py $altNec2 tmpFasta.fasta $posM2 tmp
rm tmpFasta.fasta
rm tmpPosRef_1.bed tmpPosRef_2.bed
cat query_Uptmp* >> query_Up${WindowSize}bp_Down${WindowSize}bp.fasta
awk 'NF' query_Up${WindowSize}bp_Down${WindowSize}bp.fasta > tmpSomething.fasta
rm query_Up${WindowSize}bp_Down${WindowSize}bp.fasta
rm query_Uptmp*
cat tmpSomething.fasta > query_Up${WindowSize}bp_Down${WindowSize}bp.fasta
mv query_Up${WindowSize}bp_Down${WindowSize}bp.fasta ../Query/
sh BLASRbash.sh ../Query/query_Up${WindowSize}bp_Down${WindowSize}bp.fasta $WindowSize
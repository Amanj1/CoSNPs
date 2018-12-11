#!/bin/bash
echo "Type the half-window size (Intenger) that you want, followed by [ENTER]:"
read WindowSize
# TODO: input as file, handle more than 2 position
pos1='chr17:7578263'
altNec1='A'
pos2='chr17:7579312'
altNec2='T'
#WindowSize='20'
#TODO more dynamic, only for 1 and 2 for now
posM1='1'
posM2='2'
chrSeq='../hg19/hg19_chr17_changeName.fasta'
PacBioINPUT= '../PacBioRead/pb_467_2_sr_blasr.bam'

# ==>generate PacBio_Selected.bam
# rm previously generated PacBio reads
rm -f ../PacBioRead/PacBio_Selected.bam
cp ../PacBioRead/pb_467_2_sr_blasr.bam ../PacBioRead/PacBio_Selected.bam
# selecting PacBio input BAM file
# TODO: make into loop when positoin input as file (more than 2 positions)
sh SelectPacBio.sh $pos1 $WindowSize $posM1
sh SelectPacBio.sh $pos2 $WindowSize $posM2
# Generating ref and alt sequences from hg19
# TODO: into loop when positoin input as file (more than 2 positions)
python ../Python_script/scriptWindowRef.py $pos1 $WindowSize $posM1
python ../Python_script/scriptWindowRef.py $pos2 $WindowSize $posM2
bedtools getfasta -fi $chrSeq -bed tmpPosRef_1.bed -fo tmpFasta.fasta
python ../Python_script/generateAltseq.py $altNec1 tmpFasta.fasta $posM1 $WindowSize
rm tmpFasta.fasta
# for Pos2, the output is query_Uptmpbp_Downtmpbp.fasta
# TODO: loop to append from Pos2 to PosN, Pos1 should be define outside
bedtools getfasta -fi $chrSeq -bed tmpPosRef_2.bed -fo tmpFasta.fasta
python ../Python_script/generateAltseq.py $altNec2 tmpFasta.fasta $posM2 tmp
rm tmpFasta.fasta
rm tmpPosRef_1.bed tmpPosRef_2.bed
cat query_Uptmp* >> query_Up${WindowSize}bp_Down${WindowSize}bp.fasta

#remove empty lines
# awk need to save into file
awk 'NF' query_Up${WindowSize}bp_Down${WindowSize}bp.fasta > tmpSomething.fasta
rm query_Up${WindowSize}bp_Down${WindowSize}bp.fasta
rm query_Uptmp*
cat tmpSomething.fasta > query_Up${WindowSize}bp_Down${WindowSize}bp.fasta
mv query_Up${WindowSize}bp_Down${WindowSize}bp.fasta ../Query/

#send the alt/ref sequences for BLASR alignment
sh BLASRbash.sh ../Query/query_Up${WindowSize}bp_Down${WindowSize}bp.fasta $WindowSize ../PacBioRead/PacBio_Selected.bam

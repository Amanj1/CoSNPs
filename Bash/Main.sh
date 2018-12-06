#!/bin/bash
# TODO: ErrorHandler should check if the input file with the pos and mutations are correct
echo "Type the half-window size (Intenger) that you want, followed by [ENTER]:"
read WindowSize
# TODO: input as file, handle more than 2 position
pos1='chr17:7578263'
altNec1='A'
pos2='chr17:7579312'
altNec2='T'
#WindowSize='20'
#TODO more dynamic, only for 1 and 2 for now
numPos='2'
posM1='1'
posM2='2'
chrSeq='../hg19/hg19_chr17_changeName.fasta'
PacBioINPUT='../PacBioRead/pb_467_2_sr_blasr.bam'
#chmod u+x ../PacBioRead/pb_467_2_sr_blasr.bam #add permission

# ==>generate PacBio_Selected.bam
# rm previously generated PacBio reads
rm -f PacBio_Selected.bam
#initial input bam set as filtered chr17.bam, to reduce the samtools running time
# TODO: change to sam format to optimise the run time
# TODO: save select PacBio reads when the pipeline is good
cp ../PacBioRead/chr17.bam PacBio_Selected.bam

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
rm tmpSomething.fasta
#TODO: move in the end
mv query_Up${WindowSize}bp_Down${WindowSize}bp.fasta ../Query/
ls ../Query/
#send the alt/ref sequences for BLASR alignment
sh BLASRbash.sh ../Query/query_Up${WindowSize}bp_Down${WindowSize}bp.fasta $WindowSize PacBio_Selected.bam

#not working for /output/1-80_minMatch12_blasrResult_halfWin55.txt
#../output/text_minMatch12_1-40blasrResult_halfWin55.txt
echo "Into filtering part:"
#TODO: add threhold input
rm -f result.txt
BlasrOutput='../output/Dec6_minMatch12_blasrResult_halfWin'${WindowSize}'.txt'
python ../Python_script/Filter_Blasr.py $BlasrOutput tmpOut1stFilter.txt
# TODO: first input numPos, from read number of lines
python ../Python_script/Filter_Blasr_Bad_data.py $numPos tmpOut1stFilter.txt tmpOut2ndFilter.txt 0.8
#handle the case where we have nMatch equal to Alt and Ref
#Result ouput should be: mutation boolean nMatch mutatio bolean pos 2 minMatch
# read 0 nMatch 1 nMatch
python ../Python_script/results.py tmpOut2ndFilter.txt result.txt
rm tmpOut*
#remove the tmp file, use mv if needed to save in other directory
rm Header.sam

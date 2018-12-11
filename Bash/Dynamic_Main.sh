#! /bin/bash
echo "Start!"
##############TODO: input by user####################
chrSeq='../hg19/hg19_chr17_changeName.fasta'
PacBioINPUT='../PacBioRead/chr17.bam'
#Check min WindowSize
WindowSize=35
#sapce delimited file
input="../Testing/inputPOS_test.txt"

FilterThrehold='0.6'
#####################################################
rm -f PacBio_Selected.bam
rm -f result.txt
cp $PacBioINPUT PacBio_Selected.bam
rm -f query_Up${WindowSize}bp_Down${WindowSize}bp.fasta
numPos=0
#echo "Number of reads in input bam"
#samtools view PacBio_Selected.bam | wc -l

while IFS= read -r var
do
  numPos=$((numPos+1))
  numPosStr="$numPos"
  #echo $numPos
  pos=`echo $var | awk -F" " '{print $1}'`
  altNec=`echo $var | awk -F" " '{print $2}'`
  #Select PacBio input covering the current position
  sh SelectPacBio.sh $pos $WindowSize $numPosStr
  #samtools view PacBio_Selected.bam | wc -l
  #Generate Alt Ref seq for alignment with WindowSize
  python ../Python_script/scriptWindowRef.py $pos $WindowSize $numPosStr
  bedtools getfasta -fi $chrSeq -bed tmpPosRef_$numPosStr.bed -fo tmpFasta.fasta
  python ../Python_script/generateAltseq.py $altNec tmpFasta.fasta $numPosStr $WindowSize
  rm tmpFasta.fasta
  rm tmpPosRef_*
  #remove empty lines
  awk 'NF' query_Up${WindowSize}bp_Down${WindowSize}bp.fasta > tmpSomething.fasta
  rm query_Up${WindowSize}bp_Down${WindowSize}bp.fasta
  cat tmpSomething.fasta > query_Up${WindowSize}bp_Down${WindowSize}bp.fasta
  rm tmpSomething.fasta

done < $input
mv -f query_Up${WindowSize}bp_Down${WindowSize}bp.fasta ../Query/
#send the alt/ref sequences for BLASR alignment
sh BLASRbash.sh ../Query/query_Up${WindowSize}bp_Down${WindowSize}bp.fasta $WindowSize PacBio_Selected.bam

#not working for /output/1-80_minMatch12_blasrResult_halfWin55.txt
#../output/text_minMatch12_1-40blasrResult_halfWin55.txt
echo "Into filtering part:"
#TODO: add threhold input
rm -f result.txt
BlasrOutput='../output/Dec6_minMatch12_blasrResult_halfWin'${WindowSize}'.txt'
python ../Python_script/Filter_Blasr.py $BlasrOutput tmpOut1stFilter.txt
python ../Python_script/Filter_Blasr_Bad_data.py $numPos tmpOut1stFilter.txt tmpOut2ndFilter.txt $FilterThrehold
#handle the case where we have nMatch equal to Alt and Ref
#Result ouput should be: mutation boolean nMatch mutatio bolean pos 2 minMatch
# read 0 nMatch 1 nMatch
python ../Python_script/Filter_Blasr_3rd.py tmpOut2ndFilter.txt tmpOut3ndFilter.txt
python ../Python_script/results.py tmpOut3ndFilter.txt tmpOutresult.txt
python ../Python_script/filter_result.py $numPos tmpOutresult.txt result.txt
rm tmpOut*
#remove the tmp file, use mv if needed to save
rm Header.sam

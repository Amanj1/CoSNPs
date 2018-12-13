#! /bin/bash
echo "Start!"
##############TODO: input by user####################
#TODO: error handler??#
chrSeq='../hg19/hg19_chr17_changeName.fasta'
PacBioINPUT='../PacBioRead/chr17.bam'
#Check min WindowSize
WindowSize=50
#sapce delimited file
#TODO 2/5/10/50/100
input="../Testing/input2POS_test.txt"
#input="../Testing/InputPos.txt"
FilterThrehold='0.9'
python ../Python_script/errorHandler.py $FilterThrehold $WindowSize $input > tmp_errorMsg.txt
checkpoint=`tail -n 1 tmp_errorMsg.txt`
if [ $checkpoint = '0' ]
then
  echo 'Input parameters checkpoint passed!'
  rm tmp_errorMsg.txt
else
  cat tmp_errorMsg.txt
  rm tmp*
  exit 128
fi
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
echo "Start realignments!"
#send the alt/ref sequences for BLASR alignment
sh BLASRbash.sh ../Query/query_Up${WindowSize}bp_Down${WindowSize}bp.fasta $WindowSize PacBio_Selected.bam

#not working for /output/1-80_minMatch12_blasrResult_halfWin55.txt
#../output/text_minMatch12_1-40blasrResult_halfWin55.txt
echo "Into filtering part"
#TODO: add threhold input
rm -f resultT1*
BlasrOutput='../output/Dec6_minMatch12_blasrResult_halfWin'${WindowSize}'.txt'
python ../Python_script/Filter_Blasr.py $BlasrOutput tmpOut1stFilter.txt
python ../Python_script/Filter_Blasr_Bad_data.py $numPos tmpOut1stFilter.txt tmpOut2ndFilter.txt $FilterThrehold
#handle the case where we have nMatch equal to Alt and Ref
#Result ouput should be: mutation boolean nMatch mutatio bolean pos 2 minMatch
# read 0 nMatch 1 nMatch
python ../Python_script/Filter_Blasr_3rd.py tmpOut2ndFilter.txt tmpOut3ndFilter.txt
python ../Python_script/results.py tmpOut3ndFilter.txt tmpOutresult.txt
python ../Python_script/filter_result.py $numPos tmpOutresult.txt resultT1.txt
python ../Python_script/Sumfilter_result_improved.py resultT1.txt resultT1_label.txt
echo "Filtering finished"
echo "Number of long reads input:"
samtools view $PacBioINPUT | wc -l
echo "Number of selected long reads:"
#TODO: if selected PacBio file is empty/doesn't exist, terminate the software
samtools view PacBio_Selected.bam | wc -l
echo "Number of reads containing all Pos and pass the numMatch threshold:"
wc -l resultT1.txt
echo "Number of reads left for summarizing:"
wc -l resultT1_label.txt
echo "Summary:"
#summary final data:
#TODO: save into file AND graphical design for the data
cat resultT1_label.txt | sort | uniq -c
rm tmpOut*
#remove the tmp file, use mv if needed to save
rm Header.sam

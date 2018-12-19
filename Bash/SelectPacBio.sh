#example: python ../Python_script/scriptWindowPacBio.py chr1:20 5 1
rm -f tmpDown* tmpUP*
python ./Python_script/scriptWindowPacBio.py $1 $2 $3
# output file format: tmpUP_$3.bed tmpDown_$3.bed
bedtools intersect -abam Longread_Selected.bam -b tmpUP_$3.bed  -wa \
| bedtools intersect -abam stdin -b tmpDown_$3.bed  -wa \
> Longread_Selected_tmp.bam
mv -f Longread_Selected_tmp.bam Longread_Selected.bam
rm tmpDown* tmpUP*

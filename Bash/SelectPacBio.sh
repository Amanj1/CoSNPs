#example: python ../Python_script/scriptWindowPacBio.py chr1:20 5 1
rm -f tmpDown* tmpUP*
python ../Python_script/scriptWindowPacBio.py $1 $2 $3
#cat tmpUP*
# output file format: tmpUP_$3.bed tmpDown_$3.bed
#TODO: PacBio_Selected.bam is empty, because of the same name?
bedtools intersect -abam PacBio_Selected.bam -b tmpUP_$3.bed  -wa \
| bedtools intersect -abam stdin -b tmpDown_$3.bed  -wa \
> PacBio_Selected_tmp.bam
mv -f PacBio_Selected_tmp.bam PacBio_Selected.bam
rm tmpDown* tmpUP*

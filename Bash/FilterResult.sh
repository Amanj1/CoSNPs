#!/bin/bash
#not working for /output/1-80_minMatch12_blasrResult_halfWin55.txt
#../output/text_minMatch12_1-40blasrResult_halfWin55.txt
rm -f result.txt
BlasrOutput='../output/Dec6_minMatch12_blasrResult_halfWin30.txt'
python ../Python_script/Filter_Blasr.py $BlasrOutput tmpOut1stFilter.txt
python ../Python_script/Filter_Blasr_Bad_data.py 2 tmpOut1stFilter.txt tmpOut2ndFilter.txt
#handle the case where we have nMatch equal to Alt and Ref
#Result ouput should be: mutation boolean nMatch mutatio bolean pos 2 minMatch
# read 0 nMatch 1 nMatch
python ../Python_script/results.py tmpOut2ndFilter.txt result.txt
rm tmpOut*
#remove the tmp file, use mv if needed to save
rm Header.sam

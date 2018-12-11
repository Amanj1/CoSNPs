#!/bin/bash
#not working for /output/1-80_minMatch12_blasrResult_halfWin55.txt
#../output/text_minMatch12_1-40blasrResult_halfWin55.txt
rm -f result.txt

BlasrOutput='../output/Dec6_minMatch12_blasrResult_halfWin35.txt'
python ../Python_script/Filter_Blasr.py $BlasrOutput tmpOut1stFilter.txt
#TODO numofSNP(1st input) and threhold(last input) dynamic, send the numofSNP to filter_result.py
python ../Python_script/Filter_Blasr_Bad_data.py 3 tmpOut1stFilter.txt tmpOut2ndFilter.txt 0.8
#handle the case where we have nMatch equal to Alt and Ref
#Result ouput should be: mutation boolean nMatch mutatio bolean pos 2 minMatch
# read 0 nMatch 1 nMatch
python ../Python_script/Filter_Blasr_3rd.py tmpOut2ndFilter.txt tmpOut3ndFilter.txt
python ../Python_script/results.py tmpOut3ndFilter.txt tmpOutresult.txt
python ../Python_script/filter_result.py 3 tmpOutresult.txt result.txt
rm tmpOut*
#remove the tmp file, use mv if needed to save
rm Header.sam

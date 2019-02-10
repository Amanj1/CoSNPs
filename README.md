# coSNPs version 1.0

## Introduction:

reAli is a software that can detect the coexistence of multiple SNPs in each single SMRT long read with higher accuracy. By assigning the positions and their mutated nucleotides, reAli can realign the reads to the original and mutated version of referencial genome and determine wheteher there is mutation for the positions. The alignment part is done by using BlasR, a software dedicates to align SMRT sequencing data to the referencial genome.



## Required software:

#### Python Packages (mainly for: -g|--graph option):

Python 2.7.10 (default, Oct  6 2017, 22:29:07) ***(default MacOS python version)***,

#### Languages

Python 3.6.6 :: Anaconda, Inc., Bash/Linux

| Python packages | Version | Build          |
| --------------- | ------- | -------------- |
| numpy           | 1.15.4  | py36h6a91979_0 |
| tabulate        | 0.8.2   | py36_0         |
| matplotlib      | 3.0.0   | py36h54f8f79_0 |
| sys             | default | default        |

#### Other softwares:

| Software | Version | Build      |
| -------- | ------- | ---------- |
| bedtools | 2.27.1  | ha92aebf_2 |
| samtools | 1.9     | h8ee4bcc_1 |
| blasr    | 5.3.2   | hac9d22c_4 |

## Install reMatch:

1. Download the github repository.

2. Add the reMap folder to $PATH:

   ```bash
   #example:
   $ pwd
   /Users/apple/Documents/reAli
   $ export PATH=/Users/apple/Documents/reAli:$PATH
   
   (base) student-219-62:test apple$ echo $PATH
   /Users/apple/Documents/AppliedBioinformatics/GitFolder/Applied_Bioinformatics_Xdrop/reAli:/Users/apple/Documents/AppliedBioinformatics/GitFolder/Applied_Bioinformatics_Xdrop/Bash:/Users/apple/biosoft/myBin/bin:/Users/apple/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/ncbi/blast/bin:/opt/X11/bin
   ```

   For permenently add the file to $PATH:

   ```bash
   sudo nano /etc/paths
   ```

   Then add the path to the reAli folder.

3. Add permissions to all the files in Main folder :

   ```bash
   $ chmod +x *
   ```


## Help function/ Wiki page:

help function with -h|--help

Link to wiki page:



## Example run:

##### Download referential genome: hg19-chr17.fasta (79M):

 https://drive.google.com/drive/folders/1nQAvPAJ8RqW8NmK8poa7au844I_-OrcT?usp=sharing

*For referential genome .fast file and position file, they should have the same header.

##### Testing data available in this repository: 

**./Testing/input2POS_test.txt** input file for the positions of interest.

**./Testing/chr17.bam** input file for the mapped long read

#### Running the reAli:

```bash
#example
$ coSNPs_main.sh chr17.bam input2POS_test.txt hg19_chr17_changeName.fasta 
$ pwd
/Users/apple/Documents/AppliedBioinformatics/GitFolder/test
$ coSNPs_main.sh -g ../Applied_Bioinformatics_Xdrop/Testing/chr17.bam ../Applied_Bioinformatics_Xdrop/Testing/input2POS_test.txt ../Applied_Bioinformatics_Xdrop/hg19/hg19_chr17_changeName.fasta -f 0.5

```

Example output with

```bash
$ coSNPs_main.sh ../Applied_Bioinformatics_Xdrop/Testing/chr17.bam \ ../Applied_Bioinformatics_Xdrop/Testing/input2POS_test.txt \ ../Applied_Bioinformatics_Xdrop/hg19/hg19_chr17_changeName.fasta -g
```

```bash
Number of long reads input:
    3360
Number of selected long reads:
      81
Number of reads containing all Pos and pass the numMatch threshold:
      65 resultT1.txt
Number of reads left for summarizing:
      53
Summary:
If return an error, make sure the python libraries installed to the python version below!
3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 11:07:29) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]
  ID    Count    Frequency  chr17:7578263,chr17:7579312
----  -------  -----------  -----------------------------
   1        1    0.0188679  0		0
   2       19    0.358491   0		1
   3       32    0.603774   1		0
   4        1    0.0188679  1		1

#running with 6 position

Number of long reads input:
    3360
Number of selected long reads:
      74
Number of reads containing all Pos and pass the numMatch threshold:
      47 resultT1.txt
Number of reads left for summarizing:
      24
Summary:
If return an error, make sure the python libraries installed to the python version defined list below!
3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 11:07:29) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]
  ID    Count    Frequency  chr17:7578263,chr17:7579312,chr17:7579472,chr17:7579801,chr17:7578837,chr17:7578645
----  -------  -----------  -----------------------------------------------------------------------------------
   1        1    0.0416667  0		0		1		1		1		1
   2        8    0.333333   0		1		1		1		1		1
   3       14    0.583333   1		0		1		1		1		1
   4        1    0.0416667  1		1		1		1		1		1
```

```
coSNPs_main.sh ../Applied_Bioinformatics_Xdrop/Testing/chr17.bam ../Applied_Bioinformatics_Xdrop/Testing/input4POS_test.txt ../Applied_Bioinformatics_Xdrop/hg19/hg19_chr17_changeName.fasta 
```


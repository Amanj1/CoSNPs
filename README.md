# coSNPs version 1.1

## Introduction:

coSNPs is a software that can detect the coexistence of multiple SNPs in each single SMRT long read with higher accuracy using local realignment. 

By assigning the positions and their mutated nucleotides, coSNPs can realign the reads to the original and mutated version of referential sequence and determine the nucleotide of the position of interest. The alignment part is done by using [blasr](https://github.com/PacificBiosciences/blasr) a software dedicates to align SMRT sequencing data to the referencial genome.



## Required software:

#### Python Packages:

Python 2.7.16 :: Anaconda, Inc.

| Python packages | Version | Build          |
| --------------- | ------- | -------------- |
| numpy           | 1.16.4  | py27h7e9f1db_0 |
| tabulate        | 0.8.3   | py_0           |
| sys             | default | default        |

#### Other softwares:

| Software | Version | Build       |
| -------- | ------- | ----------- |
| bedtools | 2.28.0  | hdf88d34_0  |
| samtools | 1.9     | h8571acd_11 |
| blasr    | 5.3.3   | h707fff8_0  |

## Install coSNPs:

We recommend running the analysis by [docker](https://docs.docker.com/):

1. Install docker

2. Download the GitHub repository

3. Inside the [`Docker`]/() folder:

   ```bash
   # Build image defined in ./Dockerfile
   docker build --tag=cosnps_image .
   # Start container in background
   sudo docker run -d \
   -v /PATH_REPOSITORY_OF_COSNPS/main:/home/Connected --name cosnps_container \
   -it cosnps_image
   # Execute an interactive bash shell on the container
   sudo docker exec -i -t cosnps_container /bin/bash
   
   # To exit the interactie container:
   exit
   # To kill the container:
   docker kill cosnps_container
   # To remove the docker image:
   docker image rm cosnps_image
   ```

## Help function/Wiki page:

help function with `coSNPs_main.sh -h|—help`

Wiki page:

## Example run:

##### Download referential genome: hg19-chr17.fasta (79M):

 https://drive.google.com/drive/folders/1nQAvPAJ8RqW8NmK8poa7au844I_-OrcT?usp=sharing

*For referential genome .fast file and position file, they should have the same header.

##### Testing data available in this repository: 

**[./Testing/input2POS_test.txt](https://github.com/Amanj1/Applied_Bioinformatics_Xdrop/blob/Deliverable/Testing/input2POS_test.txt)** input file for the positions of interest.

**[./Testing/chr17.bam](https://github.com/Amanj1/Applied_Bioinformatics_Xdrop/blob/Deliverable/Testing/chr17.bam)** input file for the mapped long read

#### Running the coSNPs:

```bash
#example
$ coSNPs_main.sh chr17.bam input2POS_test.txt hg19_chr17_changeName.fasta 
$ pwd
/Users/apple/Documents/AppliedBioinformatics/GitFolder/test
$ coSNPs_main.sh -g ../Applied_Bioinformatics_Xdrop/Testing/chr17.bam ../Applied_Bioinformatics_Xdrop/Testing/input2POS_test.txt ../Applied_Bioinformatics_Xdrop/hg19/hg19_chr17_changeName.fasta -f 0.5

```

Example output

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

#Running with 6 position (input6POS_test.txt)

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


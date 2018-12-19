# reAli version 1.0

## Introduction:

reAli is a software that can detect the coexistence of multiple SNPs in each single SMRT long read with higher accuracy. By assigning the positions and their mutated nucleotides, reAli can realign the reads to the original and mutated version of referencial genome and determine wheteher there is mutation for the positions. The alignment part is done by using BlasR, a software dedicates to align SMRT sequencing data to the referencial genome.



## Required software:

#### Python Packages (mainly for: -g|--graph option):

Python 2.7.10 (default, Oct  6 2017, 22:29:07) ***(default MacOS python version)***,

OR

Python 3.6.6 :: Anaconda, Inc. ***(for installing packages needed for -g|--graph option in graph.py file)***

| Packages   | Version | Build          |
| ---------- | ------- | -------------- |
| numpy      | 1.15.4  | py36h6a91979_0 |
| tabulate   | 0.8.2   | py36_0         |
| matplotlib | 3.0.0   | py36h54f8f79_0 |

#### Other softwares:

| Software | Version | Build      |
| -------- | ------- | ---------- |
| bedrolls | 2.27.1  | ha92aebf_2 |
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
$ reAli_main.sh chr17.bam input2POS_test.txt hg19_chr17_changeName.fasta 
```


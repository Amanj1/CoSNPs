Software version:

Python 2.7.10 (default, Oct  6 2017, 22:29:07) ***(default MacOS python version)*** | Python 3.6.6 :: Anaconda, Inc. ***(for installing packages needed for -g|--graph option in graph.py file)***

Python Packages (especially for: -g|--graph option):

| Packages   | Version | Build          |
| ---------- | ------- | -------------- |
| numpy      | 1.15.4  | py36h6a91979_0 |
| tabulate   | 0.8.2   | py36_0         |
| matplotlib | 3.0.0   | py36h54f8f79_0 |

Other softwares:

| Software | Version | Build      |
| -------- | ------- | ---------- |
| bedrolls | 2.27.1  | ha92aebf_2 |
| samtools | 1.9     | h8ee4bcc_1 |
| blasr    | 5.3.2   | hac9d22c_4 |

Install reMatch:

1. Download the github repository.

2. Add the reMap folder to $PATH:

   ```bash
   #example:
   $ pwd
   /Users/apple/Documents/reAli
   $ export PATH=/Users/apple/Documents/reAli:$PATH
   ```

3. Add permissions to all the files in Main folder :

   ```bash
   $ chmod +x *
   ```



Help function/ Wiki page:

Call the help help function with -h|--help

Link to wiki page:



Example run:

Download hg19-chr17 testing data: https://drive.google.com/drive/folders/1nQAvPAJ8RqW8NmK8poa7au844I_-OrcT?usp=sharing

Test data available: **./Testing/input2POS_test.txt** input file for the positions of interest.

**./Testing/chr17.bam** input file for the mapped long read

Running the reAli:

```bash
#example
$ reAli_main.sh chr17.bam input2POS_test.txt hg19_chr17_changeName.fasta 
```


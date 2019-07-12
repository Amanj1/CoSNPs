# Base image
FROM continuumio/miniconda

WORKDIR /home

RUN conda install -c anaconda numpy=1.16.4
RUN conda install -c conda-forge tabulate=0.8.3
RUN conda install -c bioconda samtools=1.9
RUN conda install -c bioconda bedtools=2.28.0
RUN conda install -c bioconda blasr=5.3.3

ENV PATH /home/Connected/Applied_Bioinformatics_Xdrop/main:$PATH

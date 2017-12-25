#!/bin/bash

#Making sure that MAFFT-Homologs can run properly
unset MAFFT_BINARIES

#Getting the input arguments
dataset=$1
database=$2

#Preparing the output location, and other variables
inputdataset=input/AminoAcids/$database/$dataset.faa
outfolder=output/AminoAcids/$database
mkdir -p $outfolder
mkdir -p logs/$database
outdataset=$outfolder/$dataset.faa

#Running MAFFT-Homologs
mafft-homologs.rb -l $(readlink -m $inputdataset) > $(readlink -m $outdataset) 2> logs/$database/$dataset.log


#!/bin/bash

#The input arguments
dataset=$1
database=$2

#Addresses
inputdataset=input/AminoAcids/$database/$dataset.faa
outfolder=output/AminoAcids/$database/$dataset

if [ ! -d $outfolder ]; then

	#creating a folder for each dataset, so that TCoffee genereates the files inside that folder.
	mkdir -p $outfolder

	cd $outfolder
	outfolder=$(pwd)
	cd - > /dev/null 2>&1

	#copying the input to the folder as well.
	cp $inputdataset $outfolder
	cd $outfolder
	
	#Running t_coffee in the accurate mode.
	t_coffee $dataset.faa -mode accurate
fi

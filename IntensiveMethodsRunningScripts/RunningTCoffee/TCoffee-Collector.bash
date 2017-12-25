#!/bin/bash

CollectionFolder=OutAlignments
for Database in Sisyphus MattBench Homstrad BAliBase;do
	echo $Database
	mkdir -p $CollectionFolder/AminoAcids/$Database

	find ./output/AminoAcids/$Database -type f -iname "*.aln" -print0 | while IFS= read -r -d $'\0' line; do
	    datasetname=${line##*/}
	    datasetname=${datasetname%.*}
	    echo $datasetname
		#Running the conversion to fasta command using the t_coffee package.
	    t_coffee -other_pg seq_reformat -in=$(readlink -m $line) -output fasta_aln > $CollectionFolder/AminoAcids/$Database/$datasetname.faa
	    cp $line $CollectionFolder/AminoAcids/$Database/$datasetname.faa
	done

done

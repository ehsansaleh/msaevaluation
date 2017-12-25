#!/bin/bash

#Getting the benchmark name, either from input or from a default value
if [ -z "$1" ]; then
	Database=Sisyphus
else
	Database=$1
fi

#The number of datasets that need to run on a single node
jobpernode=30

#Getting the number of datasets in the benchmark
datasetnum=$(ls input/AminoAcids/$Database/*.faa | wc -l)

jobcount=$(python -c "from math import ceil; print int(ceil($datasetnum/float($jobpernode)))")

#Submitting the jobs in a for loop
for (( c=0; c<$jobcount; c++ ));do
	qsub MomNode-Controller.pbs -N MAFFTH-$Database-$c -v jobpernode=$jobpernode,database=$Database,arrid=$c
done

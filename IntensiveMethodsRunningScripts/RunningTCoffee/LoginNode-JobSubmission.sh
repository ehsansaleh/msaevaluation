#!/bin/bash

#Database is the same as benchmark
if [ -z "$1" ]; then
	Database=Sisyphus
else
	Database=$1
fi

#The number of datasets that need to run on the same node
jobpernode=1

datasetnum=$(ls input/AminoAcids/$Database/*.faa | wc -l)

#Computing the number of required jobs(Number of Datasets divided by jobpernode variable)
jobcount=$(python -c "from math import ceil; print int(ceil($datasetnum/float($jobpernode)))")

#Sending the jobs to the queue
for (( c=0; c<$jobcount; c++ ));do
	qsub MomNode-Controller.pbs -N TCoffee-$Database-$c -v jobpernode=$jobpernode,database=$Database,arrid=$c
done





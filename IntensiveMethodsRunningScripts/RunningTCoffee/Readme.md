This folder is a sample script for running TCoffee on an HPC Platform such as the BlueWaters.

Here is a simplistic view of the chain of calls.

User --> LoginNode-JobSubmission.sh --> MomNode-Controller.pbs --> ComputationNode-Runner.sh

Then you have to call TCoffee-Collector.bash in order to collect the final results.

Here is a short description of what the files are doing:

1) LoginNode-JobSubmission.sh: 
    This script prepares the job configurations that are necessary for running multiple instances of TCoffee on each computation node.
    This script runs on the login nodes, and just submits the jobs through the PBS/qsub system.

2) MomNode-Controller.pbs: 
    This script just runs the "ComputationNode-Runner.sh" script multiple times using aprun (i.e. a replacement for mpirun).
    
3) ComputationNode-Runner.sh: 
    This script takes as a arguments the name of the dataset and the benchmark. Then, it runs TCoffee on the dataset.
	
4) TCoffee-Collector.bash: 
	This script converts the output alignments to FASTA format, and collects them in one folder.
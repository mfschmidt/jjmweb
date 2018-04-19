#!/bin/bash

#SBATCH -p all               # The only partition is 'all' (as of 4/2018)
#SBATCH -N 1                 # We only need one node
#SBATCH -n 1                 # We only need one core
#SBATCH --mem 1024M          # Allocate a gigabyte, probably overkill
#SBATCH -t 0                 # No time limit should be imposed
#SBATCH -o jjmweb.%N.%j.out  # STDOUT
#SBATCH -e jjmweb.%N.%j.err  # STDERR

singularity run --bind /opt/jjmdb /home/webrunner/jjmweb.simg

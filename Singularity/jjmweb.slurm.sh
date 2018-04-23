#!/bin/bash

#SBATCH -p all               # The only partition is 'all' (as of 4/2018)
#SBATCH -N 1                 # We only need one node
#SBATCH -n 1                 # We only need one core
#SBATCH --mem 1024M          # Allocate a gigabyte, probably overkill
#SBATCH -t 0                 # No time limit should be imposed
#SBATCH -o $HOME/slurmlogs/jjmweb.%N.%j.out  # STDOUT
#SBATCH -e $HOME/slurmlogs/jjmweb.%N.%j.err  # STDERR

mkdir -p $HOME/slurmlogs

singularity run --bind /opt/jjmdb /home/webrunner/jjmweb.simg

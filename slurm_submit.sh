#!/bin/bash
#SBATCH --mail-user#jsingh3@wpi.edu
#SBATCH --mail-type=ALL

#SBATCH -N 1
#SBATCH -n 8
#SBATCH --mem 60g
#SBATCH -J "HACMan_Train"
#SBATCH -p short
#SBATCH -t 02:00:00
#SBATCH --gres=gpu:1

module load python/3.8
module load cuda11.2/blas
module load cuda11.2/toolkit
module load libx11/1.7.0/hlcc3e6

source /home/jsingh3/minicoda3/bin/activate
conda activate hacman

wandb login $WANDB_API_KEY

python scripts/run.py \
--env simple_env \
--algo HybridTD3

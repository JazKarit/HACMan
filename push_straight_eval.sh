#!/bin/bash
#SBATCH --mail-user#jsingh3@wpi.edu
#SBATCH --mail-type=ALL

#SBATCH -A rbe577
#SBATCH -N 2
#SBATCH -n 24
#SBATCH --mem 80g
#SBATCH -J "HACMan_rotate_eval"
#SBATCH -p academic
#SBATCH -t 2:00:00
#SBATCH --gres=gpu:1

module load python/3.8
module load cuda11.2/blas
module load cuda11.2/toolkit
module load libx11/1.7.0/hlcc3e6

source /home/jsingh3/minicoda3/bin/activate
conda activate hacman

LD_PRELOAD="" MUJOCO_PY_FORCE_CPU=1 python scripts/run.py \
--env push_straight_env \
--gradient_steps 0 \
--ExpID 8109 \
--max_episode_steps 1 \
--initial_timesteps 0 \
--eval_n_envs 8 \
--eval 200 \
--load_ckpt scripts/results/Exp2016-tmp-0/model-ccpg4c79/rl_model_latest \
--object_name bowl_Threshold_Porcelain_Serving_Bowl_Coupe_White_M 

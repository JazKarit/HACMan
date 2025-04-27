#!/bin/bash
#SBATCH --mail-user#jsingh3@wpi.edu
#SBATCH --mail-type=ALL

#SBATCH -A rbe577
#SBATCH -N 2
#SBATCH -n 24
#SBATCH --mem 100g
#SBATCH -J "HACMan_push_straight_train"
#SBATCH -p academic
#SBATCH -t 10:00:00
#SBATCH --gres=gpu:1

module load python/3.8
module load cuda11.2/blas
module load cuda11.2/toolkit
module load libx11/1.7.0/hlcc3e6

source /home/jsingh3/minicoda3/bin/activate
conda activate hacman

LD_PRELOAD="" MUJOCO_PY_FORCE_CPU=1 python scripts/run.py \
--env push_straight_env \
--clamp_critic_max 0 \
--clamp_critic_min -20 \
--ExpID 4001 \
--max_episode_steps 2 \
--initial_timesteps 1000 \
--train_n_envs 8 \
--eval_n_envs 4

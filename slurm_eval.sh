#!/bin/bash
#SBATCH --mail-user#jsingh3@wpi.edu
#SBATCH --mail-type=ALL

#SBATCH -A rbe577
#SBATCH -N 2
#SBATCH -n 24
#SBATCH --mem 80g
#SBATCH -J "HACMan_push_straight_eval"
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
--ExpID 5002 \
--max_episode_steps 2 \
--initial_timesteps 0 \
--eval_n_envs 4 \
--eval 100 \
--record_video \
--record_from_cam agentview \
--load_ckpt scripts/results/Exp4002-tmp-0/model-kkkqej9f/rl_model_latest

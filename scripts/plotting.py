import matplotlib.pyplot as plt

# Data provided: mean ± stddev
data = {
    "Push Straight": {"mean": 0.430, "std": 0.097},
    "Roll": {"mean": 0.750, "std": 0.085},
    "Spin": {"mean": 0.470, "std": 0.069},
}

def sort_by_mean(data, key=None, descending=False):
    """
    Sort a dictionary of items by the mean value of a specified key (e.g., 'succ' or 'mean_reward').

    Args:
        data (dict): The input dictionary.
        key (str): The key to sort by ('succ' or 'mean_reward').
        descending (bool): Whether to sort in descending order.

    Returns:
        list: A list of (name, stats) tuples sorted by mean value.
    """
    if key == None:
        return sorted(data.items(), key=lambda item: item[1]["mean"], reverse=descending)
    return sorted(data.items(), key=lambda item: item[1][key]["mean"], reverse=descending)


data_spin = {
    "Cube": {
        "succ": {"mean": 0.610, "std": 0.068},
        "mean_reward": {"mean": -0.27, "std": 0.33482222620320473}
    },
     "Pill Bottle": {
        "succ": {"mean": 0.600, "std": 0.068},
        "mean_reward": {"mean": -0.31, "std": 0.3386657274741616}
    },
    "Tape": {
        "succ": {"mean": 0.560, "std": 0.069},
        "mean_reward": {"mean": -0.32, "std": 0.362172206293039}
    },
    "Lunch": {
        "succ": {"mean": 0.485, "std": 0.069},
        "mean_reward": {"mean": -0.36, "std": 0.37710728974672575}
    },
    "Planter 1": {
        "succ": {"mean": 0.485, "std": 0.069},
        "mean_reward": {"mean": -0.43, "std": 0.38622216108659063}
    },
    "Planter 2": {
        "succ": {"mean": 0.405, "std": 0.068},
        "mean_reward": {"mean": -0.49, "std": 0.3935859618796082}
    },
    "Mug": {
        "succ": {"mean": 0.290, "std": 0.063},
        "mean_reward": {"mean": -0.56, "std": 0.39410865407163026}
    },
   
}


data_push_straight = {
    "Cube": {
        "succ": {"mean": 0.955, "std": 0.029},
        "mean_reward": {"mean": -0.02, "std": 0.09273114786555688}
    },
    "Pill Bottle": {
        "succ": {"mean": 0.135, "std": 0.047},
        "mean_reward": {"mean": -0.27, "std": 0.2509559702960003}
    },
    "Tape": {
        "succ": {"mean": 0.465, "std": 0.069},
        "mean_reward": {"mean": -0.17, "std": 0.2123058311977087}
    },
    "Lunch": {
        "succ": {"mean": 0.825, "std": 0.053},
        "mean_reward": {"mean": -0.06, "std": 0.16098061686136617}
    },
    "Planter 1": {
        "succ": {"mean": 0.280, "std": 0.062},
        "mean_reward": {"mean": -0.32, "std": 0.29713711185890596}
    },
    "Planter 2": {
        "succ": {"mean": 0.245, "std": 0.060},
        "mean_reward": {"mean": -0.24, "std": 0.24681396195654}
    },
    "Mug": {
        "succ": {"mean": 0.625, "std": 0.067},
        "mean_reward": {"mean": -0.17, "std": 0.2849300135922265}
    },
}

data_roll = {
    "Cube": {
        "succ": {"mean": 0.850, "std": 0.049},
        "mean_reward": {"mean": -0.40, "std": 0.6587603731378714}
    },
    "Pill Bottle": {
        "succ": {"mean": 0.845, "std": 0.050},
        "mean_reward": {"mean": -0.22, "std": 0.33510767364604527}
    },
    "Tape": {
        "succ": {"mean": 0.750, "std": 0.060},
        "mean_reward": {"mean": -0.56, "std": 0.7418453548717897}
    },
    "Lunch": {
        "succ": {"mean": 0.520, "std": 0.069},
        "mean_reward": {"mean": -1.04, "std": 0.8801725257106143}
    },
    "Planter 1": {
        "succ": {"mean": 0.740, "std": 0.061},
        "mean_reward": {"mean": -0.45, "std": 0.42866298434407746}
    },
    "Planter 2": {
        "succ": {"mean": 0.790, "std": 0.056},
        "mean_reward": {"mean": -0.47, "std": 0.5407921840029458}
    },
    "Mug": {
        "succ": {"mean": 0.825, "std": 0.053},
        "mean_reward": {"mean": -0.49, "std": 0.6204269665896535}
    },
    "Bowl": {
        "succ": {"mean": 0.050, "std": 0.030},
        "mean_reward": {"mean": -1.88, "std": 0.4336866582841944}
    }
}

import numpy as np



# Step 1: Get the task order from data_push_straight
# sorted_push = sort_by_mean(data_push_straight, key="succ", descending=True)
# tasks = [name for name, _ in sorted_push]

# # Step 2: Function to extract mean/std for a given task list
# def extract_stats(data, tasks):
#     means, stds = [], []
#     for task in tasks:
#         if task in data:
#             means.append(data[task]["succ"]["mean"])
#             stds.append(data[task]["succ"]["std"])
#         else:
#             means.append(np.nan)
#             stds.append(0)
#     return means, stds

# # Step 3: Extract data for each dataset in push order
# means_push, stds_push = extract_stats(data_push_straight, tasks)
# means_roll, stds_roll = extract_stats(data_roll, tasks)
# means_spin, stds_spin = extract_stats(data_spin, tasks)

# # Step 4: Plot grouped bars
# x = np.arange(len(tasks))
# width = 0.25

# fig, ax = plt.subplots(figsize=(10, 6))

# bars1 = ax.bar(x - width, means_push, width, yerr=stds_push, capsize=5, label='Push Straight', color='skyblue')
# bars2 = ax.bar(x,         means_roll, width, yerr=stds_roll, capsize=5, label='Roll', color='lightgreen')
# bars3 = ax.bar(x + width, means_spin, width, yerr=stds_spin, capsize=5, label='Spin', color='salmon')

# # Labels and formatting
# ax.set_ylabel("Success Rate")
# ax.set_xticks(x)
# ax.set_xticklabels(tasks)#, rotation=45, ha='right')
# ax.set_ylim(0, 1)
# ax.legend()
# plt.grid(axis='y', linestyle='--', alpha=0.6)
# plt.tight_layout()
# plt.show()




#Plotting a bar graph with error bars
fig, ax = plt.subplots()

sorted_data = sort_by_mean(data, descending=True)
print(sorted_data)
sorted_data = [sorted_data[2], sorted_data[0], sorted_data[1]]


# Extract task names, means, and standard deviations
tasks = [name for name, _ in sorted_data]
means = [stats["mean"] for _, stats in sorted_data]
stds = [stats["std"] for _, stats in sorted_data]

# Plotting
fig, ax = plt.subplots()
colors = ["skyblue","lightgreen", "salmon",]
bars = ax.bar(tasks, means, yerr=stds, capsize=10, color=colors)

ax.set_ylabel("Success Rate")
ax.set_ylim(0, 1)
ax.set_xticklabels(tasks)#, rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

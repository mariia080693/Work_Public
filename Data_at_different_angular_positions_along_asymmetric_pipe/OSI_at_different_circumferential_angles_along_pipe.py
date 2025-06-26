
import numpy as np
import matplotlib.pyplot as plt

def load_array(filename):
    return np.genfromtxt(filename, delimiter=',')

# Load all datasets
datasets = {
    "DoE_0_50": load_array('OSI_DOE0_DOS50.csv'),
    "DoE_30_50": load_array('OSI_DOE30_DOS50.csv'),
    "DoE_60_50": load_array('OSI_DOE60_DOS50.csv'),
    "DoE_80_50": load_array('OSI_DOE80_DOS50.csv'),
    "DoE_100_50": load_array('OSI_DOE100_DOS50.csv'),
    "DoE_80_40": load_array('OSI_DOE80_DOS40.csv'),
    "DoE_80_60": load_array('OSI_DOE80_DOS60.csv'),
    "DoE_80_75": load_array('OSI_DOE80_DOS75.csv'),
}

radians = np.deg2rad(45)

# Extracts OSI data at different angles from the input array
def extract_osi(arr):
    
    arr = arr[1:,:].round(5)
    x_locs = np.unique(arr[:,1])

    def extract_at_angle(arr, angle_col, is_max=True):
        func = np.max if is_max else np.min
        return arr[arr[:,angle_col] == func(arr[:,angle_col])]

    angle_data = {k: [] for k in [0, 45, 90, 135, 180]}

    for x in x_locs:
        
        section = arr[arr[:,1] == x]

        angle_data[0].append(extract_at_angle(section, 2, True)[0,0] if section.size else np.nan)
        angle_data[90].append(extract_at_angle(section, 3, True)[0,0] if section.size else np.nan)
        angle_data[180].append(extract_at_angle(section, 2, False)[0,0] if section.size else np.nan)

        cos_val = np.cos(radians) * np.max(section[:,3])
        close_vals = section[np.isclose(section[:,3], cos_val, rtol=0, atol=1e-3)]
        if close_vals.size:
            angle_data[45].append(extract_at_angle(close_vals, 2, True)[0,0])
            angle_data[135].append(extract_at_angle(close_vals, 2, False)[0,0])
        else:
            angle_data[45].append(np.nan)
            angle_data[135].append(np.nan)

    return [x_locs] + [np.array(angle_data[a]).round(5) for a in [0, 45, 90, 135, 180]]

# Compute OSI data for each dataset
processed_data = {name: extract_osi(arr) for name, arr in datasets.items()} # name - key; arr - value

def plot_dataset(ax, x, ys, labels, styles):
    for y, label, style in zip(ys, labels, styles):
        ax.plot((x - x[0]) * 1000, y, style, markevery=0.1, label=label, linewidth=2)

def add_stenosis_overlay(ax):
    ax.plot([13.6, 13.6], [-50, 1000], 'k--')
    ax.plot([20.4, 20.4], [-50, 1000], 'k--')
    ax.plot([13.6, 20.4], [-50, -50], 'k--')
    ax.plot([13.6, 20.4], [1000, 1000], 'k--', label="stenosis area")

# Plotting
if __name__ == "__main__":
    fig, axs = plt.subplots(5, 2, figsize=(20, 100))
    angles = [0, 45, 90, 135, 180]
    colors = ['k-', 'co-', 'g^-', 'ys-', 'bD-']
    dos_labels = ["DoE=0%", "DoE=30%", "DoE=60%", "DoE=80%", "DoE=100%"]
    dos80_labels = ["DoS=40%", "DoS=50%", "DoS=60%", "DoS=75%"]

    # Column 1: DoS=50%, varying DoE
    for i, angle in enumerate(angles):
        ax = axs[i, 0]
        ax.set_title(f"\u03B1 = {angle}°", fontsize=15, loc='left')
        plot_dataset(
            ax,
            processed_data["DoE_0_50"][0],
            [processed_data[f"DoE_{d}_50"][i+1] for d in [0, 30, 60, 80, 100]],
            dos_labels,
            colors
        )

    # Column 2: DoE=80%, varying DoS
    for i, angle in enumerate(angles):
        ax = axs[i, 1]
        ax.set_title(f"\u03B1 = {angle}°", fontsize=15, loc='left')
        plot_dataset(
            ax,
            processed_data["DoE_80_50"][0],
            [processed_data[f"DoE_80_{s}"][i+1] for s in [40, 50, 60, 75]],
            dos80_labels,
            colors[1:]  # start from second color to match legend
        )

    # Shared formatting
    for j in range(5):
        for i in range(2):
            ax = axs[j, i]
            add_stenosis_overlay(ax)
            ax.set_xlabel('${x}$ (mm)', fontsize=15)
            ax.set_ylabel('OSI', fontsize=15)
            ax.set_ylim([0, 0.5])
            ax.grid(True)

        axs[j, 0].set_xlim([0, 50])
        axs[j, 1].set_xlim([0, 102])

    axs[0, 0].legend(bbox_to_anchor=(0., 1.12, 1., .102), loc='lower left',
                    ncol=2, mode="expand", borderaxespad=0., fontsize=15)
    axs[0, 1].legend(bbox_to_anchor=(0., 1.12, 1., .102), loc='lower left',
                    ncol=2, mode="expand", borderaxespad=0., fontsize=15)

    plt.rc('xtick', labelsize=15)
    plt.rc('ytick', labelsize=15)

    plt.show()

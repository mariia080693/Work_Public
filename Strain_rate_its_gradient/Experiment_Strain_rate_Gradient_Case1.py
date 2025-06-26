import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.signal import argrelextrema
from findiff import FinDiff

plt.close('all')

Q12 = np.genfromtxt('Velocity_centerline_12.csv', delimiter=',')
Q50 = np.genfromtxt('Velocity_centerline_50.csv', delimiter=',')
Q200 = np.genfromtxt('Velocity_centerline_200.csv', delimiter=',')
Q600 = np.genfromtxt('Velocity_centerline_600.csv', delimiter=',')
Experiment = np.genfromtxt('Warwick_experiment.csv', delimiter=',')

# Preprocess data including shifting due to the stenosis region
def extract_velocity_and_position(data, position_idx):
    x = data[:, position_idx] * 1e6 - 3198
    u = data[:, 0]
    return x, u

Q12_x, Q12_u = extract_velocity_and_position(Q12, 4)
Q50_x, Q50_u = extract_velocity_and_position(Q50, 3)
Q200_x, Q200_u = extract_velocity_and_position(Q200, 4)
Q600_x, Q600_u = extract_velocity_and_position(Q600, 4)

def compute_derivatives(u, x, acc=4):
    dx = FinDiff(0, x, acc=acc)
    dudx = dx(u)
    dudxdx = dx(dudx)
    return dudx, dudxdx

Q12_dudx, Q12_dudxdx = compute_derivatives(Q12_u, Q12[:, 4])
Q50_dudx, Q50_dudxdx = compute_derivatives(Q50_u, Q50[:, 3])
Q200_dudx, Q200_dudxdx = compute_derivatives(Q200_u, Q200[:, 4])
Q600_dudx, Q600_dudxdx = compute_derivatives(Q600_u, Q600[:, 4])

# Experimental data
Experiment_x = Experiment[:, 0]
Exp_Q = {
    12.5: Experiment[:, 4],
    50: Experiment[:, 3],
    200: Experiment[:, 2],
    600: Experiment[:, 1]
}

# Strain rate vs experimental Ca2+
fig, ax = plt.subplots(figsize=(14, 10))  # wider plot
colors = ['g-', 'g-', 'g-', 'g-']
linewidths = [1, 2, 3, 4]
Q_values = [12.5, 50, 200, 600]
strain_data = [Q12_dudx, Q50_dudx, Q200_dudx, Q600_dudx]
x_data = [Q12_x, Q50_x, Q200_x, Q600_x]

for i, Q in enumerate(Q_values):
    ax.plot(x_data[i], strain_data[i], colors[i], label=f'Q = {Q} μL/min', linewidth=linewidths[i])

ax.set_xlabel('x (μm)', fontsize=25)
ax.set_ylabel('γ̇ ($s^{-1}$)', color='green', fontsize=25)
ax.axvline(300, linestyle='--', color='k', linewidth=1)
ax.axvline(620, linestyle='--', color='k', linewidth=1, label='hyperbolic section')
ax.set_xlim([0, 1000])
ax.set_ylim([-25000, 25000])
ax.grid(True)
ax.tick_params(labelsize=20)  # set both x and y ticks to same size

ax2 = ax.twinx()
for i, Q in enumerate(Q_values):
    ax2.plot(Experiment_x, Exp_Q[Q], 'b-', linewidth=linewidths[i])
ax2.set_ylabel("[Ca$^{2+}$]$_{c}$(nM)", color='blue', fontsize=25)
ax2.set_ylim([0, 250])
ax2.tick_params(labelsize=20)  # set y ticks to same size

fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, fontsize=20)

# Gradient of strain rate vs experimental Ca2+
fig, ax = plt.subplots(figsize=(14, 10))  # wider plot
strain_grad_data = [Q12_dudxdx, Q50_dudxdx, Q200_dudxdx, Q600_dudxdx]

for i, Q in enumerate(Q_values):
    ax.plot(x_data[i], strain_grad_data[i], 'r-', label=f'Q = {Q} μL/min', linewidth=linewidths[i])

ax.set_xlabel('x (μm)', fontsize=25)
ax.set_ylabel('dγ̇/dx ($(sm)^{-1}$)', color='red', fontsize=25)
ax.axvline(300, linestyle='--', color='k', linewidth=1)
ax.axvline(620, linestyle='--', color='k', linewidth=1)
ax.set_xlim([0, 1000])
ax.set_ylim([-2e9, 0.25e9])
ax.grid(True)
ax.tick_params(labelsize=20)  # set both x and y ticks to same size

ax2 = ax.twinx()
for i, Q in enumerate(Q_values):
    ax2.plot(Experiment_x, Exp_Q[Q], 'b-', linewidth=linewidths[i])
ax2.set_ylabel("[Ca$^{2+}$]$_{c}$(nM)", color='blue', fontsize=25)
ax2.set_ylim([0, 250])
ax2.tick_params(labelsize=20)  # set y ticks to same size

fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, fontsize=20)

plt.show()

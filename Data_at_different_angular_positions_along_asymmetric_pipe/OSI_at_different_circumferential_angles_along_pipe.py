
import numpy as np
import matplotlib.pyplot as plt
import math
#from PIL import Image
#from io import BytesIO

def load_array(filename):
    return np.genfromtxt(filename, delimiter=',')

arr0_50 = load_array('OSI_DOE0_DOS50.csv')
arr30_50 = load_array('OSI_DOE30_DOS50.csv')
arr60_50 = load_array('OSI_DOE60_DOS50.csv')
arr80_50 = load_array('OSI_DOE80_DOS50.csv')
arr100_50 = load_array('OSI_DOE100_DOS50.csv')
arr80_40 = load_array('OSI_DOE80_DOS40.csv')
arr80_60 = load_array('OSI_DOE80_DOS60.csv')
arr80_75 = load_array('OSI_DOE80_DOS75.csv')

radians = np.deg2rad(45)

def wss(arr):
    # Remove header row if present
    arr = arr[1:,:]
    arr = arr.round(decimals=5)
    unique_x_locs = np.unique(arr[:,1])

    angle_0, angle_45, angle_90, angle_135, angle_180 = [], [], [], [], []

    for x in unique_x_locs:
        arr1 = arr[arr[:,1] == x]

        arr1_0 = arr1[arr1[:,2] == np.max(arr1[:,2])]
        arr1_90 = arr1[arr1[:,3] == np.max(arr1[:,3])]
        arr1_180 = arr1[arr1[:,2] == np.min(arr1[:,2])]

        cos_val = np.cos(radians) * np.max(arr1[:,3])
        arr1_45_135 = arr1[np.round(arr1[:,3], 4) == np.round(cos_val, 4)]
        if arr1_45_135.size == 0:
            arr1_45_135 = arr1[np.round(arr1[:,3], 3) == np.round(cos_val, 3)]
        arr1_45 = arr1_45_135[arr1_45_135[:,2] == np.max(arr1_45_135[:,2])]
        arr1_135 = arr1_45_135[arr1_45_135[:,2] == np.min(arr1_45_135[:,2])]

        angle_0.append(arr1_0[0,0] if arr1_0.size else np.nan)
        angle_45.append(arr1_45[0,0] if arr1_45.size else np.nan)
        angle_90.append(arr1_90[0,0] if arr1_90.size else np.nan)
        angle_135.append(arr1_135[0,0] if arr1_135.size else np.nan)
        angle_180.append(arr1_180[0,0] if arr1_180.size else np.nan)

    return [unique_x_locs] + [np.array(a).round(5) for a in [angle_0, angle_45, angle_90, angle_135, angle_180]]

arr_0_50 = wss(arr0_50)
arr_30_50 = wss(arr30_50)
arr_60_50 = wss(arr60_50)
arr_80_50 = wss(arr80_50)
arr_100_50 = wss(arr100_50)
arr_80_40 = wss(arr80_40)
arr_80_60 = wss(arr80_60)
arr_80_75 = wss(arr80_75)


'''
# PLOT FOR ONE CASE ONLY

fig = plt.figure(figsize = (10,10))
plt.plot([13.6,13.6],[-50,1000],'k--', [20.4,20.4],[-50, 1000],'k--', [13.6,20.4],[-50,-50],'k--')
plt.plot( [13.6,20.4],[1000,1000],'k--', label="stenosis area") 
plt.plot( (arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[1], 'r.-',markevery=0.1, label="\u03B1 = 0°",linewidth=2) 
plt.plot( (arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[2],'co-',markevery=0.1, label="\u03B1 = 45°",linewidth=2) 
plt.plot( (arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[3], 'g^-',markevery=0.1, label="\u03B1 = 90°",linewidth=2) 
plt.plot( (arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[4] ,'ys-',markevery=0.1, label="\u03B1 = 135°",linewidth=2) 
plt.plot( (arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[5] ,'bD-',markevery=0.1, label="\u03B1 = 180°",linewidth=2) 
plt.plot( (arr_0_50[0]-arr_0_50[0][0])*1000, arr_0_50[1], 'k-', label="DoE=0%",linewidth=2)
 
plt.xlabel('${x}$ (mm)', fontsize = 35)
plt.ylabel('OSI', fontsize = 35)
plt.grid('both')
plt.xlim([0, 50])
plt.ylim([0, 0.5])
plt.legend(fontsize=25)
y_ticks = np.arange(0, 0.6, 0.1) 
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.yticks(y_ticks) 
plt.legend(bbox_to_anchor=(0., 1.12, 1., .102), loc='lower left',ncol=2, mode="expand", borderaxespad=0., fontsize=25)

'''


if __name__ == "__main__":
    fig, axs = plt.subplots(5, 2, figsize=(20,100))

    # DOS50 different DOE
    axs[0,0].set_title("\u03B1 = 0°", fontsize=15, loc='left')
    axs[0,0].plot((arr_0_50[0]-arr_0_50[0][0])*1000, arr_0_50[1], 'k-', markevery=0.1, label="DoE=0%", linewidth=2)
    axs[0,0].plot((arr_30_50[0]-arr_30_50[0][0])*1000, arr_30_50[1], 'co-', markevery=0.1, label="DoE=30%", linewidth=2)
    axs[0,0].plot((arr_60_50[0]-arr_60_50[0][0])*1000, arr_60_50[1], 'g^-', markevery=0.1, label="DoE=60%", linewidth=2)
    axs[0,0].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[1], 'ys-', markevery=0.1, label="DoE=80%", linewidth=2)
    axs[0,0].plot((arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[1], 'bD-', markevery=0.1, label="DoE=100%", linewidth=2)

    axs[1,0].set_title("\u03B1 = 45°", fontsize=15, loc='left')
    axs[1,0].plot((arr_0_50[0]-arr_0_50[0][0])*1000, arr_0_50[2], 'k-', markevery=0.1, label="DoE=0%", linewidth=2)
    axs[1,0].plot((arr_30_50[0]-arr_30_50[0][0])*1000, arr_30_50[2], 'co-', markevery=0.1, label="DoE=30%", linewidth=2)
    axs[1,0].plot((arr_60_50[0]-arr_60_50[0][0])*1000, arr_60_50[2], 'g^-', markevery=0.1, label="DoE=60%", linewidth=2)
    axs[1,0].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[2], 'ys-', markevery=0.1, label="DoE=80%", linewidth=2)
    axs[1,0].plot((arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[2], 'bD-', markevery=0.1, label="DoE=100%", linewidth=2)

    axs[2,0].set_title("\u03B1 = 90°", fontsize=15, loc='left')
    axs[2,0].plot((arr_0_50[0]-arr_0_50[0][0])*1000, arr_0_50[3], 'k-', markevery=0.1, label="DoE=0%", linewidth=2)
    axs[2,0].plot((arr_30_50[0]-arr_30_50[0][0])*1000, arr_30_50[3], 'co-', markevery=0.1, label="DoE=30%", linewidth=2)
    axs[2,0].plot((arr_60_50[0]-arr_60_50[0][0])*1000, arr_60_50[3], 'g^-', markevery=0.1, label="DoE=60%", linewidth=2)
    axs[2,0].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[3], 'ys-', markevery=0.1, label="DoE=80%", linewidth=2)
    axs[2,0].plot((arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[3], 'bD-', markevery=0.1, label="DoE=100%", linewidth=2)

    axs[3,0].set_title("\u03B1 = 135°", fontsize=15, loc='left')
    axs[3,0].plot((arr_0_50[0]-arr_0_50[0][0])*1000, arr_0_50[4], 'k-', markevery=0.1, label="DoE=0%", linewidth=2)
    axs[3,0].plot((arr_30_50[0]-arr_30_50[0][0])*1000, arr_30_50[4], 'co-', markevery=0.1, label="DoE=30%", linewidth=2)
    axs[3,0].plot((arr_60_50[0]-arr_60_50[0][0])*1000, arr_60_50[4], 'g^-', markevery=0.1, label="DoE=60%", linewidth=2)
    axs[3,0].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[4], 'ys-', markevery=0.1, label="DoE=80%", linewidth=2)
    axs[3,0].plot((arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[4], 'bD-', markevery=0.1, label="DoE=100%", linewidth=2)

    axs[4,0].set_title("\u03B1 = 180°", fontsize=15, loc='left')
    axs[4,0].plot((arr_0_50[0]-arr_0_50[0][0])*1000, arr_0_50[5], 'k-', markevery=0.1, label="DoE=0%", linewidth=2)
    axs[4,0].plot((arr_30_50[0]-arr_30_50[0][0])*1000, arr_30_50[5], 'co-', markevery=0.1, label="DoE=30%", linewidth=2)
    axs[4,0].plot((arr_60_50[0]-arr_60_50[0][0])*1000, arr_60_50[5], 'g^-', markevery=0.1, label="DoE=60%", linewidth=2)
    axs[4,0].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[5], 'ys-', markevery=0.1, label="DoE=80%", linewidth=2)
    axs[4,0].plot((arr_100_50[0]-arr_100_50[0][0])*1000, arr_100_50[5], 'bD-', markevery=0.1, label="DoE=100%", linewidth=2)

    # DOE80 different DOS
    axs[0,1].set_title("\u03B1 = 0°", fontsize=15, loc='left')
    axs[0,1].plot((arr_80_40[0]-arr_80_40[0][0])*1000, arr_80_40[1], 'co-', markevery=0.1, label="DoS=40%", linewidth=2)
    axs[0,1].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[1], 'g^-', markevery=0.1, label="DoS=50%", linewidth=2)
    axs[0,1].plot((arr_80_60[0]-arr_80_60[0][0])*1000, arr_80_60[1], 'ys-', markevery=0.1, label="DoS=60%", linewidth=2)
    axs[0,1].plot((arr_80_75[0]-arr_80_75[0][0])*1000, arr_80_75[1], 'bD-', markevery=0.1, label="DoS=75%", linewidth=2)

    axs[1,1].set_title("\u03B1 = 45°", fontsize=15, loc='left')
    axs[1,1].plot((arr_80_40[0]-arr_80_40[0][0])*1000, arr_80_40[2], 'co-', markevery=0.1, label="DoS=40%", linewidth=2)
    axs[1,1].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[2], 'g^-', markevery=0.1, label="DoS=50%", linewidth=2)
    axs[1,1].plot((arr_80_60[0]-arr_80_60[0][0])*1000, arr_80_60[2], 'ys-', markevery=0.1, label="DoS=60%", linewidth=2)
    axs[1,1].plot((arr_80_75[0]-arr_80_75[0][0])*1000, arr_80_75[2], 'bD-', markevery=0.1, label="DoS=75%", linewidth=2)

    axs[2,1].set_title("\u03B1 = 90°", fontsize=15, loc='left')
    axs[2,1].plot((arr_80_40[0]-arr_80_40[0][0])*1000, arr_80_40[3], 'co-', markevery=0.1, label="DoS=40%", linewidth=2)
    axs[2,1].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[3], 'g^-', markevery=0.1, label="DoS=50%", linewidth=2)
    axs[2,1].plot((arr_80_60[0]-arr_80_60[0][0])*1000, arr_80_60[3], 'ys-', markevery=0.1, label="DoS=60%", linewidth=2)
    axs[2,1].plot((arr_80_75[0]-arr_80_75[0][0])*1000, arr_80_75[3], 'bD-', markevery=0.1, label="DoS=75%", linewidth=2)

    axs[3,1].set_title("\u03B1 = 135°", fontsize=15, loc='left')
    axs[3,1].plot((arr_80_40[0]-arr_80_40[0][0])*1000, arr_80_40[4], 'co-', markevery=0.1, label="DoS=40%", linewidth=2)
    axs[3,1].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[4], 'g^-', markevery=0.1, label="DoS=50%", linewidth=2)
    axs[3,1].plot((arr_80_60[0]-arr_80_60[0][0])*1000, arr_80_60[4], 'ys-', markevery=0.1, label="DoS=60%", linewidth=2)
    axs[3,1].plot((arr_80_75[0]-arr_80_75[0][0])*1000, arr_80_75[4], 'bD-', markevery=0.1, label="DoS=75%", linewidth=2)

    axs[4,1].set_title("\u03B1 = 180°", fontsize=15, loc='left')
    axs[4,1].plot((arr_80_40[0]-arr_80_40[0][0])*1000, arr_80_40[5], 'co-', markevery=0.1, label="DoS=40%", linewidth=2)
    axs[4,1].plot((arr_80_50[0]-arr_80_50[0][0])*1000, arr_80_50[5], 'g^-', markevery=0.1, label="DoS=50%", linewidth=2)
    axs[4,1].plot((arr_80_60[0]-arr_80_60[0][0])*1000, arr_80_60[5], 'ys-', markevery=0.1, label="DoS=60%", linewidth=2)
    axs[4,1].plot((arr_80_75[0]-arr_80_75[0][0])*1000, arr_80_75[5], 'bD-', markevery=0.1, label="DoS=75%", linewidth=2)


    for j in range(5):
        for i in range(2):
            axs[j,i].plot([13.6,13.6],[-50,1000],'k--', [20.4,20.4],[-50, 1000],'k--', [13.6,20.4],[-50,-50],'k--')
            axs[j,i].plot([13.6,20.4],[1000,1000],'k--', label="stenosis area")
            axs[j,i].set_xlabel('${x}$ (mm)', fontsize=15)
            axs[j,i].set_ylabel('OSI', fontsize=15)
            axs[j,i].set_ylim([0, 0.5])
            axs[j,i].grid('both')
        axs[j,0].set_xlim([0,50])
        axs[j,1].set_xlim([0,102])

    axs[0,0].legend(bbox_to_anchor=(0., 1.12, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0., fontsize=15)
    axs[0,1].legend(bbox_to_anchor=(0., 1.12, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0., fontsize=15)

    plt.rc('xtick', labelsize=15)
    plt.rc('ytick', labelsize=15)

    plt.show()


import matplotlib.pyplot as plt
import numpy as np

plt.close('all')


arr = np.genfromtxt('OSI_puls_0_50.csv', delimiter=',')
arr1 = np.genfromtxt('OSI_puls_30_50.csv', delimiter=',')
arr2 = np.genfromtxt('OSI_puls_60_50.csv', delimiter=',')
arr3 = np.genfromtxt('OSI_puls_80_50.csv', delimiter=',')
arr4 = np.genfromtxt('OSI_puls_100_50.csv', delimiter=',')


# Function performs spatial averaging of OSI values
def osi(arr):
    arr = arr[1:, :]  # remove header row if present
    x_locs = arr[:, 1].round(5)
    osi_vals = arr[:, 0]
    
    unique_x_locs = np.unique(x_locs)
    osi_circ = []
    osi_circ = np.array([np.mean(osi_vals[x_locs == x]) for x in unique_x_locs])   
    
    return [unique_x_locs, osi_circ]


osip_0_50 = np.array(osi(arr)); osip_30_50 = np.array(osi(arr1)); osip_60_50 = np.array(osi(arr2));
osip_80_50 = np.array(osi(arr3)); osip_100_50 = np.array(osi(arr4))


#Plotting
plt.figure(figsize = (10,8))

plt.plot(osip_0_50[0,:]-15, osip_0_50[1,:], 'r-', label="${DoE}$=0%", linewidth=3)
plt.plot(osip_30_50[0,:]-15, osip_30_50[1,:], 'c-', label="${DoE}$=30%", linewidth=3)
plt.plot(osip_60_50[0,:]-15, osip_60_50[1,:], 'g-', label="${DoE}$=60%", linewidth=3)
plt.plot(osip_80_50[0,:]-15, osip_80_50[1,:], 'y-', label="${DoE}$=80%", linewidth=3)
plt.plot(osip_100_50[0,:]-15, osip_100_50[1,:], 'b-', label="${DoE}$=100%", linewidth=3)

plt.plot([4,4],[-50,1000],'k--', [6,6],[-50, 1000],'k--', [4,6],[-50,-50],'k--')
plt.plot( [4,6],[1000,1000],'k--', label="stenosis area")
plt.xlabel('${x/D}$', fontsize = 20)
plt.ylabel(r'${OSI}$', fontsize = 20)
plt.grid()
plt.legend(fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim([0, 30])
plt.ylim([0, 0.5])
y_ticks = np.arange(0, 0.6, 0.1 )
plt.yticks(y_ticks)
plt.show()
 

 

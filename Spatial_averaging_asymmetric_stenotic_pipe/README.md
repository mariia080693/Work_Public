# Spatial Averaging of OSI in Asymmetric Pipe

This repository contains a script to process and visualize Oscillatory Shear Index (OSI) data from multiple CSV files, each corresponding to a different Degree of Eccentricity (DoE) in a stenotic pipe. The script performs spatial averaging along the axial direction and generates comparative plots.

## Files Used

- `OSI_puls_0_50.csv`
- `OSI_puls_30_50.csv`
- `OSI_puls_60_50.csv`
- `OSI_puls_80_50.csv`
- `OSI_puls_100_50.csv`

Each CSV file is expected to contain OSI values and corresponding spatial coordinates.

## How It Works

1. **Data Loading**  
   The script loads OSI data from CSV files using `numpy.genfromtxt`.

2. **Spatial Averaging**  
   For each dataset, OSI values are averaged along the axial direction (x) by grouping values with the same coordinate.

3. **Plotting**  
   The averaged OSI values are plotted as a function of normalized position (x/D). A shaded region highlights the stenosis area.


# OSI Angle Analysis Along Asymmetric Pipe

This repository contains a Python script for processing and visualizing Oscillatory Shear Index (OSI) data at different circumferential angles along a pipe with varying degrees of eccentricity (DoE) and stenosis (DoS). The analysis is based on CSV datasets representing OSI values at multiple spatial and angular positions.

## Features

- **Loads OSI data** from multiple CSV files for different DoE and DoS conditions.
- **Extracts OSI values** at five angular positions (0°, 45°, 90°, 135°, 180°) for each spatial x-location along the pipe.
- **Plots comparative OSI profiles** for:
  - Varying DoE at fixed DoS (left column)
  - Varying DoS at fixed DoE=80% (right column)
- **Highlights stenosis region** on all plots for clear visualization.

## File Structure

- `New_OSI_at_different_circumferential_angles_along_pipe.py` – Main analysis and plotting script.
- `OSI_DOE*_DOS*.csv` – Input data files for different DoE and DoS combinations.
- `README.md` – This documentation.

## How It Works

1. **Data Loading:**  
   The script loads all relevant CSV files into NumPy arrays.

2. **Data Extraction:**  
   For each dataset, the script extracts OSI values at the specified angles and all x-locations using the `extract_osi` function.

3. **Plotting:**  
   - Generates a 5×2 grid of subplots:
     - **Left column:** OSI profiles at different DoE (0%, 30%, 60%, 80%, 100%) for DoS=50%.
     - **Right column:** OSI profiles at different DoS (40%, 50%, 60%, 75%) for DoE=80%.
   - Each row corresponds to a different angle (0°, 45°, 90°, 135°, 180°).
   - The stenosis region is overlaid on each plot.

4. **Customization:**  
   - Axis labels, legends, and grid are formatted for clarity.
   - X-axis is converted to millimeters.

## Usage

1. **Install dependencies:**
   ```sh
   pip install numpy matplotlib

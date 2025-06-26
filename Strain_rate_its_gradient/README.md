# Strain Rate and Calcium Response Plotting

This script loads velocity and experimental calcium data for four different flow rates, processes the data, and visualizes the relationship between flow-induced strain rates and calcium response along the vessel centerline.

## What the Code Does

- Loads velocity profile data and experimental calcium measurements from CSV files.
- Extracts and shifts position data to align with the stenosis region.
- Calculates the strain rate (velocity gradient) and its spatial gradient using high-accuracy finite differences.
- Plots:
  - Strain rate vs. position, overlaid with experimental calcium concentration for each flow rate.
  - Gradient of strain rate vs. position, also overlaid with calcium data.
- Helps visualize how mechanical forces (strain rate and its gradient) relate to biological response (calcium signaling) in the experiment.

## Usage

1. Ensure the following CSV files are in the same directory:
    - `Velocity_centerline_12.csv`
    - `Velocity_centerline_50.csv`
    - `Velocity_centerline_200.csv`
    - `Velocity_centerline_600.csv`
    - `Warwick_experiment.csv`
2. Run:
    ```sh
    python New_Experiment_Strain_rate_Gradient_Case1.py
    ```
3. Two plots will be shown:
    - Strain rate and calcium response vs. position
    - Strain rate gradient and calcium response vs. position

## Output

Plots compare computed strain rates and their gradients with experimental calcium data for four flow rates, helping to interpret the relationship between flow mechanics and cellular response.

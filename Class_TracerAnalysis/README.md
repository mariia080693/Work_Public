# TracerAnalysis

**TracerAnalysis** is a Python class designed to analyze tracer data from probe simulations or experiments. 
It processes a CSV file, plots tracer concentration over time, and calculates mixing times based on a user-defined threshold.

---

## Features

- **Automatic data loading** from a specified CSV file
- **Plots tracer mass fractions** from multiple probes
- **Computes mixing time** for each probe and returns:
  - Individual mixing times
  - Average mixing time
  - Standard deviation

---

## Requirements

- Python 3.6+
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)

---

## File Format

The CSV file must follow this structure:

- **Rows 1–2:** Skipped (e.g., metadata or comments)
- **Row 3:** Column headers (e.g., `Probe1`, `Probe2`, ..., `Time`)
- **Row 4+:** Data values, separated by whitespace

**Example file name:** `tracer_github.csv`

---

## Output

- A plot showing tracer mass fraction vs. time for each probe
- Printed average mixing time

**Example Output:**
```
Average mixing time is 12.34
```

---

## Class Overview

### `TracerAnalysis(file_path)`

Initializes the class and loads data.

#### Methods

- **`plot_tracer_data(title='Tracer in the Probes', save_path=None)`**  
  Plots the tracer concentration over time.

- **`mixing_time(threshold=0.05)`**  
  Calculates the time when each probe reaches within the threshold of its final tracer value and stays within it.

  **Returns:**
  - `mixing_times`: list of individual mixing times
  - `average_mixing_time`: mean mixing time
  - `std_mixing_time`: standard deviation of mixing times

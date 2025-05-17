import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class TracerAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.header = None
        self.df = None
        self.probes = []
        self.time = None
        self._load_data()

    def _load_data(self):
        # Read header and full data
        self.header = pd.read_csv(self.file_path, sep='" "', skiprows=2, nrows=1, engine='python', header=None)
        self.df = pd.read_csv(self.file_path, skiprows=3, sep='\s+', engine='python', header=None)
        self.df.columns = self.header.iloc[0].values

        # Time is in the last column
        self.time = self.df.iloc[:, -1].to_numpy()

        # Probes are all columns except first and last
        self.probes = [self.df.iloc[:, i].to_numpy() for i in range(1, self.df.shape[1] - 1)]

    def plot_tracer_data(self, title='Tracer in the Probes', save_path=None):
        plt.figure(figsize=(10, 4))

        for idx, probe in enumerate(self.probes):
            plt.plot(self.time, probe, label=f'Probe {idx + 1}')
        
        plt.xlabel('Time (s)', fontsize=14)
        plt.ylabel('Tracer Mass Fraction', fontsize=14)
        plt.title(title, fontsize=16)
        plt.xlim(left=0, right=20)
        plt.ylim(bottom=0)

        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(loc='upper right', fontsize=14, framealpha=1)
        plt.grid(True)
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()
    
    def mixing_time(self, threshold=0.05):
        mixing_times = []

        for probe in self.probes:
             final_value = probe[-1]
             mixing_time_found = False
             for idx in range(len(self.time)):
                 rel_diff = np.abs((probe[idx:] - final_value) / final_value)
                 if np.all(rel_diff <= threshold):
                     mixing_times.append(self.time[idx])
                     mixing_time_found = True
                     break
        if not mixing_time_found:
            mixing_times.append(np.nan)  

        average_mixing_time = np.nanmean(mixing_times)
        std_mixing_time = np.nanstd(mixing_times)

        return mixing_times, average_mixing_time, std_mixing_time




# Example usage

if __name__ == "__main__":

    tracer = TracerAnalysis('tracer_github.csv')
    tracer.plot_tracer_data(title='Tracer')
    mix_times, av_mix_time, std_mix_time = tracer.mixing_time(threshold=0.05)
    print("Average mixing time is", av_mix_time)
 

    

    

    

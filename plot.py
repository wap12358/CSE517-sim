import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from scipy.stats import sem, t
from config import *

for rand_dist in ['exponential', 'uniform', 'deterministic']:
    # Read the CSV file
    data = pd.read_csv(f'./{rand_dist}.csv', header=None)

    # Set the confidence level
    confidence_level = 0.95

    # Initialize lists to store plot data
    service_rates = []
    means = []
    theoretical = []
    conf_intervals = []
    original_data = []

    # Loop through each row in the data
    for i in range(len(data)):
        arrival_rate = data.iloc[i, 0]  # Extract the arrival rate
        service_rate = data.iloc[i, 1]  # Extract the service rate
        avg_sojourn_times = data.iloc[i, 2:].astype(int)  # Convert experimental data to float

        service_rates.append(service_rate)
        means.append(np.mean(avg_sojourn_times))
        original_data.append(avg_sojourn_times)
        theoretical.append(float('inf') if arrival_rate >= service_rate else 2 * TIMESTAMP_PER_SECOND / (service_rate - arrival_rate))

    # Plot the results with error bars for confidence intervals
    plt.figure(figsize=(8, 6))
    plt.subplot(2, 1, 1)
    plt.plot(service_rates, means,
                 label="Mean Sojourn Time")
                 # label="Mean Sojourn Time with 95% Confidence Intervals")
    plt.plot(service_rates, theoretical, linestyle=':', marker='o', label='Theoretical Sojourn Time')
    plt.xlabel("Service Rate")
    plt.ylabel("Mean Sojourn Time (us)")
    plt.xlim([0, max(service_rates) + 2000])
    plt.ylim([min(means) / 10, max(means) * 10])
    plt.yscale('log')
    plt.title(f'{rand_dist}   Arrival_rate=10000')
    plt.legend()
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.boxplot(original_data, labels=service_rates)
    plt.xlabel("Service Rate")
    plt.ylabel("Mean Sojourn Time (us)")
    plt.ylim([min(means) / 10, max(means) * 10])
    plt.yscale('log')
    plt.grid()

    # Display the plot
    # plt.show()
    plt.savefig(f'./{rand_dist}.pdf')

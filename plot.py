import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from scipy.stats import sem, t
from config import *

for rand_dist in ['exponential', 'uniform', 'deterministic']:
    # Read the CSV file
    original_data = pd.read_csv(f'./{rand_dist}.csv', header=None)

    # Set the confidence level
    confidence_level = 0.95

    # Initialize lists to store plot data
    service_rates = []
    mean_sojourn = []
    mean_nr_item = []
    theoretical = []

    # Loop through each row in the data
    for i in range(len(original_data)):
        arrival_rate = original_data.iloc[i, 0]  # Extract the arrival rate
        service_rate = original_data.iloc[i, 1]  # Extract the service rate
        data = original_data.iloc[i, 2:].astype(float)  # Convert experimental data to float

        service_rates.append(service_rate)
        mean_sojourn.append(data[:len(data)//2])
        mean_nr_item.append(data[len(data)//2:])
        theoretical.append(float('inf') if arrival_rate >= service_rate else 2 * TIMESTAMP_PER_SECOND / (service_rate - arrival_rate))

    # Plot the results with error bars for confidence intervals
    plt.figure(figsize=(8, 6))
    plt.subplot(2, 1, 1)
    plt.boxplot(mean_sojourn, labels=[str(x//1000) + 'k' for x in service_rates], positions=service_rates, widths=1200)
    # plt.plot(service_rates, means,
    #              label="Mean Sojourn Time")
    #              # label="Mean Sojourn Time with 95% Confidence Intervals")
    plt.plot(service_rates, theoretical, linestyle=':', marker='o', label='Theoretical Sojourn Time (Poisson arrivals)')
    # plt.xlabel("Service Rate")
    plt.ylabel("Mean Sojourn Time (us)")
    plt.xlim([0, max(service_rates) + 2000])
    plt.ylim([min(list(min(x) for x in mean_sojourn)) / 10, max(list(min(x) for x in mean_sojourn)) * 10])
    plt.yscale('log')
    plt.title(f'{rand_dist}   Arrival_rate=10000')
    plt.legend()
    plt.grid()

    # plt.subplot(2, 1, 2)
    # plt.boxplot(mean_sojourn, labels=service_rates)
    # plt.xlabel("Service Rate")
    # plt.ylabel("Mean Sojourn Time (us)")
    # plt.ylim([min(means) / 10, max(means) * 10])
    # plt.yscale('log')
    # plt.grid()

    plt.subplot(2, 1, 2)
    plt.boxplot(mean_nr_item, labels=[str(x//1000) + 'k' for x in service_rates], positions=service_rates, widths=1200)
    plt.xlabel("Service Rate")
    plt.ylabel("Average # of Packets in the System")
    plt.xlim([0, max(service_rates) + 2000])
    plt.ylim([min(list(min(x) for x in mean_nr_item)) / 10, max(list(min(x) for x in mean_nr_item)) * 10])
    plt.yscale('log')
    plt.grid()

    # Display the plot
    # plt.show()
    plt.savefig(f'./{rand_dist}.svg')

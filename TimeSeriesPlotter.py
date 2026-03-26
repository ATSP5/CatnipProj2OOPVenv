import matplotlib.pyplot as plt
class TimeSeriesPlotter:
    def __init__(self):
        """
        Plotter initialization (no state needed, but kept for extensibility).
        """
        pass

    def plot_time_series_and_hist(self, values):
        """
        Plot a time series line chart and histogram for given values.

        Parameters:
            values (array-like): Time series values.
        """
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # Time series plot
        axes[0].plot(values)
        axes[0].set_title("Random Time Series")
        axes[0].set_xlabel("Time")
        axes[0].set_ylabel("Value")

        # Histogram
        axes[1].hist(values, bins=20)
        axes[1].set_title("Histogram of Values")
        axes[1].set_xlabel("Value")
        axes[1].set_ylabel("Frequency")

        plt.tight_layout()
        plt.show()
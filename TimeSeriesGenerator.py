import numpy as np
class TimeSeriesGenerator:
    def __init__(self, seed=None):
        """
        Initialize the generator with an optional random seed.
        """
        self.seed = seed
        if self.seed is not None:
            np.random.seed(self.seed)

    def generate_time_series(self, n_points=100):
        """
        Generate random time series data (random walk).

        Parameters:
            n_points (int): Number of data points.

        Returns:
            np.ndarray: Generated time series values.
        """
        return np.cumsum(np.random.randn(n_points))

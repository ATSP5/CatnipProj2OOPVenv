from TimeSeriesGenerator import TimeSeriesGenerator
from TimeSeriesPlotter import TimeSeriesPlotter
def main():
 data = TimeSeriesGenerator()
 parameter = TimeSeriesPlotter()

 data_1 = data.generate_time_series()
 parameter.plot_time_series_and_hist(data_1)
 print('Done')
if __name__=="__main__":
 main()
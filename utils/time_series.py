"""
This file contains time series-related useful functions.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_data_air_passengers() -> pd.DataFrame:
    """
    Data sourced from https://www.kaggle.com/datasets/ashfakyeafi/air-passenger-data-for-time-series-analysis.
    """
    time_series = pd.read_csv('my_datasets/time-series/AirPassengers.csv')
    time_series['Month'] = pd.to_datetime(time_series['Month'])
    return time_series


def plot_predictions(
	date_column: str,
	value_column: str,
	df_train: pd.DataFrame,
	df_test: pd.DataFrame,
	df_predictions: pd.DataFrame,
	title: str
	) -> None:
	"""
	Plot train, test labels, and test predictions results.
	Each of the three dataframes should have two columns - one date column
	(specified by the argument date_column) and one value column (specified
	by the argument value_column).
	Args:
		date_column (str):             Name of the column which contains the date value in datetime format.
		value_column (str):            Name of the column which contains the actual value, in numeric data type.
		df_train (pd.DataFrame):       DataFrame on which the forecasting model was trained.
		df_test (pd.DataFrame):        DataFrame with values for prediction testing.
		df_predictions (pd.DataFrame): DataFrame with predicted values for the dates in df_test DataFrame.
		title (str):                   Title of the plot.
	Returns:
		None
	"""
	train, test, predictions = df_train.copy(deep=True), df_test.copy(deep=True), df_predictions.copy(deep=True)
	train['data split'] = 'Train'
	test['data split'] = 'Test'
	predictions['data split'] = 'Prediction'
	sns.lineplot(
		data = pd.concat([train, test, predictions]),
		x = date_column,
		y = value_column,
		hue = 'data split'
	)
	plt.title(title)
	plt.show()
	return None



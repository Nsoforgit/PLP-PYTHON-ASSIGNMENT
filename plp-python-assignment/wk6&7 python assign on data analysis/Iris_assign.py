import pandas as pd  # Import the pandas library and give it the alias 'pd' for easier use
from sklearn.datasets import load_iris # Import the load_iris function from scikit-learn to load the Iris dataset
import matplotlib.pyplot as plt # Import matplotlib's pyplot module and give it the alias 'plt' for plotting

# Task 1: Load and Explore the Dataset
# --- Loading the dataset ---
# Load the Iris dataset using the load_iris function from scikit-learn
iris = load_iris()

# --- Convert the dataset to a Pandas DataFrame ---
# Create a Pandas DataFrame from the Iris data. This makes it easier to analyze and manipulate the data.
# 'data=iris.data' provides the numerical data (measurements)
# 'columns=iris.feature_names' provides the names for each measurement column
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add a 'target' column to the DataFrame. This column contains the species of each Iris flower as numerical labels (0, 1, 2).
iris_df['target'] = iris.target

# Add a 'target_names' column to the DataFrame. This column contains the actual names of the Iris species (setosa, versicolor, virginica) for better readability.
# We use a list comprehension to map the numerical target values to their corresponding species names.
iris_df['target_names'] = [iris.target_names[i] for i in iris_df['target']]

# --- Displaying the first few rows of the DataFrame ---
print("First 5 rows of the Iris dataset:")
# Use .head() to display the first 5 rows of the DataFrame to get a glimpse of the data
print(iris_df.head())

# --- Exploring dataset information ---
print("\nDataset Information:")
# Use .info() to get a concise summary of the DataFrame, including data types and non-null values
print(iris_df.info())

# --- Calculating summary statistics ---
print("\nSummary Statistics:")
# Use .describe() to calculate and display summary statistics (like mean, standard deviation, min, max, percentiles) for numerical columns
print(iris_df.describe())

# --- Checking for missing values ---
print("\nMissing Values:")
# Use .isnull().sum() to check for missing values in each column and count them.
# .isnull() creates a DataFrame of boolean values (True for missing, False for not missing)
# .sum() then sums up the True values (which are treated as 1) for each column, giving the count of missing values.
print(iris_df.isnull().sum())


# Task 2: Basic Data Analysis
# --- Basic Statistics (already done in Task 1's exploration with .describe()) ---
# Note: We already calculated basic statistics for numerical columns using .describe() in Task 1.
#       These statistics (mean, median, std, etc.) are part of basic data analysis.

# --- Grouping and calculating average Sepal Length per Species ---
print("\nAverage Sepal Length per Species:")
# Use .groupby('target_names') to group the DataFrame by the 'target_names' column (Iris species).
# Then, select the 'sepal length (cm)' column within each group and calculate the mean() for each group.
print(iris_df.groupby('target_names')['sepal length (cm)'].mean())

# --- Grouping and calculating average Petal Width per Species ---
print("\nAverage Petal Width per Species:")
# Similar to above, but calculate the mean of 'petal width (cm)' for each Iris species group.
print(iris_df.groupby('target_names')['petal width (cm)'].mean())

# --- Example of Aggregation: Mean and Median Sepal Length per Species ---
print("\nMean and Median Sepal Length per Species:")
# Use .agg(['mean', 'median']) to calculate multiple statistics (mean and median in this case) for 'sepal length (cm)' for each species group.
print(iris_df.groupby('target_names')['sepal length (cm)'].agg(['mean', 'median']))

# Findings/Observations will be added as comments at the end of the script, summarizing insights from Task 2 and 3.

# Task 3: Data Visualization
# --- Line Chart: Sepal Length Trend for Iris Setosa (adapted for Iris data) ---
# Filter the DataFrame to get data only for the 'setosa' species
setosa_data = iris_df[iris_df['target_names'] == 'setosa']
# Create a new figure for the plot, setting the figure size for better readability
plt.figure(figsize=(8, 6))
# Create a line plot: x-axis is the index of setosa data points (acting as 'imaginary time'), y-axis is 'sepal length (cm)'
plt.plot(setosa_data.index, setosa_data['sepal length (cm)'])
# Set the title of the plot
plt.title('Sepal Length Trend for Iris Setosa (Imaginary Time Series)')
# Set the label for the x-axis
plt.xlabel('Data Point Index (Imaginary Time)')
# Set the label for the y-axis
plt.ylabel('Sepal Length (cm)')
# Add a grid to the plot to make it easier to read values
plt.grid(True)
# Display the plot. This command opens a window showing the plot.
plt.show()

# --- Bar Chart: Average Petal Length per Species ---
# Calculate the average petal length for each Iris species using groupby and mean()
avg_petal_length_species = iris_df.groupby('target_names')['petal length (cm)'].mean()
# Create a new figure for the bar chart
plt.figure(figsize=(8, 6))
# Create a bar chart. x-axis is species names (index of avg_petal_length_species), y-axis is average petal lengths (values)
# Set colors for the bars for visual appeal.
plt.bar(avg_petal_length_species.index, avg_petal_length_species.values, color=['skyblue', 'lightcoral', 'lightgreen'])
# Set the title of the bar chart
plt.title('Average Petal Length per Iris Species')
# Set the label for the x-axis
plt.xlabel('Iris Species')
# Set the label for the y-axis
plt.ylabel('Average Petal Length (cm)')
# Display the bar chart.
plt.show()

# --- Histogram: Distribution of Petal Width ---
# Create a new figure for the histogram
plt.figure(figsize=(8, 6))
# Create a histogram to visualize the distribution of 'petal width (cm)'
# 'bins=20' divides the data into 20 bins for the histogram. 'color' and 'edgecolor' set the appearance of the bars.
plt.hist(iris_df['petal width (cm)'], bins=20, color='lightseagreen', edgecolor='black')
# Set the title of the histogram
plt.title('Distribution of Petal Width (cm)')
# Set the label for the x-axis
plt.xlabel('Petal Width (cm)')
# Set the label for the y-axis
plt.ylabel('Frequency') # Y-axis for histogram typically represents frequency (count) of values in each bin.
# Display the histogram.
plt.show()

# --- Scatter Plot: Sepal Length vs Petal Length ---
# Create a new figure for the scatter plot
plt.figure(figsize=(8, 6))
# Create a scatter plot to visualize the relationship between 'sepal length (cm)' (x-axis) and 'petal length (cm)' (y-axis)
# 'color' sets the color of the points, 'alpha' sets transparency (0.7 for semi-transparent points).
plt.scatter(iris_df['sepal length (cm)'], iris_df['petal length (cm)'], color='purple', alpha=0.7)
# Set the title of the scatter plot
plt.title('Scatter Plot: Sepal Length vs Petal Length')
# Set the label for the x-axis
plt.xlabel('Sepal Length (cm)')
# Set the label for the y-axis
plt.ylabel('Petal Length (cm)')
# Display the scatter plot.
plt.show()


# Findings/Observations:
# - The Iris dataset contains measurements for 150 Iris flowers, with 50 flowers from each of three species (setosa, versicolor, virginica).
# - The measurements are sepal length, sepal width, petal length, and petal width, all in centimeters.
# - There are no missing values in this dataset, which is good.
# - Basic statistics (.describe()) show the range, average, and spread of each measurement.
# - Grouping by species and calculating means (.groupby()) revealed that different Iris species have different average measurements.
# - In particular, Virginica species tends to have larger sepal and petal lengths and widths on average compared to Versicolor and Setosa.
# - Setosa species tends to have smaller sepal and petal lengths and widths compared to the other two.
# - The bar chart visualization clearly shows the differences in average petal length across species.
# - The histogram of petal width shows that petal widths are not uniformly distributed, possibly suggesting different groups or clusters within the data.
# - The scatter plot of sepal length vs. petal length suggests a positive correlation - as sepal length increases, petal length tends to increase as well. There also seem to be clusters of points, possibly corresponding to different species.
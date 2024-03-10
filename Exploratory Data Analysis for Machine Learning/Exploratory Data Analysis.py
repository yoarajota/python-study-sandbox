import os
import numpy as np
import pandas as pd
from helpers import Helpers
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns

h = Helpers

# Define the URL from which to download the file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/iris_data.csv"

h.download_file(url, "iris_data.csv")

data = pd.read_csv("data\iris_data.csv")
 
print(data.head())

## Question 1

# Load the data from the file using the techniques learned today. Examine it.

# Determine the following:

# * The number of data points (rows). (*Hint:* check out the dataframe `.shape` attribute.)
# * The column names. (*Hint:* check out the dataframe `.columns` attribute.)
# * The data types for each column. (*Hint:* check out the dataframe `.dtypes` attribute.)

### BEGIN SOLUTION
# Number of rows
print(data.shape[0])

h.n()

# Column names
print(data.columns.tolist())

h.n()

# Data types
print(data.dtypes)
### END SOLUTION

h.n()


## Question 2

# Examine the species names and note that they all begin with 'Iris-'. Remove this portion of the name so the species name is shorter. 

### BEGIN SOLUTION
# The str method maps the following function to each entry as a string
data['species'] = data.species.str.replace('Iris-', '')
# alternatively
# data['species'] = data.species.apply(lambda r: r.replace('Iris-', ''))

print(data.head())

h.n()
### END SOLUTION

## Question 3

# Determine the following:  
# * The number of each species present. (*Hint:* check out the series `.value_counts` method.)
# * The mean, median, and quantiles and ranges (max-min) for each petal and sepal measurement.

# *Hint:* for the last question, the `.describe` method does have median, but it's not called median. It's the *50%* quantile. `.describe` does not have range though, and in order to get the range, you will need to create a new entry in the `.describe` table, which is `max - min`.

### BEGIN SOLUTION

# Number of each species
print(data.species.value_counts())

h.n()

# Select just the rows desired from the 'describe' method and add in the 'median'
stats_df = data.describe()
stats_df.loc['range'] = stats_df.loc['max'] - stats_df.loc['min']

out_fields = ['mean','25%','50%','75%', 'range']
stats_df = stats_df.loc[out_fields]
stats_df.rename({'50%': 'median'}, inplace=True)
print(stats_df)
### END SOLUTION


# Question 4

# Calculate the following for each species in a separate dataframe:

# The mean of each measurement (sepal_length, sepal_width, petal_length, and petal_width).
# The median of each of these measurements.
# Hint: you may want to use Pandas groupby method to group by species before calculating the statistic.

# If you finish both of these, try calculating both statistics (mean and median) in a single table (i.e. with a single groupby call). See the section of the Pandas documentation on applying multiple functions at once for a hint.

### BEGIN SOLUTION
# The mean calculation
print(data.groupby('species').mean())
h.n()

# The median calculation
print(data.groupby('species').median())
h.n()

# applying multiple functions at once - 2 methods
print(data.groupby('species').agg(['mean', 'median']))  # passing a list of recognized strings
h.n()

# If certain fields need to be aggregated differently, we can do:
agg_dict = {field: ['mean', 'median'] for field in data.columns if field != 'species'}
agg_dict['petal_length'] = 'max'
pprint(agg_dict)

print(data.groupby('species').agg(agg_dict))
h.n()
### END SOLUTION


## Question 5

# Make a scatter plot of `sepal_length` vs `sepal_width` using Matplotlib. Label the axes and give the plot a title.

### BEGIN SOLUTION
# A simple scatter plot with Matplotlib
ax = plt.axes()

ax.scatter(data.sepal_length, data.sepal_width)

# Label the axes
ax.set(xlabel='Sepal Length (cm)',
       ylabel='Sepal Width (cm)',
       title='Sepal Length vs Width');

plt.show()
### END SOLUTION

## Question 6

# Make a histogram of any one of the four features. Label axes and title it as appropriate. 

### BEGIN SOLUTION
# Using Matplotlib's plotting functionality
ax = plt.axes()
ax.hist(data.petal_length, bins=25);

ax.set(xlabel='Petal Length (cm)', 
       ylabel='Frequency',
       title='Distribution of Petal Lengths');

plt.show()

# Alternatively using Pandas plotting functionality
ax = data.petal_length.plot.hist(bins=25)

ax.set(xlabel='Petal Length (cm)', 
       ylabel='Frequency',
       title='Distribution of Petal Lengths');

plt.show()

### END SOLUTION



## Question 7

# Now create a single plot with histograms for each feature (`petal_width`, `petal_length`, `sepal_width`, `sepal_length`) overlayed. If you have time, next try to create four individual histogram plots in a single figure, where each plot contains one feature.

# For some hints on how to do this with Pandas plotting methods, check out the [visualization guide](http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html) for Pandas.

sns.set_context('notebook')

### BEGIN SOLUTION

for column in data.columns:
    sns.histplot(data[column], kde=True, label=column)

plt.legend()
plt.show()
### END SOLUTION

## Question 8

# Using Pandas, make a boxplot of each petal and sepal measurement. Here is the documentation for [Pandas boxplot method](http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html#visualization-box).

### BEGIN SOLUTION
# Here we have four separate plots
data.boxplot(by='species');
### END SOLUTION``````````````````````````````````

## Question 9

# Now make a single boxplot where the features are separated in the x-axis and species are colored with different hues. 

# *Hint:* you may want to check the documentation for [Seaborn boxplots](http://seaborn.pydata.org/generated/seaborn.boxplot.html). 

# Also note that Seaborn is very picky about data format--for this plot to work, the input dataframe will need to be manipulated so that each row contains a single data point (a species, a measurement type, and the measurement value). Check out Pandas [stack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.stack.html) method as a starting place.

# Here is an example of a data format that will work:

# |     | species | measurement  | size |
# | -   | ------- | ------------ | ---- |
# | 0	| setosa  | sepal_length | 5.1  |
# | 1	| setosa  | sepal_width  | 3.5  |

### BEGIN SOLUTION
# First we have to reshape the data so there is 
# only a single measurement in each column

plot_data = (data
             .set_index('species')
             .stack()
             .to_frame()
             .reset_index()
             .rename(columns={0:'size', 'level_1':'measurement'})
            )

print(plot_data.head())

# Now plot the dataframe from above using Seaborn

sns.set_style('white')
sns.set_context('notebook')
sns.set_palette('dark')

f = plt.figure(figsize=(6,4))
sns.boxplot(x='measurement', y='size', 
            hue='species', data=plot_data);

plt.show()
### END SOLUTION

## Question 10

# Make a pairplot with Seaborn to examine the correlation between each of the measurements.

### BEGIN SOLUTION
sns.set_context('talk')
sns.pairplot(data, hue='species');
plt.show()
### END SOLUTION
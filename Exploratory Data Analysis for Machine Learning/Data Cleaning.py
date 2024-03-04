import pandas as pd
import numpy as np 

import seaborn as sns 
import matplotlib.pylab as plt

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from scipy.stats import norm
from scipy import stats

from helpers import Helpers as h

# Define the URL from which to download the file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/Ames_Housing_Data1.tsv"

h.download_file(url, "Ames_Housing_Data1.tsv")

housing = pd.read_csv("data/Ames_Housing_Data1.tsv", sep='\t')

print(housing.head(5))

h.space()

print("We can find more information about the features and types using the info() method.")
housing.info()
h.n()
print("According to the output above, we have 2930 entries, 0 to 2929, as well as 81 features. The 'Non-Null Count' column shows the number of non-null entries. If the count is 2930 then there is no missing values for that particular feature. 'SalePrice' is our target or response variable and the rest of the features are our predictor variables. We also have a mix of numerical (28 int64 and 11 float64) and object data types.")
h.n()

print(housing["SalePrice"].describe())
h.n()
print("From the above analysis, it is important to note that the minimum value is greater than 0. Also, there is a big difference between the minimum value and the 25th percentile. It is bigger than the 75th percentile and the maximum value. This means that our data might not be normally distributed (an important assumption for linear regression analysis), so will check for normality in the Log Transform section.")

h.space()

# Exercise 1
print("Counting values of Sale Condition;")
print(housing["Sale Condition"].value_counts())

## **Looking for Correlations**
h.space()

print("We will use the corr() function to list the top features based on the pearson correlation coefficient (measures how closely two sequences of numbers are correlated). Correlation coefficient can only be calculated on the numerical attributes (floats and integers), therefore, only the numeric attributes will be selected.")
h.n()


hous_num = housing.select_dtypes(include = ['float64', 'int64'])

hous_num_corr = hous_num.corr()['SalePrice'][:-1] # -1 means that the latest row is SalePrice
top_features = hous_num_corr[abs(hous_num_corr) > 0.5].sort_values(ascending=False) #displays pearsons correlation coefficient greater than 0.5
print("There is {} strongly correlated values with SalePrice:\n{}".format(len(top_features), top_features))


# pairplot function -> By default, this function will create a grid of Axes such that each numeric variable in data will by shared across the y-axes across a single row and the x-axes across a single column. The diagonal plots are treated differently: a univariate distribution plot is drawn to show the marginal distribution of the data in each column.
# for i in range(0, len(hous_num.columns), 5):
#     sns.pairplot(data=hous_num,
#                 x_vars=hous_num.columns[i:i+5],
#                 y_vars=['SalePrice'])

# plt.show()

## **Log Transformation**

# We will use the visual method, by plotting the 'SalePrice' distribution using the distplot() function from the seaborn library
sp_untransformed = sns.displot(housing['SalePrice'])
plt.show()
h.n()

print("SalePrice Skewness: %f" % housing['SalePrice'].skew())
# In statistics skewness is a measure of asymmetry of the distribution
h.n()

print("Moderate skewness is -0.5 to -1.0 and 0.5 to 1.0; and highly skewed distribution is < -1.0 and > 1.0. In our case, we have ~1.7, so it is considered highly skewed data.")
h.n()

print("Now, we can try to transform our data, so it looks more normally distributed. We can use the np.log() function from the numpy library to perform log transform.")
h.n()

log_transformed = np.log(housing['SalePrice'])
sp_transformed = sns.displot(log_transformed)
print("Transformed SalePrice Skewness: %f" % (log_transformed).skew())
plt.show()
h.n()
print("As we can see, the log method transformed the 'SalePrice' distribution into a more symmetrical bell curve and the skewness level now is -0.01, well within the range.")

# Exercise 2
# Visually inspect the 'Lot Area' feature. If there is any skewness present, apply log transform to make it more normally distributed.

sp_untransformed = sns.displot(housing['Lot Area'])
plt.show()
h.n()


lot_area_skewness = housing['Lot Area'].skew()
print("Lot Area Skewness: %f" % lot_area_skewness)

# Moderate skewness is -0.5 to -1.0 and 0.5 to 1.0; and highly skewed distribution is < -1.0 and > 1.0.
if (lot_area_skewness > 1.0) or (lot_area_skewness < -1.0):
    print("The 'Lot Area' feature is highly skewed. We will apply log transform to make it more normally distributed.")
    h.n()
    lot_area_transformed = np.log(housing['Lot Area'])
    sp_transformed = sns.displot(lot_area_transformed)
    print("Transformed Lot Area Skewness: %f" % (lot_area_transformed).skew())
    plt.show()


## **Handling the Duplicates**

duplicate = housing[housing.duplicated(['PID'])]
print("Duplicated:")
print(duplicate)

# As we can see, there is one duplicate row in this dataset. To remove it, we can use pandas `drop_duplicates()` function. By default, it removes all duplicate rows based on all the columns.

dup_removed = housing.drop_duplicates()
print("Dup Removed:")
print(dup_removed)

print("Has duplicated?")
print(housing.index.is_unique)

## Exercise 3
# In this exercise try to remove duplicates on a specific column by setting the subset equal to the column that contains the duplicate, such as 'Order'.

dup_removed = housing.drop_duplicates(subset=['Order'])
print("Order Dup Removed")
print(dup_removed)

## **Handling the Missing Values**

### Finding the Missing Values

# For easier detection of missing values, pandas provides the isna(), isnull(), and notna() functions.

total = housing.isnull().sum().sort_values(ascending=False)
total_select = total.head(20)
total_select.plot(kind="bar", figsize = (8,6), fontsize = 10)

plt.xlabel("Columns", fontsize = 20)
plt.ylabel("Count", fontsize = 20)
plt.title("Total Missing Values", fontsize = 20)
plt.show()


housing.dropna(subset=["Lot Frontage"])
# Using this method, all the rows, containing null values in 'Lot Frontage' feature, for example, will be dropped.

housing.drop("Lot Frontage", axis=1)
# Using this method, the entire column containing the null values will be dropped.

median = housing["Lot Frontage"].median()
print(median)

h.space()

housing["Lot Frontage"] = housing["Lot Frontage"].fillna(median)
print(housing.tail())

h.n()

print("Index# 2927, containing a missing value in the 'Lot Frontage', now has been replaced with the median value.")

h.n()

## Exercise 4
# In this exercise, let's look at 'Mas Vnr Area' feature and replace the missing values with the mean value of that column.

median = housing["Mas Vnr Area"].median()
housing["Mas Vnr Area"] = housing["Mas Vnr Area"].fillna(median)

## **Feature Scaling**

# Min-max scaling (or normalization) is the simplest: values are shifted and rescaled so they end up ranging from 0 to 1. This is done by subtracting the min value and dividing by the max minus min.
# Standardization is different: first it subtracts the mean value (so standardized values always have a zero mean), and then it divides by the standard deviation, so that the resulting distribution has unit variance. 

# Scikit-learn library provides MinMaxScaler for normalization and StandardScaler for standardization needs. 

norm_data = MinMaxScaler().fit_transform(hous_num)
print(norm_data)

h.space()

scaled_data = StandardScaler().fit_transform(hous_num)
print(scaled_data)

h.space()

## Exercise 5
# In this exercise, use StandardScaler() and fit_transform() functions to standardize the 'SalePrice' feature only.

norm_data = MinMaxScaler().fit_transform(housing[['SalePrice']])
print(norm_data)

h.space()

# Standardize 'SalePrice' with StandardScaler
scaled_data = StandardScaler().fit_transform(housing[['SalePrice']])
print(scaled_data)

h.space()

## **Handling the Outliers**
### Finding the Outliers
# An outlier is an observation point that is distant from other observations

### Uni-variate Analysis

sns.boxplot(x=housing['Lot Area'])
plt.show()

sns.boxplot(x=housing['SalePrice'])

plt.show()

### Bi-variate Analysis
# As we can see from these two plots, we have some points that are plotted outside the box plot area and that greatly deviate from the rest of the population. Whether to remove or keep them will greatly depend on the understanding of our data and the type of analysis to be performed. 

price_area = housing.plot.scatter(x='Gr Liv Area', y='SalePrice')

plt.show()

# From the above graph, there are two values above 5000 sq. ft. living area that deviate from the rest of the population and do not seem to follow the trend. It can be speculated why this is happening but for the purpose of this lab we can delete them.

### Deleting the Outliers

housing.sort_values(by = 'Gr Liv Area', ascending = False)[:2]

outliers_dropped = housing.drop(housing.index[[1499,2181]])

new_plot = outliers_dropped.plot.scatter(x='Gr Liv Area', y='SalePrice')

plt.show()

## Exercise 6
# Determine whether there are any outliers in the 'Lot Area' feature. 
# You can either plot the box plot for the 'Lot Area', perform a bi-variate analysis by making a scatter plot between the 'SalePrice' and the 'Lot Area', or use the Z-score analysis. If there re any outliers, remove them from the dataset.

sns.boxplot(x=housing['Lot Area'])
plt.show()

price_lot = housing.plot.scatter(x='Lot Area', y='SalePrice')   
plt.show()

housing['Lot_Area_Stats'] = stats.zscore(housing['Lot Area'])
housing[['Lot Area','Lot_Area_Stats']].describe().round(3)
housing.sort_values(by = 'Lot Area', ascending = False)[:1]
lot_area_rem = housing.drop(housing.index[[957]])

price_lot = housing.plot.scatter(x='Lot Area', y='SalePrice')
plt.show()

## Z-score Analysis

# Below, we are using Z-score function from scipy library to detect the outliers in our 'Low Qual Fin SF' parameter. 

housing['LQFSF_Stats'] = stats.zscore(housing['Low Qual Fin SF'])
h.space()
print(housing[['Low Qual Fin SF','LQFSF_Stats']].describe().round(3))

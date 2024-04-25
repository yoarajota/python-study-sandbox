import pandas as pd
import seaborn as sns
import skillsnetwork
from helpers import Helpers
import matplotlib.pylab as plt
import numpy as np

sns.set()


h = Helpers

# Define the URL from which to download the file
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/Ames_Housing_Data.tsv'

h.download_file(url, "Ames_Housing_Data.tsv")

df = pd.read_csv('data/Ames_Housing_Data.tsv', sep='\t')

df.info()

h.space()

df = df.loc[df['Gr Liv Area'] <= 4000,:]
print("Number of rows in the data:", df.shape[0])
print("Number of columns in the data:", df.shape[1])
data = df.copy() # Keep a copy our original data 

h.space()

print(df.head())

h.space()

# Start some cleaning

# Get a Pd.Series consisting of all the string categoricals
one_hot_encode_cols = df.dtypes[df.dtypes == object]  # filtering by string categoricals
one_hot_encode_cols = one_hot_encode_cols.index.tolist()  # list of categorical fields

df[one_hot_encode_cols].head().T

# Converting categorical variables to dummies
# Making skew variables symmetric

#### One-hot encoding the dummy variables:
# Do the one hot encoding
df = pd.get_dummies(df, columns=one_hot_encode_cols, drop_first=True)
df.describe().T

### Log transforming skew variables
# Create a list of float colums to check for skewing
mask = data.dtypes == float
float_cols = data.columns[mask]

skew_limit = 0.75 # define a limit above which we will log transform
skew_vals = data[float_cols].skew()

# Showing the skewed columns
skew_cols = (skew_vals
    .sort_values(ascending=False)
    .to_frame()
    .rename(columns={0:'Skew'})
    .query('abs(Skew) > {}'.format(skew_limit)))

h.space()

print(skew_cols)

# Let's look at what happens to one of these features, when we apply np.log1p visually.

# Choose a field
field = "BsmtFin SF 1"

# Create two "subplots" and a "figure" using matplotlib
fig, (ax_before, ax_after) = plt.subplots(1, 2, figsize=(10, 5))

# Create a histogram on the "ax_before" subplot
df[field].hist(ax=ax_before)

# Apply a log transformation (numpy syntax) to this column
df[field].apply(np.log1p).hist(ax=ax_after)

# Formatting of titles etc. for each subplot
ax_before.set(title='before np.log1p', ylabel='frequency', xlabel='value')
ax_after.set(title='after np.log1p', ylabel='frequency', xlabel='value')
fig.suptitle('Field "{}"'.format(field));

fig.show()

# Perform the skew transformation:

for col in skew_cols.index.values:
    if col == "SalePrice":
        continue
    df[col] = df[col].apply(np.log1p)

h.space()
# We now have a larger set of potentially-useful features
print(df.shape)

# There are a *lot* of variables. Let's go back to our saved original data and look at how many values are missing for each variable. 
df = data
data.isnull().sum().sort_values()

# Let's pick out just a few numeric columns to illustrate basic feature transformations.

smaller_df= df.loc[:, ['Lot Area', 'Overall Qual', 'Overall Cond', 
'Year Built', 'Year Remod/Add', 'Gr Liv Area', 
'Full Bath', 'Bedroom AbvGr', 'Fireplaces', 
'Garage Cars','SalePrice']]

# Now we can look at summary statistics of the subset data
smaller_df.describe().T

smaller_df.info()

# There appears to be one NA in Garage Cars - we will take a simple approach and fill it with 0
smaller_df = smaller_df.fillna(0)

smaller_df.info()

sns.pairplot(smaller_df, plot_kws=dict(alpha=.1, edgecolor='none'))

plt.show()
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
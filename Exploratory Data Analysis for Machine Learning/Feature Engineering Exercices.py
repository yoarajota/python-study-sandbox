import pandas as pd
import seaborn as sns
import skillsnetwork
from helpers import Helpers
import matplotlib.pylab as plt
import numpy as np

h = Helpers

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/airlines_data.xlsx"

h.download_file(url, "airlines_data.xlsx")
 
data = pd.read_excel("airlines_data.xlsx")

data.isnull().sum()

data = data.fillna(method='ffill')

data['Airline'] = np.where(data['Airline']=='Vistara Premium economy', 'Vistara', data['Airline'])
data['Airline'] = np.where(data['Airline']=='Jet Airways Business', 'Jet Airways', data['Airline'])

### Exercicios

# Exercise 1
# In this exercise, use np.where() function to combine 'Multiple carriers Premium economy' and 'Multiple carriers' categories, like shown in the code above. Print the newly created list using unique().tolist() functions.

data['Airline'] = np.where(data['Airline']=='Multiple carriers Premium economy', 'Multiple carriers', data['Airline'])
data['Airline'].unique().tolist()

## Exercise 2
# In this exercise, use `value_counts()` to determine the values distribution of the 'Total_Stops' parameter.

data['Total_Stops'].value_counts()
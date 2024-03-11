import pandas as pd
import plotly.express as px
import datetime 
import requests
import json
from helpers import Helpers as h

gasoline = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/18100001.csv")

print(gasoline.head())

h.n()

print(gasoline.shape)

h.n()

gasoline.info()

h.n()

print(gasoline.columns)

h.n()

print(gasoline.isnull().sum())

h.n()

## **Data Wrangling** 
### Selecting and renaming the columns of interest

data = (gasoline[['REF_DATE','GEO','Type of fuel','VALUE']]).rename(columns={"REF_DATE" : "DATE", "Type of fuel" : "TYPE"})
print(data.head())

h.n()

### Splitting the columns

data[['City', 'Province']] = data['GEO'].str.split(',', n=1, expand=True)

print(data.head())

h.n()

data['DATE'] = pd.to_datetime(data['DATE'], format='%b-%y')
data['Month'] = data['DATE'].dt.month_name().str.slice(stop=3)
data['Year'] = data['DATE'].dt.year
print(data.head())

h.n()

print(data.VALUE.describe())

h.n()

print(data.GEO.unique().tolist())

h.n()

## Exercise 1
# In this exercise, print out all categories in 'TYPE' column.

print(data.TYPE.unique().tolist())

h.n()

## **Data Filtering** 
calgary = data[data['GEO'] == 'Calgary, Alberta']

print(calgary)

h.n()

sel_years = data[data['Year'] ==  2000]
print(sel_years)

h.n()

## Exercise 2 a

# In this exercise, please use the examples shown above, to select the data that shows the price of the 'household heating fuel', in Vancouver, in 1990.

filt = data[data['TYPE'] == 'Household heating fuel']
filt = filt[filt['City'] == 'Vancouver']
filt = filt[filt['Year'] == 1990]
print(filt)

exercise2a = data[( data['Year'] ==  1990) & (data['TYPE'] == "Household heating fuel") & (data['City']=='Vancouver')]
print(exercise2a)

## Exercise 2 b

# In this exercise, please select the data that shows the price of the 'household heating fuel', in Vancouver, in the years of 1979 and 2021.

exercise2b = data[( data['Year'] <=  1979) | ( data['Year'] ==  2021) & (data['TYPE'] == "Household heating fuel") & (data['City']=='Vancouver')]
print(exercise2b)

h.n()

### Filtering using `groupby()` method

geo = data.groupby('GEO')
print(geo.ngroups)

group_year = data.groupby(['Year'])['VALUE'].mean()
print(group_year)

h.n()

## Exercise 3 a

# In the cell below, please use `groupby()` method to group by the maximum value of gasoline prices, for each month. 

group_month = data.groupby(['Month'])['VALUE'].max()
print(group_month)


## Exercise 3 b

# In the cell below, please use `groupby()` method to group by the median value of gasoline prices, for each year and each city. 

exercise3b = data.groupby(['Year', 'City'])['VALUE'].median()
print(exercise3b)


## **Visualizing the data with *pandas* plotly.express** 

# Here, we will plot the prices of gasoline in all cities during 1979 - 2021.
price_bycity = data.groupby(['Year', 'GEO'])['VALUE'].mean().reset_index(name ='Value').round(2)

# create figure
fig = px.line(price_bycity
                   ,x='Year', y = "Value", 
                   color = "GEO", color_discrete_sequence=px.colors.qualitative.Light24)
fig.update_traces(mode='markers+lines')
fig.update_layout(
    title="Gasoline Price Trend per City",
    xaxis_title="Year",
    yaxis_title="Annual Average Price, Cents per Litre")
fig.show()

mon_trend = data[(data['Year'] ==  2021) & (data['GEO'] == "Toronto, Ontario")]
group_month = mon_trend.groupby(['Month'])['VALUE'].mean().reset_index().sort_values(by="VALUE")
fig = px.line(group_month, x='Month', y = "VALUE")
fig.update_traces(mode='markers+lines')
fig.update_layout(
    title="Toronto Average Monthly Gasoline Price in 2021",
    xaxis_title="Month",
    yaxis_title="Monthly Price, Cents per Litre")
fig.show()

## Exercise 4

# In the cell below, use *plotly.express* or other libraries, to plot the annual average gasoline price, per year, per gasoline type.
type_gas = data.groupby(['Year', 'TYPE'])['VALUE'].mean().reset_index(name ='Type').round(2)
fig = px.line(type_gas, x='Year', y = "Type", color = "TYPE", color_discrete_sequence = px.colors.qualitative.Light24)
fig.update_traces(mode='markers+lines')
fig.update_layout(
    title="Fuel Type Price Trend",
    xaxis_title="Year",
    yaxis_title="Annual Average Price, Cents per Litre")
fig.show()

bycity = data.groupby(['Year', 'City'])['VALUE'].mean().reset_index(name ='Value').round(2)
bycity.head()

fig = px.bar(bycity, x='City', y = "Value", animation_frame="Year")

fig.update_layout(
    title="Time Lapse of Average Price of Gasoline, by Province",
    xaxis_title="Year",
    yaxis_title="Average Price of Gasoline, Cents per Litre")

fig.show()

one_year = data[data['Year'] == 2021]
print(one_year.head())

geo = requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/canada_provinces.geojson")

mp = json.loads(geo.text)
    
fig = px.choropleth(geodata,
                    locations="ProvinceID",
                    geojson=mp,
                    featureidkey="properties.cartodb_id",
                    color="Average Gasoline Price",
                    color_continuous_scale=px.colors.diverging.Tropic,
                    scope='north america',
                    title='<b>Average Gasoline Price </b>',                
                    hover_name='Province',
                    hover_data={
                        'Average Gasoline Price' : True,
                        'ProvinceID' : False
                    },
                     
                    locationmode='geojson-id',
                    )
fig.update_layout(
    showlegend=True,
    legend_title_text='<b>Average Gasoline Price</b>',
    font={"size": 16, "color": "#808080", "family" : "calibri"},
    margin={"r":0,"t":40,"l":0,"b":0},
    legend=dict(orientation='v'),
    geo=dict(bgcolor='rgba(0,0,0,0)', lakecolor='#e0fffe')
)

#Show Canada only 
fig.update_geos(showcountries=False, showcoastlines=False,
                showland=False, fitbounds="locations",
                subunitcolor='white')
fig.show()
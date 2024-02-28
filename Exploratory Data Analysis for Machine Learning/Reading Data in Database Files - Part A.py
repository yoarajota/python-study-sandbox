# Imports
import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd
import requests
import os

# Define the URL from which to download the file
# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/classic_rock.db"

# # Define the directory where you want to save the file
# directory = "data/"

# # Create the directory if it does not exist
# os.makedirs(directory, exist_ok=True)

# # Send an HTTP GET request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Open the file in binary write mode and write the contents of the response
#     with open(os.path.join(directory, "classic_rock.db"), "wb") as f:
#         f.write(response.content)
#     print("File downloaded successfully.")
# else:
#     print(f"Failed to download the file. Status code: {response.status_code}")

# We now have a live connection to our SQL database

# Initialize path to SQLite databasejdbc:sqlite:/C:/__tmp/test/sqlite/jdbcTest.db
path = 'data/classic_rock.db'
con = sq3.Connection(path)

# Write the query
query = '''
SELECT * 
FROM rock_songs;
'''

# Execute the query
observations = pds.read_sql(query, con)

observations.head()

print(observations)
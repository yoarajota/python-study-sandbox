import pandas as pd
import seaborn as sns
import skillsnetwork
from helpers import Helpers

sns.set()


h = Helpers

# Define the URL from which to download the file
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/Ames_Housing_Data.tsv'

h.download_file(url, "Ames_Housing_Data.tsv")

df = pd.read_csv('data/Ames_Housing_Data.tsv', sep='\t')

df.info()
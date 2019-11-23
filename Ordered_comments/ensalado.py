import os
import numpy as np
import pandas as pd
from google.cloud import bigquery


print(' you need GOOGLE_APPLICATION_CREDENTIALS do download the dataset')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="GAC.json"

sql = """
select time_ts,`by`,id ,`text` from `saltyhacker.hacker.comments` where time_ts > '2013-10-13' 
"""
# Run a Standard SQL query using the environment's default project
df = pd.read_gbq(sql, dialect='standard')

# Run a Standard SQL query with the project set explicitly
project_id = 'saltyhacker'
df = pd.read_gbq(sql, project_id=project_id, dialect='standard')

df.to_csv('./comments.csv')


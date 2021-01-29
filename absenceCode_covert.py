#install (if you dont have it) and import pandas
import pandas as pd

#read the csv file
df = pd.read_csv('Absence_Request.csv')

#Define the mapping values for all time types. Only examples below
work_type = {
    "DEU":"DE_001",
    "ESP":"ES_001",
    "CHE":"CH_001",
    "SWE":"SE_001"
    }

sick_type = {
    "DEU":"DE_002",
    "ESP":"ES_003",
    "CHE":"CH_002",
    "SWE":"SE_002"
}

#Replace the values in the time type column for the mapped values based on the country
df.loc[df['timeType.externalCode'] == "WORK", 'timeType.externalCode'] = df['Country'].map(work_type)
df.loc[df['timeType.externalCode'] == "SICK", 'timeType.externalCode'] = df['Country'].map(sick_type)

#Remove the Country column
df = df.drop(columns = ['Country'])

#Write a new CSV file
df.to_csv('Absence_Rquest_updated.csv', index=False)

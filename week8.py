import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#load dataset
df = pd.read_csv('metadata.csv')
#understand dataset
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
#check for missing values
print(df.isnull().sum())
import missingno as msno # type: ignore
msno.bar(df)
plt.show()
#Data transformation
df['pub_year'] = df['pub_year'].astype(int)
df['title_length'] = df['title'].apply(len)
#Exploratory Data Analysis
plt.figure(figsize=(10,6))
sns.histplot(df['pub_year'], bins=30, kde=True)
plt.title('Publication Year Distribution')
plt.xlabel('Publication Year')
plt.ylabel('Frequency')
plt.show()





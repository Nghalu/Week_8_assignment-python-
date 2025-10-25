import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv('metadata.csv',low_memory=False)
# Display the first few rows of the dataset
print(df.head())
print(df.shape)
print(df.info())
# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)
# Summary statistics of numerical columns
print(df.describe())
# Summary statistics of categorical columns
print(df.describe(include=['object']))
# Visualize the distribution of a numerical column
plt.figure(figsize=(10, 6)) 
plt.hist(df['who_covidence_id'].dropna(), bins=30, color='blue', alpha=0.7)
plt.title('who_covidence Distribution')
plt.xlabel('who_covidence_id')
plt.ylabel('Frequency')
plt.show()

df['year'] = pd.to_datetime(df['publish_time']).dt.year
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.show()




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from IPython import get_ipython
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm

warnings.filterwarnings("ignore")

# Read in the sleep data and print some summary statistics
df = pd.read_csv('sleep_data.csv')
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.duplicated().sum())
print(df.isnull().sum())
print(df.info())
print(df.describe())
print(df.nunique())

# Convert the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'])

# Create some sleep plots
plt.figure(figsize=(15,6))
sns.lineplot(x=df['date'], y=df['sleep_hours'], data=df, palette='muted')
plt.show()

plt.figure(figsize=(15,6))
sns.scatterplot(x=df['date'], y=df['sleep_hours'], data=df, palette='muted')
plt.show()

plt.figure(figsize=(15,6))
sns.histplot(df['sleep_hours'], bins=20, kde=True, palette='muted')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(15,6))
sns.distplot(df['sleep_hours'], bins=20, kde=True)
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(15,6))
sns.boxplot(df['sleep_hours'], palette='muted')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(15,6))
sns.violinplot(df['sleep_hours'], palette='muted')
plt.xticks(rotation=90)
plt.show()

# Set the 'date' column as the index and read in the new sleep data
df = df.set_index('date')
df1 = pd.read_csv('sleep_data_new.csv')

# Print some summary statistics about the new sleep data
print(df1.head())
print(df1.tail())
print(df1.shape)
print(df1.columns)
print(df1.duplicated().sum())
df1 = df1.drop_duplicates()
print(df1.isnull().sum())
print(df1.info())
print(df1.nunique())

# Create some plots of the new sleep data
print(df1['sourceName'].unique())
print(df1['sourceName'].value_counts())

plt.figure(figsize=(15,6))
sns.countplot(x='sourceName', data=df1, palette='muted')
plt.show()

plt.figure(figsize=(30,20))
plt.pie(df1['sourceName'].value_counts(), labels=df1['sourceName'].value_counts().index,
        autopct='%1.1f%%', textprops={'fontsize': 25, 'color': 'black', 'weight': 'bold', 'family': 'serif'})
hfont = {'fontname': 'serif', 'weight': 'bold'}
plt.title('Source Name', size=20, **hfont)
plt.show()

print(df1['value'].unique())
print(df1['value'].value_counts())

plt.figure(figsize=(15,6))
sns.countplot(x='value', data=df1, palette='muted')
plt.show()

plt.figure(figsize=(30,20))
plt.pie(df1['value'].value_counts(), labels=df1['value'].value_counts().index,
        autopct='%1.1f%%', textprops={'fontsize': 25, 'color': 'black', 'weight': 'bold', 'family': 'serif'})
hfont = {'fontname': 'serif'}
plt.title('Value', size=20)

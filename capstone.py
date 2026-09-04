import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print(sns.get_dataset_names())
df = sns.load_dataset('penguins')

print(df.head(10))

print(df.shape) 

print(df.tail())

print(df.isnull().sum())

print(df.describe())

print(df.info())

print(df.describe(include='all'))

print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')

plt.show()


df.select_dtypes(include=[np.number]).hist(figsize=(12, 8), sharex=False, sharey=False, layout=(3, 2))

plt.show()


print(df.sex.value_counts())
print(df.species.value_counts())
print(df.island.value_counts())

sns.countplot(x='sex', data=df)
plt.show()

sns.countplot(x='island', data=df)
plt.show()

sns.countplot(x='species', data=df)
plt.show()

sns.countplot(data=df, x='sex', hue='species')
plt.show()

sns.countplot(data=df, x='island', hue='species')
plt.show()

sns.countplot(data=df, x='island', hue='sex')
plt.show()

sns.pairplot(data=df, hue='species')
plt.show()
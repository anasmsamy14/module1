import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('penguins')
df = df.dropna()

print('First 5 rows')
print(df.head())
print()
print('df.info()')
print()
print ('df.describe()')
print()
print('species:', df['species'].unique())
print('island:', df['island'].unique())


sns.histplot(data=df, x='body_mass_g', bins=20, color='blue')
plt.title('Distribution of Body Mass')
plt.xlabel('Body Mass (g)')
plt.ylabel('Frequency')
plt.show()


sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
plt.title('KDE Plot of Flipper Length by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Density')
plt.show()

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Scatter Plot of Flipper Length vs Body Mass')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

corr = df.corr(numeric_only=True)
print('Correlation Matrix:')
print(corr)
print()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
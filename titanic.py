import seaborn as sns
import matplotlib.pyplot as plt

#titanic dataset
df = sns.load_dataset('titanic')
df.info()

print('First 5 rows:')
print(df.head())
print()
print('df.info():')
print()
print('df.describe():')
print()
print('survived:', df['survived'].unique())
print('pclass:', df['pclass'].unique())

sns.histplot(data=df, x='age', bins=20, color='green')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


sns.kdeplot(data=df, x='fare', hue='pclass', fill=True)
plt.title('kde plot of fare')
plt.xlabel('Fare')
plt.ylabel('Density')
plt.show()


sns.scatterplot(data=df, x='age', y='fare', hue='pclass')
plt.title('Scatter Plot of Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

sns.barplot(data=df, x='pclass', y='fare', hue='pclass')
plt.title('Bar Plot of Fare by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.show()


sns.boxplot(data=df, x='pclass', y='age', hue='pclass')
plt.title('Box Plot of Age by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Age')
plt.show()

sns.violinplot(data=df, x='pclass', y='fare', hue='pclass')
plt.title('Violin Plot of Fare by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.show()

sns.lmplot(data=df, x='age', y='fare', hue='pclass', aspect=1.5)
plt.title('Linear Regression of Age vs Fare by Pclass')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

sns.pairplot(data=df, hue='pclass', diag_kind='kde')
plt.suptitle('Pair Plot of Titanic Dataset', y=1.02)
plt.show()

sns.jointplot(data=df, x='age', y='fare', hue='pclass', kind='scatter')
plt.suptitle('Joint Plot of Age vs Fare by Pclass', y=1.02)
plt.show()

sns.stripplot(data=df, x='pclass', y='fare', hue='pclass', jitter=True)
plt.title('Strip Plot of Fare by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.show()


sns.swarmplot(data=df, x='pclass', y='fare', hue='pclass')
plt.title('Swarm Plot of Fare by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.show()

sns.catplot(data=df, x='pclass', y='fare', hue='pclass', kind='box')
plt.title('Cat Plot of Fare by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.show()


sns.qplot(data=df, x='age', y='fare', hue='pclass')
plt.title('Quantile Plot of Age vs Fare by Pclass')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

sns.jointplot(data=df, x='age', y='fare', hue='pclass', kind='hex')
plt.suptitle('Hexbin Plot of Age vs Fare by Pclass', y=1.02)
plt.show()


sns.lmplot(data=df, x='age', y='fare', hue='pclass', aspect=1.5)
plt.title('Linear Regression of Age vs Fare by Pclass')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

corr = df.corr(numeric_only=True)
print('Correlation Matrix:')
print(corr)

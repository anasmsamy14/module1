import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()
print(df.head())
print(df.info())


sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Total Bill by Day and Gender')
plt.xlabel('Day of the Week')
plt.ylabel('count of Total Bill')
plt.show()


sns.countplot(x='day', hue='sex', data=df)
plt.title('Count of Total Bill by Day and Gender')
plt.xlabel('Day of the Week')
plt.ylabel('Count of Total Bill')
plt.show()


sns.boxplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Boxplot of Total Bill by Day and Gender')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()

sns.stripplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Stripplot of Total Bill by Day and Gender')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()

sns.violinplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Violin Plot of Total Bill by Day and Gender')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()


sns.swarmplot(x = 'day' , y='total_bill', hue='sex', data=df)
plt.title('Swarm plot of total bill by day and gender')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()


sns.jointplot(x='total_bill',y= 'tip',data=df)
plt.title('Joint Plot of Total Bill and Tip')
plt.ylabel('Tip Amount')
plt.xlabel('Total Bill Amount')
plt.show()  



sns.pairplot(df[[ 'total_bill', 'tip' ]], hue='sex')
plt.title('Pair Plot of Total Bill, Tip, and Other Variables by Gender')
plt.subtitle('Pair Plot of Total Bill, Tip, and Other Variables by Gender')
plt.show()


sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Point Plot of Total Bill by Day and Gender   ')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()

sns.lmplot(x='total_bill', y='tip', hue='sex', data=df)
plt.title('Linear Regression of Total Bill and Tip by Gender')  
plt.xlabel('Total Bill Amount')
plt.ylabel('Tip Amount')
plt.show()

sns.kdeplot(data=df, x='total_bill', hue='sex', fill=True)
plt.title('KDE Plot of Total Bill by Gender')
plt.xlabel('Total Bill Amount')
plt.ylabel('Density')
plt.show()


sns.oddsplot(x='total_bill', y='tip', data=df, hue='sex')
plt.title('Odds Plot of Total Bill and Tip by Gender')
plt.xlabel('Total Bill Amount')
plt.ylabel('Tip Amount')
plt.show
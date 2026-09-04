import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())

plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Customer Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x="day")
plt.title("Number of Customers by Day")
plt.xlabel("Day")
plt.ylabel("Number of Customers")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Distribution of Bills by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

plt.figure(figsize=(8, 5))
sns.stripplot(data=tips, x="day", y="total_bill")
plt.title("Individual Customer Bills by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

plt.figure(figsize=(8, 5))
sns.swarmplot(data=tips, x="day", y="total_bill")
plt.title("Customer Bill Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter")
plt.show()

sns.pairplot(tips, hue="sex")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="sex", y="total_bill")
plt.title("Customer Bills by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Bill")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="sex", y="tip")
plt.title("Average Tip by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Tip")
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x="size")
plt.title("Number of Customers by Party Size")
plt.xlabel("Party Size")
plt.ylabel("Number of Customers")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=tips, x="size", y="total_bill", hue="day")
plt.title("Total Bill vs Party Size")
plt.xlabel("Party Size")
plt.ylabel("Total Bill")
plt.show()

plt.figure(figsize=(8, 5))
sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("Relationship Between Total Bill and Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()
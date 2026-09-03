import seaborn as sns
import matplotlib.pyplot as plt

# Load the planets dataset
planets = sns.load_dataset("planets")

# Inspect the data
print(planets.head())
print(planets.info())
print(planets.describe())

# 1. Histogram of planet orbital periods
sns.histplot(data=planets, x="orbital_period", bins=30)
plt.title("Distribution of Planet Orbital Periods")
plt.xlabel("Orbital Period (days)")
plt.ylabel("Number of Planets")
plt.show()

# 2. KDE plot of planet distance
sns.kdeplot(data=planets, x="distance", fill=True)
plt.title("Distribution of Planet Distance")
plt.xlabel("Distance")
plt.ylabel("Density")
plt.show()

# 3. Histogram with KDE curve
sns.histplot(data=planets, x="distance", bins=30, kde=True)
plt.title("Planet Distance Distribution")
plt.xlabel("Distance")
plt.ylabel("Number of Planets")
plt.show()

# 4. Scatter plot: distance vs orbital period
sns.scatterplot(
    data=planets,
    x="distance",
    y="orbital_period",
    hue="method"
)

plt.title("Planet Distance vs Orbital Period by Discovery Method")
plt.xlabel("Distance")
plt.ylabel("Orbital Period (days)")
plt.legend(title="Discovery Method")
plt.show()
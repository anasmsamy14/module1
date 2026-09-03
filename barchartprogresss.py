import matplotlib.pyplot as plt

# Savings data
weeks = [1, 2, 3, 4, 5, 6, 7, 8]
savings = [10, 20, 35, 50, 65, 80, 100, 125]

# Line graph
plt.plot(
    weeks,
    savings,
    color="blue",
    marker="o",
    linestyle="-",
    linewidth=2
)

# Title and labels
plt.title("My Savings Progress")
plt.xlabel("Week")
plt.ylabel("Savings ($)")

# Show line graph
plt.show()

# Bar chart
plt.bar(weeks, savings)

# Title and labels
plt.title("My Savings Progress - Bar Chart")
plt.xlabel("Week")
plt.ylabel("Savings ($)")

# Show bar chart
plt.show()
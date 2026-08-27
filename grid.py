import matplotlib.pyplot as plt


days  =  ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores  =  [10, 50, 30, 60, 100]

plt.plot(days, scores)
plt.show()

plt.plot(days, scores)
plt.title('My quiz score Tracker')
plt.xlabel('Days of the week')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.show()

plt.plot(days, scores, color='green', marker='o', linestyle='dashed', linewidth=2)
plt.title('My quiz score Tracker')
plt.xlabel('Days of the week')
plt.ylabel('Scores')
plt.grid(True)
plt.ylim(0, 100)
plt.show()

plt.bar(days, scores, color='blue')
plt.title('My quiz score bar chart')
plt.xlabel('Days of the week')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.show()
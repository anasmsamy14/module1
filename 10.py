import matplotlib.pyplot as plt
students = ['Ana', 'Ali', 'Ahmed', 'Anas', 'Khalid', 'Sami', 'Huda', 'Rami', 'Lina', 'Omar']
scores = [85, 92, 78, 96, 88, 91, 84, 89, 93, 87]


plt.bar(students, scores, color='red')
plt.title('Students Scores')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.show()


plt.plot(students, scores, color='navy', marker='o', linestyle='dashed', linewidth=2)
plt.title('Students Scores Line Chart')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.grid(True)
plt.show()

plt.plot(students, scores, color='purple', marker='o', linestyle='dashed', linewidth=2)
plt.title('Students Scores Line Chart')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.grid(True)
plt.show()


plt.plot(students, scores, color='green', marker='o', linestyle='dashed', linewidth=2)
plt.title('Students Scores Line Chart')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.grid(True)
plt.show()

plt.bar(students, scores, color='yellow')
plt.title('Students Scores')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.show()


plt.bar(students, scores, color='blue')
plt.title('Students Scores')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.show()


plt.bar(students, scores, color='orange')
plt.title('Students Scores')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.ylim(0, 100)
plt.show()

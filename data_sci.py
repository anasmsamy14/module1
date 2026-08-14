import numpy as np
data_type = [('name','S15'),('class',int),('height',float)]
student_details = [('Ali', 10, 3.5),('Ahmed', 9, 5.0),('Anas', 10, 5.2),('Hassan', 9, 5.0),('Hussain', 10, 5.1)]
student = np.array(student_details, dtype=data_type)
print('original array:')
print(student)
print('sort by height:')
print(np.sort(student, order='height'))
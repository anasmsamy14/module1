import pandas as pd

# 1. Import Pandas
print("Pandas imported successfully!")

# 2. Create a labelled Series
marks = pd.Series(
    [85, 92, 78, 95, 88],
    index=["Ali", "Sara", "Omar", "Maya", "Adam"],
    name="Marks"
)

print("\nStudent Marks Series:")
print(marks)

# 3. Create a DataFrame
data = {
    "Name": ["Ali", "Sara", "Omar", "Maya", "Adam"],
    "Math": [85, 92, 78, 95, 88],
    "English": [90, 87, 82, 96, 91],
    "Science": [88, 94, 80, 92, 89]
}

df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)

# 4. Save the DataFrame to a CSV file
df.to_csv("student_marks.csv", index=False)

print("\nCSV file saved!")

# 5. Read the CSV file
student_data = pd.read_csv("student_marks.csv")

print("\nData read from CSV:")
print(student_data)

# 6. View the first rows
print("\nFirst 5 rows:")
print(student_data.head())

# 7. Inspect the data information
print("\nData information:")
print(student_data.info())

# 8. Check for missing values
print("\nMissing values:")
print(student_data.isnull().sum())

# 9. Clean missing values
student_data = student_data.fillna(0)

print("\nData after cleaning:")
print(student_data)

# 10. Calculate total marks
student_data["Total"] = (
    student_data["Math"]
    + student_data["English"]
    + student_data["Science"]
)

# 11. Calculate average marks
student_data["Average"] = student_data["Total"] / 3

print("\nFinal Student Marks:")
print(student_data)

# 12. Display overall average
overall_average = student_data["Average"].mean()

print("\nOverall Average:", overall_average)

# 13. Display highest total
highest_mark = student_data["Total"].max()

print("Highest Total:", highest_mark)
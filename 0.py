import pandas as pd 
print ("----Part 1 : Panda Series----")
scores = [50,90,80,100,55,99]
players = pd.Series(scores, index = [
'Ana', 'Ali', 'Ahmed', 'Anas', 'Khalid', 'Sami'])
print(players)

print()
print ("----Part 2 : Panda DataFrame----")
data = {
    'Players': ['Ana', 'Ali', 'Ahmed', 'Anas', 'Khalid', 'Sami'],
    'level': ['Beginner', 'Intermediate', 'Advanced', 'Super HARD  ', 'Intermediate', 'Advanced'],
    'Scores': [50, 90, 80, 100, 55, 99],
    'wins': [2, 5, 8, 1000, 4, 7]
}
df = pd.DataFrame(data)
print(df)
print()
print ("----Part 3 : Accessing Rows-----")
print('Row 0 (top player):')
print(df.loc[0])
print()
print('Row 1 and 2 and 3:')
print(df.loc[[1, 2, 3]])
print ()
print ("----Part 4 : Reading CSV file----")
full_df
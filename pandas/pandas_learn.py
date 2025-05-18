import pandas as pd

# 1. Create a DataFrame from a dictionary
student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 25, 22],
    'Score': [85, 90, 88]
}
df = pd.DataFrame(student_data)
print('DataFrame:')
print(df)

# 2. Select a column
print('\nNames:')
print(df['Name'])

# 3. Select a row by index
print('\nFirst row:')
print(df.iloc[0])

# 4. Basic statistics
print('\nAverage score:', df['Score'].mean())

# 5. Read from a CSV (uncomment if you have a CSV file)
df_csv = pd.read_csv('./pandas/students.csv')
print(df_csv.head())
print(df.shape)        # (rows, columns)
print(df.columns)      # column names
print(df['Name'])      # access a specific column
import matplotlib.pyplot as plt
import pandas as pd

 
df_csv = pd.read_csv('./pandas/students.csv')
print(df_csv.head())
# Plot a bar chart of student scores
plt.figure(figsize=(6,4))
plt.bar(df_csv['Name'], df_csv['Score'], color='skyblue')
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Student Scores')
plt.show()

# Plot a histogram of ages
plt.figure(figsize=(6,4))
plt.hist(df_csv['Age'], bins=5, color='orange', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages')
plt.show()
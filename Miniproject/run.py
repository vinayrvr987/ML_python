import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('./Miniproject/students.csv')
print(df.head())

# Average score of students
df['Average'] = df[['Math', 'Science', 'English', 'History']].mean(axis=1)
print(df[['Name', 'Average']])

# Subject-wise top scorers
for subject in ['Math', 'Science', 'English', 'History']:
    top_scorer = df.loc[df[subject].idxmax()]
    print(f"Top scorer in {subject}: {top_scorer['Name']} with score {top_scorer[subject]}")

# Visualize the scores
plt.figure(figsize=(10, 6))
sns.barplot(x='Name', y='Average', data=df, palette='viridis')
plt.title('Average Scores of Students')
plt.xlabel('Students')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./Miniproject/average_scores.png')
plt.show()

# Heatmap of subject scores
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Math', 'Science', 'English', 'History']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Subject Scores')
plt.savefig('./Miniproject/heatmap.png')
plt.show()
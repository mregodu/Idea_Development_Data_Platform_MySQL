
import pandas as pd

# Load students data
students = pd.read_csv('data/students.csv')
students.drop_duplicates(subset='email', inplace=True)
students.fillna({'department': 'Unknown', 'year': 1}, inplace=True)

# Load innovations data
innovations = pd.read_csv('data/innovations.csv')
innovations['status'] = innovations['status'].str.capitalize()
innovations['category'] = innovations['category'].str.strip()

# Save cleaned data
students.to_csv('data/students_cleaned.csv', index=False)
innovations.to_csv('data/innovations_cleaned.csv', index=False)
print("Data cleaning complete.")

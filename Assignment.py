import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file and convert it into dataframe
csv = pd.read_csv("C:/Users/aksha/Downloads/smartphones_cleaned.csv")
df = pd.DataFrame(csv)
print(f"Original Dataframe:\n",df)

# Check the missing values in Dataframe
mv = df.isnull()
print(f"Displaying the missing values:\n",mv)

# Removing the rows with missing values
mv_drop = df.dropna()
print(f"Dropping the missing values rows:\n",mv_drop)

# Removing the duplicates rows
dup_drop = mv_drop.drop_duplicates()
print(f"Dropping the duplicates rows:\n",dup_drop)

# Saving the updated dataframe as CSV file
dup_drop.to_csv('new_student.csv')
print(f"new data frame:\n",dup_drop)



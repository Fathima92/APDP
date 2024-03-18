import pandas as pd

# Load data from a CSV file
data = pd.read_csv("data.csv")

# Check for missing values
print("Missing values summary:")
print(data.isnull().sum())  # Shows the number of missing values per column

# Handle missing values (example: fill with mean)
data["Age"] = data["Age"].fillna(data["Age"].mean())  # Fill missing values in "Age" column with mean

# Explore data types and descriptive statistics
print("Data types:")
print(data.dtypes)
print("Descriptive statistics:")
print(data.describe())  # Provides summary statistics for numerical columns

# Data cleaning (example: remove outliers)
data = data[data["Salary"] < data["Salary"].quantile(0.95)]  # Remove top 5% outliers in "Salary"

# Feature engineering (example: create a new category for age groups)
data["Age_Group"] = pd.cut(data["Age"], bins=[0, 20, 40, 60, 100], labels=["Young", "Middle-aged", "Senior"])

# Encode categorical variables (example: one-hot encoding)
data = pd.get_dummies(data, columns=["Country"])  # One-hot encode the "Country" column

# Data preparation (select specific columns)
selected_data = data[["Name", "Age_Group", "Salary", "Country_USA"]]

# Save the processed data to a new CSV file
selected_data.to_csv("processed_data.csv", index=False)

# Example usage for further analysis (assuming you have a Machine Learning library like scikit-learn)
from sklearn.model_selection import train_test_split

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(selected_data.drop("Salary", axis=1), selected_data["Salary"], test_size=0.2)

# Train a machine learning model (replace with your desired model)
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train, y_train)

# ... (Your machine learning code here)

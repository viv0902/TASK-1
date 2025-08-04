import pandas as pd

# Load dataset
df = pd.read_excel('consumer.xlsx', sheet_name='consumer')

# Preview initial data
print("Initial data preview:")
print(df.head())

# Rename columns to lowercase and replace spaces with underscores if any
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert date columns to datetime (Dt_Customer), keep only date part (remove time)
df['dt_customer'] = pd.to_datetime(df['dt_customer'], errors='coerce', dayfirst=True).dt.date

# Check for duplicates and remove them
duplicates_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates_count}")
df = df.drop_duplicates()

# Handle missing values:
# For income, let's fill missing values with the median income
median_income = df['income'].median()
df['income'] = df['income'].fillna(median_income)

# For other columns, depending on nature, fill or drop:
# Example: drop rows where 'year_birth' or 'education' missing (adjust as needed)
df = df.dropna(subset=['year_birth', 'education'])

# Convert year_birth to integer type
df['year_birth'] = df['year_birth'].astype(int)

# Check and fix datatype of other columns if needed (e.g., Recency as int)
df['recency'] = pd.to_numeric(df['recency'], errors='coerce').fillna(0).astype(int)

# Standardize categorical columns (education, marital_status) - trim strings and uniform case
df['education'] = df['education'].str.strip().str.title()
df['marital_status'] = df['marital_status'].str.strip().str.title()

# Optional: Remove outliers or invalid values - example check income > 0
df = df[df['income'] > 0]

# Final preview of cleaned data
print("Cleaned data preview:")
print(df.info())
print(df.head())

# Save cleaned data to new file
df.to_csv('consumer_cleaned.csv', index=False)

print("Data cleaning completed. Cleaned data saved to 'consumer_cleaned.csv'")
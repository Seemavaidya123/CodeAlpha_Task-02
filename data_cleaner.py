import pandas as pd

def clean_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Fill missing values with a placeholder (e.g., 'Unknown')
    data.fillna('Unknown', inplace=True)

    # Save the cleaned data to a new file
    cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')
    data.to_csv(cleaned_file_path, index=False)
    print(f'Cleaned data saved to: {cleaned_file_path}')

if __name__ == "__main__":
    # Specify the CSV file to clean
    file_path = input("Enter the path of the CSV file to clean: ")
    clean_data(file_path)

import pandas as pd

def clean_and_transform_data(input_file, output_file):
    """
    Clean and transform the dataset.
    
    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output cleaned CSV file.
    """
    # Load the dataset
    df = pd.read_csv(input_file)

    # Display initial information about the dataset
    print("Initial dataset info:")
    print(df.info())
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    print("Duplicates removed.")

    # Handle missing values
    # Impute missing values in 'Message' column
    df['Message'].fillna('No message', inplace=True)  # Impute with placeholder
    print("Missing values in 'Message' handled.")
    
    # Impute missing values in 'Media Path' column
    df['Media Path'].fillna('No media', inplace=True)  # Impute with placeholder
    print("Missing values in 'Media Path' handled.")
    
    # Validate the data (e.g., check for valid media paths)
    df['Media Path'] = df['Media Path'].apply(lambda x: x if isinstance(x, str) and x.strip() != '' else None)
    df.dropna(subset=['Media Path'], inplace=True)  # Drop rows where Media Path is invalid
    print("Invalid media paths removed.")

    # Standardizing formats (e.g., Date formatting)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert to datetime
    print("Date column standardized.")

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
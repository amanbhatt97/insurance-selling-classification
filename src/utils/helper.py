# dependencies
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()


def load_data(path, file_name):
    """
    Load data from a file. Supports CSV, Pickle, Excel, and JSON formats.
    
    Parameters:
    path (str): The directory path where the file is located.
    file_name (str): The name of the file to read, including its extension.
    
    Returns:
    pd.DataFrame: A pandas DataFrame containing the loaded data.
    """
    # Construct the full file path
    file_path = os.path.join(path, file_name)
    
    # Get the file extension
    file_extension = os.path.splitext(file_name)[1].lower()
    
    # Load the data based on file extension
    if file_extension == '.csv':
        return pd.read_csv(file_path)
    elif file_extension == '.pkl' or file_extension == '.pickle':
        return pd.read_pickle(file_path)
    elif file_extension in ['.xls', '.xlsx']:
        return pd.read_excel(file_path)
    elif file_extension == '.json':
        return pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")


def save_data(df, path, file_name):
        """
        Save a DataFrame to a file. Supports CSV, Pickle, Excel, and JSON formats.

        Parameters:
        df (pd.DataFrame): The DataFrame to save.
        path (str): The directory path where the file should be saved.
        file_name (str): The name of the file to save, including its extension.
        """
        # Construct the full file path
        file_path = os.path.join(path, file_name)
        
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1].lower()
        
        # Save the data based on file extension
        if file_extension == '.csv':
            df.to_csv(file_path, index=False)
        elif file_extension == '.pkl' or file_extension == '.pickle':
            df.to_pickle(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            df.to_excel(file_path, index=False)
        elif file_extension == '.json':
            df.to_json(file_path, orient='records', lines=True)
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")
        
        
def create_path(*paths):
    """
    Create a directory path by joining the given path segments and ensure the directory exists.
    
    Parameters:
    *paths: A variable number of path segments to be joined.
    
    Returns:
    str: The created directory path.
    """
    # Join the given path segments
    full_path = os.path.join(*paths)
    
    # Create the directory if it does not exist
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    
    return full_path
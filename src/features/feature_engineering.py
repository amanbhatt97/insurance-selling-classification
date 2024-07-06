from sklearn.preprocessing import LabelEncoder, StandardScaler
from src.data.preprocess_data import EDA

class EncodingScaling:
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()

    def fit_transform(self, data, target):
        """
        Fit and transform categorical and numerical columns in the data.

        Parameters:
        - data: pandas DataFrame

        Returns:
        - data_processed: pandas DataFrame with encoded categorical and scaled numerical columns
        """
        numerical_columns = EDA().numerical_features(data, target)
        categorical_columns = EDA().categorical_features(data) 
        data_processed = data.copy()
        
        # Encode categorical columns
        for column in categorical_columns:
            label_encoder = LabelEncoder()
            data_processed[column] = label_encoder.fit_transform(data_processed[column])
            self.label_encoders[column] = label_encoder
        
        # Scale numerical columns
        data_processed[numerical_columns] = self.scaler.fit_transform(data_processed[numerical_columns])
        
        return data_processed

    def transform(self, data, target):
        """
        Transform categorical and numerical columns in the data.

        Parameters:
        - data: pandas DataFrame

        Returns:
        - data_transformed: pandas DataFrame with transformed categorical and numerical columns
        """
        numerical_columns = EDA().numerical_features(data, target)
        categorical_columns = EDA().categorical_features(data)
        data_transformed = data.copy()
        
        # Encode categorical columns
        for column in categorical_columns:
            if column in self.label_encoders:
                label_encoder = self.label_encoders[column]
                data_transformed[column] = label_encoder.transform(data_transformed[column])
            else:
                raise ValueError(f"LabelEncoder for {column} not found. Fit the encoder first.")
        
        # Scale numerical columns
        data_transformed[numerical_columns] = self.scaler.transform(data_transformed[numerical_columns])
        
        return data_transformed
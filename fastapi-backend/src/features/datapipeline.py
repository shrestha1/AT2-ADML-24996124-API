import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder

class CategoricalEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, categorical_columns=None):
        self.categorical_columns = categorical_columns
        self.encoder = None
        self.encoded_column_names = None
    
    def fit(self, X, y=None):
        # Ensure categorical_columns is provided
        if self.categorical_columns is None:
            raise ValueError("You must provide 'categorical_columns' for the encoder to work.")
        
        # Initialize the OneHotEncoder
        self.encoder = OneHotEncoder(sparse_output=False)
        
        # Fit the encoder on the specified columns
        self.encoder.fit(X[self.categorical_columns])
        
        # Store the encoded column names
        self.encoded_column_names = self.encoder.get_feature_names_out(self.categorical_columns)
        
        return self
    
    def transform(self, X):
        # Ensure that the encoder was fit before calling transform
        if self.encoder is None:
            raise RuntimeError("You must fit the encoder before transforming the data.")
        
        # Apply the encoder to transform the categorical columns
        X_encoded = self.encoder.transform(X[self.categorical_columns])
        
        # Convert the encoded data to a DataFrame
        df_encoded = pd.DataFrame(X_encoded, columns=self.encoded_column_names, index=X.index).astype(int).astype(bool)
        # Drop the original categorical columns and concatenate the new encoded columns
        
        X_dropped = X.drop(columns=self.categorical_columns)
        X_transformed = pd.concat([X_dropped, df_encoded], axis=1)
        
        return X_transformed

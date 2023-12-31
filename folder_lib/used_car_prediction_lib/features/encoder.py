from abc import ABCMeta, abstractmethod
import pandas as pd

####################father################   
class Encoder(metaclass = ABCMeta):
    
    @abstractmethod
    def encode(self,df, columns_to_encode):
        return NotImplementedError


####################child################   
class BinaryEncoder(Encoder): 

    def __init__(self, true_value, false_value):
        self.true_value = true_value
        self.false_value = false_value
        
    #function for binary variables where we specify the true and false values
    def encode(self, df, column_names):
        for column_name in column_names:
            df[column_name] = df[column_name].replace({self.true_value: 1, self.false_value: 0})
        return df

####################child################   
class OneHotEncoder(Encoder): 
    #function for categorical variables 
    def encode(self,df, columns_to_encode):
        df = pd.get_dummies(df, columns=columns_to_encode, drop_first=True)
        
        # Convert Boolean columns to integers (0s and 1s)
        boolean_columns = df.select_dtypes(include='bool').columns
        df[boolean_columns] = df[boolean_columns].astype(int)
        
        return df


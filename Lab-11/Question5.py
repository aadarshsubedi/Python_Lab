# Create a DataFrame with some missing values (NaN). 
# Fill the missing values with the column mean. 
# Drop rows with missing values. 
import pandas as pd
import numpy as np
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, np.nan, 3, 4, 5]
}
df=pd.DataFrame(data)
print("Dataframe: \n ",df)

df_filled=df.fillna(df.mean()) #This will fill the nan with the mean of the column
print("Dataframe after column filling with mean: \n",df_filled)

df_drop=df.dropna()# It will drop the nan
print("Dataframe after dropping the nan: \n",df_drop)

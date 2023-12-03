
import pandas as pd

def lower_case_no_space_colname (df:pd.DataFrame)->pd.DataFrame:
    '''
    This function takes a Pandas DataFrame as input, and created an interal copy.
    Then on the internal copy, it will convert all column names to lower case and replace white space with '_'.
    
    Input:
    df:Pandas DataFrame
        
    Output:
    Modified Pandas DataFrame
    
    '''
    df2 = df.copy()
    cols = []
    for c in df2.columns:
        cols.append(c.lower().replace(' ', '_'))
    df2.columns = cols
    return df2

def delete_unamed_column(df:pd.DataFrame, unnamed_col = ['Unnamed: 0', 'Unnamed:_0']) -> pd.DataFrame:
    '''
    This function takes a Pandas DataFrame as input, and creates an internal copy.
    Then on the interal copy, it checks whether or not contains a column named "Unnamed: 0" or "Unnamed:_0".
    If it exists, deletes the column and returns the modified DataFrame, otherwise returns
    the original DataFrame.

    Inputs:
    df: Pandas DataFrame

    Output:
    Modified Pandas DataFrame
    '''

    df2 = df.copy()

    if unnamed_col in df2.columns:
        df2 = df2.drop(unnamed_col, axis=1)

    return df2

def clean_gender_column(df:pd.DataFrame) -> pd.DataFrame:
    '''
    This function will take a Pandas DataFrame as an input and it will replace the values in
    the "gender" column ins such a way that any gender which is not Male or Female with be 
    replaced by "U" otherwise the genders will be either "F" or "M"

    Inputs:
    df: Pandas DataFrame

    Outputs:
    A pandas DataFrame with the values in the "gender" column cleaned.
    '''

    df2 = df.copy()

    if "gender" not in df2.columns:
        return df2
    else:
        df2['gender'] = df2['gender'].apply(lambda x: str(x)[0].upper() if str(x)[0].upper() in ['M', 'F'] else "U")
        #df2['gender'] = list(map(lambda x: x[0].upper() if x[0].upper() in ['M', 'F'] else "U", df2['gender']))
        return df2

        
def checking_null_value (df:pd.DataFrame, threshold = 3)-> pd.DataFrame:
    '''
    This function takes a Pandas DataFrame, calculate the percentage of null value
    present in each column. 
    Return one dataframe showing a complete columns with their percentage of null value,
    and another dataframe showing only comlumns which have a percentage of null value
    above the input threshold.
    
    
    Input:
    df:Pandas DataFrame
    an optional threshold value: numeric (float, int)
    
    Output:
    2 Pandas DataFrame: one shows percentage of null value in all columns.
    And the other shows columns with null value percentage above the provided threshold
    '''
    
    missing_values_df = pd.DataFrame(round(df.isna().sum()/len(df),4)*100)

    missing_values_df = missing_values_df.reset_index()

    missing_values_df.columns = ['column_name', 'percentage_of_missing_values']
    column_with_null_higher_than_threshold_df = missing_values_df[missing_values_df['percentage_of_missing_values']>threshold]
    return  missing_values_df
    return  column_with_null_higher_than_threshold_df      
    

def clean_dataframe(df: pd.DataFrame, options: dict={"column_name": "state"}) -> pd.DataFrame:
    '''
    This function will take a Pandas DataFrame and it will apply the previous functions in the library
    to clean some columns of the dataframe

    Inputs: 
    df: Pandas DataFrame

    Outputs:
    Another DataFrame
    '''

    df2 = df.copy()

    df2 = lower_case_no_space_colname(df2)
    df2 = delete_unamed_column(df2)
    df2 = clean_gender_column(df2)

    return df2

def check_value_count_each_column (df:pd.DataFrame):
    '''
    This function takes the input pandas dataframe, 
    then print value_counts for each column in the dataframe
    Input:
    df: Pandas dataframe
    Output:
    none
    '''
    for cols in list(df.columns):
        print('\nValue counts of',cols,'\n',df[cols].value_counts())


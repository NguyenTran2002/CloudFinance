# universal import
from universal_imports import *

#------------------------------

def sum_category(in_df, category, start_time = '1900-01-01', end_time = '2200-12-31'):
    """
    DESCRIPTION:
        Sum the category over the time period

    INPUT SIGNATURE:
        1. in_df (pd.DataFrame): the input dataframe
        2. category (str): the category to sum
        3. start_time (string): YYYY-MM-DD format
        4. end_time (string): YYYY-MM-DD format

    OUTPUT SIGNATURE:
        1. category_sum (float): the sum of the category over the time period
    """

    # convert start_time and end_time to datetime
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)

    # filter the dataframe
    filtered_df = in_df[(in_df["Date"] >= start_time) & (in_df["Date"] <= end_time)\
        & (in_df["Category"] == category)]

    # sum the category
    category_sum = filtered_df["Amount"].sum()

    return category_sum
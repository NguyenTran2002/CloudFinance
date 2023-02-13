# universal import
from universal_imports import *

#------------------------------

def sum_category(in_df, category, start_time, end_time):
    """
    DESCRIPTION:
        Sum the category over the time period

    INPUT SIGNATURE:
        1. in_df (pd.DataFrame): the input dataframe
        2. category (str): the category to sum
        3. start_time (datetime.datetime): the start time
        4. end_time (datetime.datetime): the end time

    OUTPUT SIGNATURE:
        1. category_sum (float): the sum of the category over the time period
    """

    # filter the dataframe
    filtered_df = in_df[(in_df["Date"] >= start_time) & (in_df["date"] <= end_time)]

    # sum the category
    category_sum = filtered_df[category].sum()

    return category_sum
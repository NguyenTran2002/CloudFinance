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

#------------------------------

def sum_ALL_categories(in_df, start_time = '1900-01-01', end_time = '2200-12-31'):

    """
    DESCRIPTION:
        Sum all the categories over the time period

    INPUT SIGNATURE:
        1. in_df (pd.DataFrame): the input dataframe
        2. start_time (string): YYYY-MM-DD format
        3. end_time (string): YYYY-MM-DD format

    OUTPUT SIGNATURE:
        1. sum_categories (dict): a dictionary of the total amount spent in each category
    """

    # convert start_time and end_time to datetime
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)

    # filter the dataframe
    filtered_df = in_df[(in_df["Date"] >= start_time) & (in_df["Date"] <= end_time)]

    # get the unique categories
    categories = filtered_df.Category.unique()

    # create a dictionary to store the total amount spent in each category
    sum_categories = {}

    # loop through the categories
    for category in categories:

        # sum the category
        category_sum = sum_category(filtered_df, category, start_time, end_time)

        # add the category and sum to the dictionary
        sum_categories[category] = category_sum

    return sum_categories
# universal import
from universal_imports import *

#------------------------------

# import features
import helper

#------------------------------

def add_transaction(in_df, description, category, amount, date, account, third_party = None):
    """
    DESCRIPTIOIN
        - Add a transaction to the main dataframe with input provided by the user

    INPUT SIGNATURE:
        1. Description (str): description of the transaction
        2. Category (str): category of the transaction (hard-coded category)
        3. Amount (float): money spent on the transaction
        4. Date (str): date of the transaction
        5. Account (str): account used for the transaction
        6. Third Party (str): name of the third party involved in the transaction

    OUTPUT SIGNATURE:
        1. updated_df (pd.DataFrame): return the main dataframe with the new transaction added
    """

    # convert date to datetime object
    date = pd.to_datetime(date)

    # generate a unique ID for the new transaction
    new_id = helper.get_unique_id()

    # create a new dataframe with the new transaction
    new_transaction_df = pd.DataFrame({ \
        'Unique ID' : [new_id], \
        'Description': [description], \
        'Category': [category], \
        'Amount': [amount], \
        'Date': [date], \
        'Account': [account], \
        'Third Party': [third_party]})

    # append the new transaction to the main dataframe
    updated_df = pd.concat([in_df, new_transaction_df], axis = 0, ignore_index = True)

    # sort the dataframe by date in descending order
    updated_df = updated_df.sort_values(by = 'Date', ascending = False)

    # reset the index
    updated_df = updated_df.reset_index(drop = True)

    return updated_df
import unittest

# navigate to the Features folder
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_imports import *

# import other features
import data_manipulation
import helper

# Import testing specific libraries
from pandas.testing import assert_frame_equal

#------------------------------

class test_add_transaction(unittest.TestCase):
      
    def setUp(self):

        # read in the data
        self.main_df = pd.read_csv('Data/Test Data/Samples.csv')

        # reformat the data
        self.main_df = helper.reformat_main_df(self.main_df)

        # read in the expected result
        self.expected_df = pd.read_csv('Data/Test Data/add_transaction.csv')

        # reformat the expected result
        self.expected_df = helper.reformat_main_df(self.expected_df)

        # sort the expected_df by date in descending order
        self.expected_df = self.expected_df.sort_values(by = ['Date'], ascending = False)

        # reset the index of expected_df
        self.expected_df = self.expected_df.reset_index(drop = True)

        # drop column unique ID
        self.expected_df = self.expected_df.drop(columns = ['Unique ID'])

    def test_add_transaction(self):

        # add the first transaction
        produced_df = data_manipulation.add_transaction(\
            in_df = self.main_df, \
            description = "Added Expense for Food", \
            category = "Food and Dining", \
            amount = 100, \
            date = "2018-04-28", \
            account = "Chase Freedom Flex")[0]

        # add the second transaction
        produced_df = data_manipulation.add_transaction(\
            in_df = produced_df, \
            description = "Added Expense for Book", \
            category = "Book", \
            amount = 127, \
            date = "2030-04-11", \
            account = "Capital One Savor", \
            third_party = "Christopher")[0]

        # drop column unique ID
        produced_df = produced_df.drop(columns = ['Unique ID'])

        pd.testing.assert_frame_equal(produced_df, self.expected_df)

#------------------------------

if __name__ == '__main__':
    unittest.main()
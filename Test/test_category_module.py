import unittest

# navigate to the Features folder
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_imports import *

# import other features
import helper
import category_module

#------------------------------

class test_sum_category(unittest.TestCase):
      
    def setUp(self):
        
        # read in the sample data
        self.sample_df = pd.read_csv('Data/Test Data/Samples.csv')

        # convert column "Date" to datetime
        self.sample_df['Date'] = pd.to_datetime(self.sample_df['Date'])

        # expected results
        self.expected_dict = {
            'Business Services':621,\
            'Clothing':951,\
            'Education':288,\
            'Food and Dining':1440,\
            'Health and Fitness':427,\
            'Home':710,\
            'Pet':519,\
            'Shopping':897,\
            'Transportation':856,\
            'Uncategorized':714\
        }

    def test_sum_category(self):

        # get the unique categories in the dataframe
        unique_categories = self.sample_df['Category'].unique()

        # record the sum of each category
        category_sum_dict = {}

        for category in unique_categories:

            # get the sum of the category
            category_sum_dict[category] = category_module.sum_category(self.sample_df, category)

        self.assertEqual(category_sum_dict, self.expected_dict)

#------------------------------

class test_sum_ALL_categories(unittest.TestCase):
      
    def setUp(self):
        
        # read in the sample data
        self.sample_df = pd.read_csv('Data/Test Data/Samples.csv')

        # convert column "Date" to datetime
        self.sample_df['Date'] = pd.to_datetime(self.sample_df['Date'])

        # expected results
        self.expected_dict = {
            'Business Services':621,\
            'Clothing':951,\
            'Education':288,\
            'Food and Dining':1440,\
            'Health and Fitness':427,\
            'Home':710,\
            'Pet':519,\
            'Shopping':897,\
            'Transportation':856,\
            'Uncategorized':714\
        }

    def test_sum_ALL_categories(self):

        # get the sum
        category_sum_dict = category_module.sum_ALL_categories(self.sample_df)

        self.assertEqual(category_sum_dict, self.expected_dict)

#------------------------------

if __name__ == '__main__':
    unittest.main()
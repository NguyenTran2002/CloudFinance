import unittest

# navigate to the Features folder
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_imports import *

# import other features
import helper
import yearly

# Import testing specific libraries
from pandas.testing import assert_frame_equal

#------------------------------

class test_get_cumulative_expenses_by_day_in_a_month(unittest.TestCase):
      
    def setUp(self):
        
        # read in the sample data
        self.sample_df = pd.read_csv('Data/Test Data/Samples.csv')

        # convert column "Date" to datetime
        self.sample_df['Date'] = pd.to_datetime(self.sample_df['Date'])

        # expected results
        self.expected_2015_df = pd.read_csv('Data/Test Data/cumulative_2015.csv')
        self.expected_2019_df = pd.read_csv('Data/Test Data/cumulative_till_august_2019.csv')

    def test_get_cumulative_expenses_by_month_in_a_year(self):

        produced_2015_df = yearly.get_cumulative_expenses_by_month_in_a_year(self.sample_df, 2015)[0]
        produced_2019_df = yearly.get_cumulative_expenses_by_month_in_a_year(self.sample_df, 2019, 8)[0]

        pd.testing.assert_frame_equal(produced_2015_df, self.expected_2015_df)
        pd.testing.assert_frame_equal(produced_2019_df, self.expected_2019_df)

#------------------------------

if __name__ == '__main__':
    unittest.main()
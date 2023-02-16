import unittest

# navigate to the Features folder
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_imports import *

# import other features
import helper
import monthly

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
        self.expected_june_2016_df = pd.read_csv('Data/Test Data/cumulative_june_2016.csv')
        self.expected_august_2019_df = pd.read_csv('Data/Test Data/cumulative_august_2019.csv')

    def test_get_cumulative_expenses_by_day_in_a_month(self):

        produced_june_2016_df = monthly.get_cumulative_expenses_by_day_in_a_month(self.sample_df, 2016, 6)[0]
        produced_august_2019_df = monthly.get_cumulative_expenses_by_day_in_a_month(self.sample_df, 2019, 8)[0]

        pd.testing.assert_frame_equal(produced_june_2016_df, self.expected_june_2016_df)
        pd.testing.assert_frame_equal(produced_august_2019_df, self.expected_august_2019_df)

#------------------------------

if __name__ == '__main__':
    unittest.main()
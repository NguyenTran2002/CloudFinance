import unittest

# navigate to the Features folder
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_imports import *

# import other features
import helper

# Import testing specific libraries
from pandas.testing import assert_frame_equal

#------------------------------

class test_get_unique_id(unittest.TestCase):
      
    def setUp(self):
        
        # generate 10,000 unique IDs
        self.unique_ids = [helper.get_unique_id() for i in range(10000)]

    def test_get_unique_id(self):

        expected = True

        test_result = True

        for unique_id in self.unique_ids:

            # check if the ID is unique
            if self.unique_ids.count(unique_id) > 1:
                # print("Count: ", self.unique_ids.count(unique_id))
                test_result = False
                break;

        self.assertEqual(test_result, expected)

#------------------------------

if __name__ == '__main__':
    unittest.main()
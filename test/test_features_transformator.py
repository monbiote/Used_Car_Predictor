#if you want to test within class, import unittest and inheritance from it
import unittest

#pytest test with function start from head of test
import pytest_cov

import used_car_prediction_lib.features.transformator as tr

import pandas as pd
import numpy as np

#unittest
# with basic concepts of input and output
#use expected output compare with output from tested function
#assert if is wrong

#########################  Transformator ##################################

class TestTransformator_subclasses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    #instantiate mock object
    def setUp(self):
        # Creating a sample DataFrame
        self.df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})

        self.square_transformator = tr.Square_Transformator()
        self.normalization_transformator = tr.Normalization_Transformator()
        self.standardization_transformator = tr.Standardization_Transformator()
        self.log_transformator = tr.Log_Transformator()
    def tearDown(self):
        # Resetting the DataFrame to ensure isolation between tests
        self.df = None

    #test square transformation
    def test_square_transformation(self):
        
        squared_df = self.square_transformator.transform(self.df, 'col1')
        expected_df = self.df.copy()
        expected_df['col1'] = np.square(self.df['col1'])

        # Check transformed DataFrame
        pd.testing.assert_frame_equal(squared_df, expected_df)

    #test normalization transformation
    def test_normalization_transformation(self):
        normalized_df = self.normalization_transformator.transform(self.df, 'col1')
        
        # Calculating expected results
        col_min, col_max = self.df['col1'].min(), self.df['col1'].max()
        expected_df = self.df.copy()
        expected_df['col1'] = (expected_df['col1'] - col_min) / (col_max - col_min)

        # Assertions
        # Check transformed DataFrame
        pd.testing.assert_frame_equal(normalized_df, expected_df)


    #test standarization transformation
    def test_standardization_transformation(self):
        standardized_df = self.standardization_transformator.transform(self.df, 'col1')

        # Calculating expected results
        col_mean, col_std = self.df['col1'].mean(), self.df['col1'].std()
        expected_df = self.df.copy()
        expected_df['col1'] = (expected_df['col1'] - col_mean) / col_std

        # Assertions
        self.assertEqual(standardized_df.shape, expected_df.shape)
        self.assertListEqual(standardized_df.columns.tolist(), expected_df.columns.tolist())
        pd.testing.assert_frame_equal(standardized_df, expected_df)

    #test log transformation
    def test_log_transformation(self):
        log_df = self.log_transformator.transform(self.df, 'col1')

        # Calculating expected results
        expected_df = self.df.copy()
        expected_df['col1'] = np.log(expected_df['col1'])

        # Assertions
        self.assertEqual(log_df.shape, expected_df.shape)
        self.assertListEqual(log_df.columns.tolist(), expected_df.columns.tolist())
        pd.testing.assert_frame_equal(log_df, expected_df)

#several files---make sure its our file
if __name__ == '__main__':
    unittest.main()


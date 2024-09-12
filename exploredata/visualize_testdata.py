import unittest
from evaluation.evaluate import GenerateResultCsv

class TestGenerateResultCsv(unittest.TestCase):
    def setUp(self):
        self.generator = GenerateResultCsv()

    def test_init(self):
        self.assertIsNotNone(self.generator)

    def test_generateActual_0_with_empty_file(self):
        with open('actual_0.csv', 'w') as f:
            pass  # Create an empty file
        self.generator.generateActual_0()
        with open('actual_0.csv', 'r') as f:
            content = f.read()
        self.assertEqual(content, '')  # Check if the file is empty

if __name__ == '__main__':
    unittest.main()import unittest
    from evaluation.evaluate import GenerateResultCsv
    
    class TestGenerateResultCsv(unittest.TestCase):
        def setUp(self):
            self.generate_result_csv = GenerateResultCsv()
    
        def test_init_with_empty_file(self):
            # Create a file with only header rows
            with open('empty_file.csv', 'w') as file:
                file.write('start_district_id,time_slotid,gap\n')
    
            # Call the constructor with the empty file
            self.generate_result_csv.__init__()
    
            # Check if the object is initialized correctly
            self.assertIsNotNone(self.generate_result_csv)
    
            # Clean up the created file
            file.close()
            os.remove('empty_file.csv')
    
    if __name__ == '__main__':
        unittest.main()from order import ExploreOrder
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
from utility.datafilepath import g_singletonDataFilePath
from visualization import visualizeData
import numpy as np
import math


class VisualizeTestData(visualizeData):
    def __init__(self):
        ExploreOrder.__init__(self)
        self.gapdf = self.load_gapdf(g_singletonDataFilePath.getTest1Dir())
        return
    def run(self):
        self.disp_gap_bytimeiid()
#         self.disp_gap_bydistrict()
#         self.disp_gap_bydate()
        return
    


if __name__ == "__main__":   
    obj= VisualizeTestData()
    obj.run()
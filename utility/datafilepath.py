
class DataFilePath:
    """
    A class that provides file paths for data files used in the supply-demand forecasting project.
    """

    def __init__(self):
        """
        Initializes a new instance of the DataFilePath class.
        """
        self.dataDir = '../data/citydata/season_1/'

    def getOrderDir_Train(self):
        """
        Returns the file path for the training order data directory.
        """
        return self.dataDir + 'training_data/order_data/'

    def getOrderDir_Test1(self):
        """
        Returns the file path for the test set 1 order data directory.
        """
        return self.dataDir + 'test_set_1/order_data/'

    def getTest1Dir(self):
        """
        Returns the file path for test set 1 directory.
        """
        return self.dataDir + 'test_set_1/'

    def getTest2Dir(self):
        """
        Returns the file path for test set 2 directory.
        """
        return self.dataDir + 'test_set_2/'

    def getTrainDir(self):
        """
        Returns the file path for the training data directory.
        """
        return self.dataDir + 'training_data/'

    def getGapCsv_Train(self):
        """
        Returns the file path for the gap CSV file in the training order data directory.
        """
        return self.getOrderDir_Train() + self.getGapFilename()

    def getGapCsv_Test1(self):
        """
        Returns the file path for the gap CSV file in the test set 1 order data directory.
        """
        return self.getOrderDir_Test1() + self.getGapFilename()

    def getTestset1Readme(self):
        """
        Returns the file path for the readme file in test set 1 directory.
        """
        return self.dataDir + 'test_set_1/read_me_1.txt'

    def getTestset2Readme(self):
        """
        Returns the file path for the readme file in test set 2 directory.
        """
        return self.dataDir + 'test_set_2/read_me_2.txt'

    def getGapFilename(self):
        """
        Returns the filename for the gap CSV file.
        """
        return "temp/gap.csv"

    def getGapPredictionFileName(self):
        """
        Returns the filename for the gap prediction CSV file.
        """
        return 'gap_prediction.csv'

    def getPrevGapFileName(self):
        """
        Returns the filename for the previous gap dataframe pickle file.
        """
        return "temp/prevgap.df.pickle"

    def get_dir_name(self, data_dir):
        """
        Returns the name of the directory from the given data directory path.
        """
        return data_dir.split('/')[-2]

g_singletonDataFilePath = DataFilePath()

# Test cases for the DataFilePath class.
class DataFilePath:
    """
    A class that provides file paths for data files used in the supply-demand forecasting project.
    """

    def __init__(self):
        """
        Initializes a new instance of the DataFilePath class.
        """
        self.dataDir = '../data/citydata/season_1/'

    def getOrderDir_Train(self):
        """
        Returns the file path for the training order data directory.
        """
        return self.dataDir + 'training_data/order_data/'

    def getOrderDir_Test1(self):
        """
        Returns the file path for the test set 1 order data directory.
        """
        return self.dataDir + 'test_set_1/order_data/'

    def getTest1Dir(self):
        """
        Returns the file path for test set 1 directory.
        """
        return self.dataDir + 'test_set_1/'

    def getTest2Dir(self):
        """
        Returns the file path for test set 2 directory.
        """
        return self.dataDir + 'test_set_2/'

    def getTrainDir(self):
        """
        Returns the file path for the training data directory.
        """
        return self.dataDir + 'training_data/'

    def getGapCsv_Train(self):
        """
        Returns the file path for the gap CSV file in the training order data directory.
        """
        return self.getOrderDir_Train() + self.getGapFilename()

    def getGapCsv_Test1(self):
        """
        Returns the file path for the gap CSV file in the test set 1 order data directory.
        """
        return self.getOrderDir_Test1() + self.getGapFilename()

    def getTestset1Readme(self):
        """
        Returns the file path for the readme file in test set 1 directory.
        """
        return self.dataDir + 'test_set_1/read_me_1.txt'

    def getTestset2Readme(self):
        """
        Returns the file path for the readme file in test set 2 directory.
        """
        return self.dataDir + 'test_set_2/read_me_2.txt'

    def getGapFilename(self):
        """
        Returns the filename for the gap CSV file.
        """
        return "temp/gap.csv"

    def getGapPredictionFileName(self):
        """
        Returns the filename for the gap prediction CSV file.
        """
        return 'gap_prediction.csv'

    def getPrevGapFileName(self):
        """
        Returns the filename for the previous gap dataframe pickle file.
        """
        return "temp/prevgap.df.pickle"

    def get_dir_name(self, data_dir):
        """
        Returns the name of the directory from the given data directory path.
        """
        return data_dir.split('/')[-2]

    def test_get_order_dir_train(self):
        """
        Test case for the getOrderDir_Train function.

        This function asserts that the getOrderDir_Train function returns the correct directory path for training order data.

        Returns:
            None
        """
        assert g_singletonDataFilePath.getOrderDir_Train() == '../data/citydata/season_1/training_data/order_data/'


        g_singletonDataFilePath = DataFilePath()
        test_get_order_dir_train()
    

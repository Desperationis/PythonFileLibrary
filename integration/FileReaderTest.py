from PythonFileLibrary.src.FileReader import FileReader
import unittest

class FileReaderTest(unittest.TestCase):
    def setUp(self):
        # Init func for every test
        pass

    def tearDown(self):
        # Called after every test, successful or not
        pass

    def testA(self):
        self.assertEqual(5, 6)
    
    def testB(self):
        self.assertEqual(5, 5)
    
    def testC(self):
        pass

    def test_notatest(self):
        pass



# Only run this script if we delibrately wanted to
if __name__ == "__main__":
    unittest.main()

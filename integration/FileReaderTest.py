from PythonFileLibrary.src.FileReader import FileReader
import unittest

class FileReaderTest(unittest.TestCase):
    def setUp(self):
        # Init func for every test
        self.fileReader = FileReader("FileReaderEnvironment/RegularFile.txt")

    def tearDown(self):
        # Called after every test, successful or not
        pass

    def test_TypeException(self):
        # Check if an exception is thrown if given a file that doesn't exist
        with self.assertRaises(TypeError):
            self.fileReader = FileReader(fileName="nonexistent.txt")
        
    def test_CacheInsertion(self):
        # Test if cache is preserved when passed into file reader.
        fileCache = [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            " \n"
        ]

        self.fileReader = FileReader(fileList=fileCache)

        for index, line in enumerate(self.fileReader.Read()):
            self.assertTrue(fileCache[index] == line)

        for index, line in enumerate(self.fileReader):
            self.assertTrue(fileCache[index] == line)
    
    def test_BadConstructor(self):
        fileCache = [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            " \n"
        ]

        # Check if the file, not cache, was loaded in first. 
        self.fileReader = FileReader("FileReaderEnvironment/RegularFile.txt", fileCache)
        self.assertTrue(self.fileReader.GetFileLength() == 25)
    
    def test_Reset(self):
        self.fileReader.MoveCursorDown(10000)
        self.fileReader.ResetCursor()
        self.assertTrue(self.fileReader.cursorPosition == 0)

    def test_UpperBound(self):
        self.fileReader.MoveCursorUp(100000)
        self.assertTrue(self.fileReader.cursorPosition == 0)
    
    def test_LowerBound(self):
        self.fileReader.MoveCursorDown(100000)
        self.assertTrue(self.fileReader.cursorPosition == self.fileReader.GetFileLength() - 1)
    
    def test_ValidType(self):
        # Check if files with only ASCII are allowed.
        self.assertTrue(FileReader.ValidFileType("FileReaderEnvironment/RegularFile.txt"))
        # TODO: Check for image
    
    def test_Filename(self):
        self.assertTrue(self.fileReader.GetFilename() == "RegularFile.txt")
        # TODO: Check for ABSOLUTE PATH

        fileCache = [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            " \n"
        ]
        self.fileReader = FileReader(fileList=fileCache)
        self.assertTrue(self.fileReader.GetFilename() == "")
    
    def test_Length(self):
        self.assertTrue(self.fileReader.GetFileLength() == 25)

    
    def test_Content(self):
        # DO this
        pass



# Only run this script if we delibrately wanted to
if __name__ == "__main__":
    unittest.main()

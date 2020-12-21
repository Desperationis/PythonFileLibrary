from PythonFileLibrary.integration.FileReaderTest import FileReaderTest
from PythonFileLibrary.integration.RecursiveScannerTest import RecursiveScannerTest
import unittest

def ReaderSuite():
    readerSuite = unittest.suite.TestSuite()
    readerSuite.addTest(FileReaderTest("test_TypeException"))
    readerSuite.addTest(FileReaderTest("test_CacheInsertion"))
    readerSuite.addTest(FileReaderTest("test_BadConstructor"))
    readerSuite.addTest(FileReaderTest("test_Reset"))
    readerSuite.addTest(FileReaderTest("test_UpperBound"))
    readerSuite.addTest(FileReaderTest("test_LowerBound"))
    readerSuite.addTest(FileReaderTest("test_ValidType"))
    readerSuite.addTest(FileReaderTest("test_Filename"))
    readerSuite.addTest(FileReaderTest("test_Length"))
    readerSuite.addTest(FileReaderTest("test_Content"))
    return readerSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(ReaderSuite())

from PythonFileLibrary.integration.FileReaderTest import FileReaderTest
from PythonFileLibrary.integration.RecursiveScannerTest import RecursiveScannerTest
import unittest

def FileReaderSuite():
    readerSuite = unittest.suite.TestSuite()
    readerSuite.addTest(FileReaderTest("test_FileException"))
    readerSuite.addTest(FileReaderTest("test_PreserveCache"))
    readerSuite.addTest(FileReaderTest("test_DoubleConstructor"))
    readerSuite.addTest(FileReaderTest("test_Reset"))
    readerSuite.addTest(FileReaderTest("test_UpperBound"))
    readerSuite.addTest(FileReaderTest("test_LowerBound"))
    readerSuite.addTest(FileReaderTest("test_Filename"))
    readerSuite.addTest(FileReaderTest("test_Length"))
    readerSuite.addTest(FileReaderTest("test_CursorManipulation"))
    return readerSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(FileReaderSuite())

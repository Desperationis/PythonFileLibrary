from PythonFileLibrary.unit.FileReaderTest import FileReaderTest
from PythonFileLibrary.unit.RecursiveScannerTest import RecursiveScannerTest
import unittest

def ReaderSuite():
    readerSuite = unittest.suite.TestSuite()
    readerSuite.addTest(FileReaderTest("testA"))
    readerSuite.addTest(FileReaderTest("testB"))
    return readerSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(ReaderSuite())

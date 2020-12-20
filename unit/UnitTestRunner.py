from ReaderTest import *
from RecursiveScannerTest import *
import unittest

def ReaderSuite():
    readerSuite = unittest.suite.TestSuite()
    readerSuite.addTest(ReaderTest("testA"))
    readerSuite.addTest(ReaderTest("testB"))
    return readerSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(ReaderSuite())

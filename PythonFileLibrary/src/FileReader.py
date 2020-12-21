from PythonFileLibrary.src.HelperFunctions import OpenFileSafely

class FileReader:
    """Provides an interface to read a cached text file.

    Cached text file can be read through cursor manipulation, where the cursor
    can be moved up or down to return the current line. If the cursor is out of
    bounds, it will return either the first or last line of the file.

    Attributes:
        cursorPosition: The # of the current line the cursor is on.
    """
    
    def __init__(self, fileName : str = "", fileList : [str] = []):
        self.cursorPosition = 0
        self._filename = None
        self._fileContents = []
        

    def _CacheFile(self, location):
        # TODO: Open a file and cache it into _fileContents. If if it doesn't
        # exist, throw an exception
        pass

    @staticmethod
    def ValidFileType(fileName: str) -> bool:
        # TODO: Check if a file can be read using this class via checking
        # for ASCII encoding. 
        pass

    def GetFilename(self) -> str:
        # TODO: Return the filename of the file.
        pass

    def GetFileLength(self) -> int:
        # TODO: Pass length of cache. 
        pass

    def ResetCursor(self):
        # TODO: Make a function that resets the cursor to the top of the page. 
        pass

    def Read(self) -> str:
        # TODO: Make a function that yields the cached current line while
        # changing cursor position. 
        pass

    def __iter__(self) -> str:
        # TODO: Pump Read() through here
        pass

    def MoveCursorUp(self, amount : int = 1):
        # TODO: Implement a func that moves the cursor up from a positive
        # integer, even when reading a file. If the amount reaches the top of a
        # file, set the cursor to the top of the file. 
        pass

    def MoveCursorDown(self, amount : int = 1):
        # TODO: Implement a func that moves the cursor down from a positive
        # integer, even when reading a file. If the amount reaches the bottom of
        # the file, set the cursor to the top of the file. 
        pass

    def ReachedEnd(self) -> bool:
        # TODO: Check when we have reached the end of the file.
        pass

from PythonFileLibrary.src.HelperFunctions import OpenFileSafely

class FileReader:
    """Provides an interface to read a cached text file.

    Cached text file can be read through cursor manipulation, where the cursor
    can be moved up or down to return the current line. If the cursor is out of
    bounds, it will return either the first or last line of the file.
    """
    
    def __init__(self, fileName : str):

        #self.cursorPosition = 0
        

        self.fileName = fileName
        self.file = OpenFileSafely(fileName, "r", True)
        self.canParse = self.file is not None

        if self.canParse:
            self.lines = self.file.readlines()
            self.currentLine = 0


    def ResetCursor(self):
        # TODO: Make a function that resets the cursor to the top of the page. 
        pass

    def Read(self) -> str:
        # TODO: Make a function that yields the current line while changing
        # cursor position. 
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



    # Resets the reader's cursor to the top.
    def ResetReader(self):
        if self.canParse:
            self.currentLine = 0

    # Returns whether or not the parse has reached the end of the file.
    #def ReachedEnd(self):
     #   return self.currentLine == len(self.lines) - 1

    # Returns the current line.
    def GetCurrentLine(self):
        if self.canParse:
            return self.lines[self.currentLine]
        return "Can't get line; File not opened."

    # View the next line without commiting.
    def PeekNextLine(self):
        nextLine = min(self.currentLine + 1, len(self.lines) - 1)
        return self.lines[nextLine]

    # Returns the next line. CleanRead() will skip ahead this line.
    def GetNextLine(self):
        if self.canParse:
            # Read next line
            self.SkipLine()
            self.currentLine = min(self.currentLine, len(self.lines) - 1)

            return self.GetCurrentLine()

        return "Can't get line; File not opened."

    # Yield function that spits out the lines of the file.
    def CleanRead(self):
        # Function that yields the next non-null line
        if self.canParse:
            yield self.GetCurrentLine()

            while not self.ReachedEnd():
                yield self.GetNextLine()
        else:
            yield "Cannot parse file"

    # Skips a number of lines (negative or positive)
    def SkipLine(self, amount = 1):
        self.currentLine += amount

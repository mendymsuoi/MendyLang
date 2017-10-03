import library, mTypes
def Tokenize(command):
    tokens=mTypes.List(str)
    startswithcommand=command.StartsWith(library.library.keys)
    if startswithcommand:
        tokens.Add(startswithcommand)
from mtypes import *
import library


def startsWith(string, list_):
    for item in list_:
        if string.startswith(item):
            return item
    return False

    
def tokenize(line):
    out=[]
    easyString=False
    while line:
        a=startsWith(line, library.library.keys)
        if easyString:
            out.append("")
            for character in line:
                if easyString:
                    if character!=";":
                        out[len(out)-1]+=character
                        line=line[1:]
                    else:
                        out.append("")
                        out[len(out)-1]+=character
                        line=line[1:]
                        easyString = False
        else:
            out.append(a)
            line=line[len(a):]
            if a == "\\":
                easyString=True;
                out.append("\"")
    while "" in out:
        out.remove("")
    while " " in out and out[out.index(" ")-1]!="\\":
        out.remove(" ")
    return out
    
# for token in tokenize("print \\hello"):
#     print(token)
print(tokenize("print \\Hello world;print \\hello;print \\ "))

# def s(string, list_):
#     try:
#         return list_.index(string)
#     except ValueError:
#         return False;
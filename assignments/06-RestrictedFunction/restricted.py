import os, inspect, sys
def jaa8r():
    #curFile = os.path.abspath(__file__)
    curFile = os.path.abspath(__file__)
    callFile = inspect.getouterframes(inspect.currentframe(), 4)[1][1]
    if (callFile[0:1] == ".") : callFile = callFile[1:]
    #print(curFile, callFile)
    if (callFile in curFile): print("Banana.")
    else : print("Access Denied")
#print("In file: ")
#jaa8r()
#print()

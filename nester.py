def print_lol(theList):
    for eachItem in theList:
        if isinstance(eachItem , list):
            print_lol(eachItem)
        else:
            print(eachItem)

    

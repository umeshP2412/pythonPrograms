def switcher(inp):
    myDict = {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    } 
    print(myDict.get(inp,"Invalid input"))

inp = int(input("Give value for day: "))
switcher(inp)  
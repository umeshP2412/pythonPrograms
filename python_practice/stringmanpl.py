def stringmani(line):
    l = line.split(" ")
    return "-".join(l)


if __name__ == "__main__":
    line = input("Give line: ")
    y = stringmani(line)
    print(y)
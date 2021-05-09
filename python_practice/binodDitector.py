import os

def isBinod(filename):
    file = open(filename,'r')
    content = file.read()
    if 'binod' in content.lower():
        return True
    else:
        return False

if __name__ == '__main__':
    path = '\\Programs\\nester\\python_practice'
    dir_files = os.listdir(path)
    print(dir_files)  
    nBinod = 0
    for item in dir_files:
        if item.endswith('txt'):
            flag = isBinod(item)
            if (flag):
                print(f"binod detected in {item}")
                nBinod += 1
            else:
                print(f"binod not detected in {item}")
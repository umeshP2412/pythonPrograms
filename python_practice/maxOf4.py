a = int(input("Give value a: "))
b = int(input("Give value b: "))
c = int(input("Give value c: "))
d = int(input("Give value d: "))

if a>b:
    if a>c:
        if a>d:
            print(f"a is max: {a}")
        else:
            print(f"d is max: {d}")
    else:
        if c>d:
            print(f"c is max: {c}")
        else:
            print(f"d is max: {d}")
else:
    if b>c:
        if b>d:
            print(f"b is max: {b}")
        else:
            print(f"d is max: {d}")
    else:
        if c>d:
            print(f"c is max: {c}")
        else:
            print(f"d is max: {d}")
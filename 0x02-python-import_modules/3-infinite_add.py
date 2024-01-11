#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = 0
    for n in range(1, len(argv)):
        x += int(argv[n])
    print("{}".format(x))

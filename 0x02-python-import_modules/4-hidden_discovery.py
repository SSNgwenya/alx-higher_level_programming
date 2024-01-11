#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    a = dir()
    for x in range(0, len(a)):
        if a[x][:2] != "__":
            print("{:s}".format(a[x]))

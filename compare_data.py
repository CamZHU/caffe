#!/usr/bin/python3
import sys


if __name__ == '__main__':
    assert(len(sys.argv) == 3)
    with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2:
        d1 = list(map(float, f1.readline().split()))
        d2 = list(map(float, f2.readline().split()))
        print(len(d1))
        print(len(d2))
        for i in range(len(d1)):
            try:
                assert(d1[i] == d2[i])
            except:
                print(i, d1[i], d2[i])
                raise

#!/usr/bin/env python3
import sys

argv = sys .argv[1:]

if len(argv) == 0:
    print("none")
else:
    for word in args:
        if not word.endswith("ism"):
            print(word + "ism")

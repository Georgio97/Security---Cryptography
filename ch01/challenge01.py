#!/usr/bin/python3

import sys
import os
import base64

def file_get_content(filename):
        file_content = []
        line = ""

        try:
                file = open(filename, "r")
                line = file.readline()[:-1]
                while (line != None and len(line) > 0):
                        file_content.append(line)
                        line = file.readline()[:-1]
                return file_content
        except:
                sys.stderr.write("Error: Can't open file\n")
                exit(84)


def main():
        try:
                if (len(sys.argv) != 2):
                        sys.stderr.write("Error: too few arguments\n")
                        exit(84)
                file_content = file_get_content(sys.argv[1])
                if (not(len(file_content))):
                        sys.stderr.write("Error: File seems to be empty\n")
                        exit(84)
                for item in file_content:
                        test = base64.encodebytes(bytes.fromhex(item))
                        print(bytes.decode(test), end="")
        except:
                exit(84)

if __name__ == "__main__":
        main()

exit(0)
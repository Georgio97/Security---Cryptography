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
                result = ""
                if (len(sys.argv) != 2):
                        sys.stderr.write("Error: too few arguments\n")
                        exit(84)
                file_content = file_get_content(sys.argv[1])
                if (len(file_content) != 2):
                        sys.stderr.write("Error: File seems to leak data\n")
                        exit(84)
                elif (len(file_content[0]) != len(file_content[1])):
                        sys.stderr.write("Error: Different length between two strings")
                        exit(84)
                b1 = bytes.fromhex(file_content[0])
                b2 = bytes.fromhex(file_content[1])
                for i in range(0, len(b1)):
                        tmp = hex(b1[i] ^ b2[i])[2:]
                        result += "0" + tmp if (len(tmp) == 1) else tmp
                print(result.upper())
        except:
                exit(84)

if __name__ == "__main__":
        main()

exit(0)
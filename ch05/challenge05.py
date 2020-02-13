#!/usr/bin/python3

import os
import sys
import re

def error(msg, name=sys.argv[0]):    
    print('%s:' % name, msg, file=sys.stderr)
    sys.exit(84)

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
                error("Error: Can't open file\n")
                exit(84)

def main(args):
    if (len(sys.argv) != 2):
                error("Error: too few arguments\n")
                exit(84)
                file_content = file_get_content(sys.argv[1])
                if (len(file_content) != 2):
                        error("Error: File seems to leak data\n")
                        exit(84)
                elif (len(file_content[0]) != len(file_content[1])):
                        error("Error: Different length between two strings")
                        exit(84)
    try:
        with open(args[1], 'r') as f:
            key = bytes.fromhex(re.sub(r'\s', '', f.readline()))
            data = bytes.fromhex(re.sub(r'\s', '', f.read()))
            if (len(key) == 0 or len(data) == 0):
                raise ValueError()
    except ValueError:
        error('invalid data in file', name=args[1])

    print(bytes(data[1] ^ key[i % len(key)] for i in range(len(data))).hex().upper())

if __name__ == '__main__':
    main(sys.argv)
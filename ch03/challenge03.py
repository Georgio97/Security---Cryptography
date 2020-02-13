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

def single_bytes_xor(bytes_string, single_byte):
        result = ""

        for i in range(0, len(bytes_string)):
                tmp = chr(bytes_string[i] ^ single_byte[0])
                result += tmp
        return result

def get_english_score(string):
        score = 0
        frequencies = {
                'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
                'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
                'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
                'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
                'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
                'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
                'y': .01974, 'z': .00074, ' ': .13000
        }

        score = sum([frequencies.get(byte, 0) for byte in string.lower()])
        return score

def main():
        try:
                potential_english = {}

                if (len(sys.argv) != 2):
                        sys.stderr.write("Error: too few arguments\n")
                        exit(84)
                file_content = file_get_content(sys.argv[1])
                if (len(file_content) != 1):
                        sys.stderr.write("Error: File seems to leak data\n")
                        exit(84)
                b1 = bytes.fromhex(file_content[0])
                for i in range(0, 255):
                        b2 = bytearray.fromhex('{:02x}'.format(i))
                        potential_english['{:02x}'.format(i)] = get_english_score(single_bytes_xor(b1, b2))
                result = sorted(potential_english.items(), reverse= True, key= lambda items: items[1])
                print (result[0][0].upper())
        except:
                exit(84)

if __name__ == "__main__":
        main()

exit(0)
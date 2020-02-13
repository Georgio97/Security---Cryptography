#!/usr/bin/python3

import os
import sys
import re
import base64

ETAOIN = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
}

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
    if len(args) != 2:
        error('invalid number of arguments')
    try:
        with open(args[1], 'r') as f:
            data = bytes.fromhex(re.sub(r'\s', '', f.read()))
            if len(data) == 0:
                raise ValueError()
    except ValueError:
        error('invalid data in file', name=args[1])

    def avg(l):
        return sum(l) / len(l)

    def szip(l, step):
        return zip(*(l[i::step] for i in range(step)))

    keysizes = sorted(range(1, 41), key=lambda keysize: avg([sum(bin(a ^ b).count('1') for a, b in zip(a, b)) / keysize for a, b in szip([data[i:i+keysize] for i in range(0, len(data), keysize)], 2)]))[:5]
    scores = []
    for keysize in keysizes:
        key = bytes(max(range(256), key=lambda k: sum(ETAOIN[b] for b in map(lambda b: chr(b^k), data[i::keysize]) if b in ETAOIN)) for i in range(keysize))
        score = sum(ETAOIN[b] for b in map(lambda x: chr(x[1]^key[x[0] % len(key)]), enumerate(data)) if b in ETAOIN)
        scores.append((key, score))
    key = sorted(scores, key=lambda x: (x[1], 1 / len(x[0])))[-1][0]
    print(key.hex().upper())

if __name__ == '__main__':
    main(sys.argv)
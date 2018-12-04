import os
import collections
from random import shuffle, SystemRandom

sysrand = SystemRandom()

def frandom():
    ret = sysrand.random()
    for i in range(sysrand.randint(1,100)):
        ret = ret * sysrand.random()
    return ret

def rshuffle(bag,nshuf=10):
    for i in range(sysrand.randint(1,nshuf)):
        shuffle(bag,frandom)

def avoid(fname):
    if fname in ['.DS_Store']: return True
    else: return False

def tokenize(line):
    return [ x.strip() for x in line.split() ]

def get_file_contents(folder):
    tokens = []
    for i in os.listdir(folder):
        if avoid(i): continue
        path = os.path.join(folder,i)
        if os.path.isdir(path):
            return get_file_contents(path)
        else:
            tokens.extend(tokenize(open(path, encoding='utf-8').read()))
    return tokens

tokens = get_file_contents('diary')
shuffle(tokens,SystemRandom().random)
text = " ".join(tokens)
counter = collections.Counter()
counter.update(tokens)

with open("tmp.txt","w",encoding='utf-8') as f:
    f.write(text)

import json
with open('wordcount.json', 'w', encoding='utf-8') as fp:
    json.dump(counter, fp, indent=4, sort_keys=True, ensure_ascii=False)        
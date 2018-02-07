import collections

from collections import defaultdict
from collections import Counter
import sys
od = collections.OrderedDict()
from collections import OrderedDict

f = "s.txt"
f = open(f, "r")

wordcount = Counter(f.read().split())

f.close()

f = "s.txt"
f = open(f, "r")
wc2={}
for word in f.read().split():
    if word not in wc2:
        wc2[word] = 1
    else:
        wc2[word] += 1



c3 = OrderedDict(sorted(wc2.items(), key=lambda t: t[1]))
print c3
print wordcount
f.close()



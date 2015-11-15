import heapq
from collections import Counter,namedtuple

class N(namedtuple("N",["left","right"])):
    def opt(self,code,acc):
        self.left.opt(code, acc +"0")
        self.right.opt(code,acc +"1")

class le(namedtuple("le",["char"])):
    def opt(self, code, acc):
        code[self.char] = acc or "0"

def s_encode(s):
    h = []
    for ch, fr in Counter(s).items():
        h.append((fr,len(h),le(ch)))
    heapq.heapify(h)

    cnt = len(h)
    while len(h) > 1:
        fr1, _cnt1, left = heapq.heappop(h)
        fr2, _cnt2, right = heapq.heappop(h)
        heapq.heappush(h,(fr1 + fr2, cnt, N(left, right)))
        cnt += 1

    code ={}
    if h:
        [(_fr, _cnt, root)]=h
        code = {}
        root.opt(code,"")
    return code

def main():
    s = input()
    code = s_encode(s)
    en_coded = "".join(code[ch] for ch in s)
    print(len(code), len(en_coded))
    for ch in sorted(code):
        print("{}: {}".format(ch,code[ch]))
    print(en_coded)

main()




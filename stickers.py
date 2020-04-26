from collections import Counter
from functools import lru_cache
stickers = ["with", "example", "science"]
target = "thehat"


stickers = [Counter(s) for s in stickers]
inf = float('inf')


@lru_cache(None)
def query(s):
    """
    s: a string
    """
    print("s", s)
    if not s:
        return 0
    c = Counter(s)
    print("c : ", c)

    ans = inf
    for st in stickers:
        print("st : ", st)
        print("s[-1] : ", s[-1])

        if s[-1] not in st:
            continue
        ns = ""
        for k, v in c.items():
            ns += k * (max(0, v - st[k]))

        print("ns : ", ns)
        ans = min(ans, query(ns) + 1)
        print("ans : ", ans)
    return ans

ans = query(target)
print(ans)
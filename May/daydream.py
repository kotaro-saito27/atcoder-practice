s = input()

def solve(query):
    while True:
        for frag in ("erase", "eraser", "dream", "dreamer"):
            if query.endswith(frag):
                query = query[:-len(frag)]
                break
        if not query:
            print('YES')
        else:
            print('NO')

solve(s)
#
def wrongsubs(n, k):
    n = str(n)
    n = list(n)
    n = [int(item) for item in n]
    # print(n)
    for i in range(k):
        m =  n.pop()
        if m != 0:
            n.append(m - 1)
    # print(n)
    res = ""
    for i in range(len(n)):
        res += str(n[i])
    print(res)
[n, k] = [int(item) for item in  list(input().split(" "))]
wrongsubs(n, k)

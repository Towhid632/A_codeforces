tests = int(input())
for _ in range(tests):
    [a,b,c] = [int(item) for item in input().split(" ")]
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")


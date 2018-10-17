
t = int(input())

for x in range(t):

    n = int(input())
    ans = ((n ** 2) * 2) - (n ** 2)

    print(ans % 1000000007)

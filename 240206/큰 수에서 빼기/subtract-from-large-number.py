a, b = map(int, input().split())

ans = 0
if a > b :
    ans = a - b
else:
    ans = b - a

print(ans)
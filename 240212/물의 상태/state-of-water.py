temp = int(input())

if temp < 0:
    print('ice')
elif 0 <= temp < 100:
    print('water')
else:
    print('vapor')
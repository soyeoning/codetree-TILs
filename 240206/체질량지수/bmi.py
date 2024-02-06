height, weight = map(int, input().split())

height_m = height / 100
BMI = int(weight / (height_m ** 2))

print(BMI)

if BMI > 25:
    print('Obesity')
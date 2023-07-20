# 구구단 만들기
for i in range(2, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)
    print()

# 커피자판기 만들기
money, price = map(int, input().split())

if money >= price:
    print('커피 나왔습니다! 거스름돈은', str(money % price) + '원',  '입니다')
else:
    print('돈이 부족합니다.')

# 체질량지수 구하기
weight, height = map(int, input().split())
bmi = weight/height**2
if bmi >= 30:
    print('비만입니다.')
elif 25 <= bmi <= 29.9:
    print('과체중입니다.')
elif 18.5 <= bmi <= 24.9:
    print('정상입니다.')
else:
    print('저체중입니다.')
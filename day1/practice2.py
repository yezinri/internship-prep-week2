# 구구단 만들기
def multifly_box():
    for i in range(2, 10):
        for j in range(1, 10):
            print(i, '*', j, '=', i*j)
        print()

# multifly_box()

# 커피자판기 만들기
coffee_dictionary = {
    "americano": {
        "price": 2000,
        "type": "ice",
    },
    "latte": {
        "price": 3000,
        "type": "ice",
    }
}

def vending_machine():
    amount = int(input('돈을 넣어주세요 : '))
    coffee = input('커피를 주문해주세요 : ')
    if coffee_dictionary.get(coffee):
        coffee_info = coffee_dictionary[coffee]
        price = coffee_info['price']
        if amount >= price:
            print(f'거스름돈은 {amount - price} 입니다.')
        else:
            print('돈이 부족합니다.')
    else:
        print('주문하신 메뉴가 없습니다.')

# vending_machine()

# 체질량지수 구하기
def get_bmi():
    weight = int(input('몸무게를 입력해주세요 : '))
    height = int(input('키를 입력해주세요 : '))
    bmi = weight/(height*0.01)**2
    if bmi >= 30:
        print('비만입니다.')
    elif bmi >= 25:
        print('과체중입니다.')
    elif bmi >= 18.5:
        print('정상입니다.')
    else:
        print('저체중입니다.')

# get_bmi()
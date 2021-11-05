class Icecream:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor
        #이름: name, 맛: flavor, 설명:description

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f'이름: {self.name}\t맛: {self.flavor}'


class Cup:
    _CUP_CATRGORIES = ['싱글컵', '더블컵', '파인트']
    _PRICES = [4000, 6200, 8200]

    #_CUP_CATRGORIES[self.count_flovor-1]
    def __init__(self, name, count_flavor):
        self.name = name
        self.count_flavor = count_flavor
        self.price = Cup._PRICES[self.count_flavor -1]
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        엄마는_외계인 = Icecream('엄마는 외계인', '초콜릿, 바닐라, 초콜릿과자')
        엄마는_외계인.set_description('밀크 초콜릿, 다크 초콜릿, 화이트 무스 세 가지 아이스크림에 달콤 바삭한 초코볼이 더해진 아이스크림')

        베리베리_스트로베리 = Icecream('베리베리_스트로베리', '딸기, 스트로베리')

        아빠는딸바봉 = Icecream('아빠는딸바봉', '딸기, 바닐라')

        self.menu.append(엄마는_외계인)
        self.menu.append(베리베리_스트로베리)
        self.menu.append(아빠는딸바봉)

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index+1, icecream)
    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()                 #메뉴 보여주기
            flavor = input('맛을 고르세요: ')  #사용자 선택
            flavor = int(flavor)             #인덱스를 위해 문자 -> 숫자
            icecream = self.menu[flavor -1]  #메뉴에서 인덱스로 가져오자
            self.order_menu.append(icecream) #주문한 메뉴에 추가하자
        print('주문한 아이스크림입니다.')
        for icecream in self.order_menu:     #주몬내역 보여주자
            print(icecream)

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}\t종류: {Cup._CUP_CATRGORIES[self.count_flavor -1]}'

# 이지꺼 = Cup('더블컵', 2)
# print(이지꺼)
# 이지꺼.order()

나현이꺼 = Cup('싱글컵', 1)
나현이꺼.order()
print(나현이꺼)

class Recipe:
    def __init__(self, name):
        # 재료
        self.whatin = {}  #dictionary : key-value 형태의 값으로 저장할 수 있는 자료구조이다. (key값으로 찾고 싶을 때 사용)
        # 이름
        self.name = name
        # 조리 시간
        self.time = ''  # string 형
        # 영상 주소
        self.link = ''  # string 형
        # 설명
        self.info = ''
        # 몇 인분인지
        self.quantity = 1  # 1로 초기화

    def set_link(self):
        link = input('>> 레시피 영상 주소를 입력하세요 : ')
        self.link = '입력된 주소가 없습니다.' if link == '' else link

    def set_info(self):
        info = input('>> 레시피 정보를 입력하세요 : ')
        self.info = '입력된 주소가 없습니다.' if info == '' else info

    def set_quantity(self):
        quantity = input('>> 레시피가 몇 인분 기준인가요? :')
        self.quantity = 1 if quantity =='' else quantity

    def set_time(self):
        time = input('>> 레시피 소요시간을 입력하세요 : ')
        self.time = 0 if time == '' else time

    def set_whatin(self):
        while True:
            whatin = input('>> 재료를 입력하세요(예시: 감자 100) : (입력이 끝나면 enter를 치세요)')
            if whatin == '':
                break
            name, gram = whatin.split()  # ()안에 안써주면 초기값을 의미, split은 문자열만 가능
            self.whatin[name] = gram + 'g'   # dictionary


    def set_recipe(self):
        self.set_link()
        self.set_whatin()
        self.set_time()
        self.set_info()
        self.set_quantity()


    def __str__(self):
            return f'레시피 : {self.name}\n양 : {self.quantity}인분\n정보 : {self.info}\n링크 : {self.link}'\
                   f'\n재료 : {self.whatin}\n시간 : {self.time}분'

# 김치찌개 = Recipe('김치찌개')
# 김치찌개.set_whatin()
# 김치찌개.set_info()
# 김치찌개.set_time()
# print(김치찌개)

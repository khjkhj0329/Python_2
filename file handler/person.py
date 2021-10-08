class Person:
    def __init__(self, name, music):
        self.name = name
        self.musin = music
    def __str__(self):  #self에 name, age가 들어있다
        return f'이름: {self.name}\t좋아하는 음악: {self.musin}'
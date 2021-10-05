print('한꺼번에 전체 읽기')
# f = open('text.txt', 'r', encoding='utf-8')
# data = f.read()
# f.close()
# print(data)
with open('text.txt', 'r', encoding='utf-8') as f:
    data = f.read()
print(data)

print('한 줄씩 읽기')
with open('text.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()     #한줄씩 읽기 / line" 'hello\n
        if line == '':          #파일에서 읽어올 내용 없으면, 끝
            break
        print(line.rsplit())    #print('hello')

print('한 꺼번에 전체 읽어서, 한줄 씩 리스트')
with open('text.txt', 'r', encoding='utf-8') as f:
    lines = f.readline()
    # print(lines)
for line in lines:
    print(line.rsplit())
import pickle
from save_object import Person

# 객체 하나 가져오기
with open('object.bin', 'rb') as f:
    data = pickle.load(f)
print(data)

# 리스트 객체 가져오기
with open('object.bin', 'rb') as f:
    data = pickle.load(f)
for d in data:
    print(d)
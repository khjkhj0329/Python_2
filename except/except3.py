list1 = [1, 5, 7]
try:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    # print(list1[3])     # IndexError
except IndexError as e:
    print(e)
except:
    pass
else:
    print('μ±κ³΅!!!ππ``        ')
finally:
    print('κΌ­ μ€νν΄μΌνλ μ½λ')
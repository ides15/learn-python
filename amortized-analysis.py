import timeit

def test2(n):
    ls = []
    for number in range(n):
        t = timeit.timeit("nest(" + str(number) +")", setup="from __main__ import nest", number=1)
        ls.append(t)
    return ls

print(test2(50))
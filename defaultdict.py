from collections import defaultdict

dd = defaultdict(int) # int parameter is just the function int() which returns 0

words = str.split('red blue green red yellow blue red green green red')

for word in words:
    dd[word] += 1
    print(dd)

print(dd)
# above works because defaultdict will generate a key instead of throwing KeyError

# d = dict()

# words1 = str.split('red blue green red yellow blue red green green red')

# for word in words:
#     d[word] += 1
#     print(d)
# above won't work because d doesn't already have those keys

def isprimary(c):
    if (c == 'red') or (c == 'blue') or (c == 'green'):
        return True
    return False

dd2 = defaultdict(bool)

for word in words:
    dd2[word] = isprimary(word)

print(dd2)
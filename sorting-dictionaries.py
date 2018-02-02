from pprint import pprint

def wordcount(fname):
    fhand = open(fname)

    count = dict()
    for line in fhand:
        words = line.split()

        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

    return count

d = wordcount('functions.py')

[(key, d[key]) for key in sorted(d, key=d.__getitem__, reverse=True)]
# prints the word and number of occurances in a file sorted by number of occurances (value)

[(key, d[key]) for key in sorted(d, key=len, reverse=True)]
# prints the word and number of occurances in a file sorted by the len of the word (len(key))

count = wordcount('functions.py')
filtered = {key: value for key, value in count.items() if value < 11 and value > 3}

pprint(filtered)
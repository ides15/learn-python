d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}

d2 = {
    'one': 'un',
    'two': 'deux',
    'three': 'trois',
    'four': 'quatre',
    'five': 'cinq'
}

print([d2[key] for key in sorted(d2, key=d.__getitem__)])
# ['un', 'deux', 'trois', 'quatre', 'cinq']

# print(d) --> dictionary in JSON format
# print(list(d)) --> list of keys
# print(sorted(d)) --> list of keys sorted by key
# print(sorted(d.items())) --> list of key value pairs
# print(d.keys()) --> dictionary list of keys
# print(d.values()) --> dictionary list of values
textfile = open('./cs2107assign1/encrypted_message.txt')
# Oxford English Corpus:
letter_frequencies = {
    "a": 0.08167,
    "b": 0.01492,
    "c": 0.02782,
    "d": 0.04253,
    "e": 0.12702,
    "f": 0.02228,
    "g": 0.02015,
    "h": 0.06094,
    "i": 0.06966,
    "j": 0.00153,
    "k": 0.00772,
    "l": 0.04025,
    "m": 0.02406,
    "n": 0.06749,
    "o": 0.07507,
    "p": 0.01929,
    "q": 0.00095,
    "r": 0.05987,
    "s": 0.06327,
    "t": 0.09056,
    "u": 0.02758,
    "v": 0.00978,
    "w": 0.0236,
    "x": 0.0015,
    "y": 0.01974,
    "z": 0.00074
}

lettercountfile = {};

originalText = textfile.read()
text = originalText.lower()
totalcnt = len(text)
for i in range(totalcnt):
    char = text[i];
    if(char.isalpha()) :
        if char in lettercountfile:
            lettercountfile[char]+=1
        else:
            lettercountfile[char]= 1
        

for key in lettercountfile:
    lettercountfile[key]/=totalcnt;

# def get_closest_key(dict_obj, initial_value):
#     closest_key = None
#     closest_distance = float('inf')
#     for key, value in dict_obj.items():
#         distance = abs(value - initial_value)
#         if distance < closest_distance:
#             closest_distance = distance
#             closest_key = key
#     return closest_key

sortedCounts = sorted(lettercountfile.items(), key=lambda x: x[1], reverse = True)
letter_frequencies = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse = True)
# print(letter_frequencies)
# freqorder = ""
mapping = {}
for i, (c, _) in enumerate(sortedCounts):
    print(c, letter_frequencies[i][0])
    mapping[c] = letter_frequencies[i][0]

# current mapping
# k e
# d t
# p a
# b o -> i
# r i -> o -> s
# g n
# c s -> o
# x h -> d -> r
# v r -> l
# j d -> h
# m l -> r -> c
# z c -> r -> u
# o u -> r -> d
# a m -> y
# n w -> f
# y f -> w -> m
# t g -> p
# i y -> m -> w -> g
# l p -> b
# f b -> p -> q
# e v
# s k -> w
# h j
# w x
# q q -> p -> g -> w

# manual mapping
mapping['h'] = 'k'
mapping['s'] = 'w'
mapping['t'] = 'p'
mapping['n'] = 'f'
mapping['y'] = 'm'
mapping['q'] = 'z'
mapping['b'] = 'i'
mapping['r'] = 's'
mapping['c'] = 'o' 
mapping['j'] = 'h'
mapping['x'] = 'r'
mapping['l'] = 'b'
mapping['f'] = 'q'
mapping['v'] = 'l'
mapping['m'] = 'c'
mapping['z'] = 'u'
mapping['o'] = 'd'
mapping['a'] = 'y'
mapping['i'] = 'g'
newStr = ""
for i in range(len(text)):
    char = text[i];
    if(char.isalpha()):
        convertchar = mapping[char]
        if(char.isupper()):
            newStr += convertchar.upper()
        else:
            newStr += convertchar
    else:
        newStr += char


print(newStr)
    
    

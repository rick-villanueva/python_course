#Counter - dictionary subclass

from collections import Counter

l = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4]

Counter(l)

s = 'aaasssvvvvvvvvvv'

Counter(s)

s2 = 'How many time does each word show up in this sentence word word word show'

words = s2.split()

Counter(words)

c = Counter(words)
c.most_common()
c.most_common(2)

sum(c.values()) #how many words

#defaultdict
from collections import defaultdict

d = {'k1':1}
d['k1']

#assings a predetermined value
d2 = defaultdict(object)

d2['one']

d2 = defaultdict(lambda : 0)

d2['one']

#OrderedDict

dict_1 = {}
dict_1['a'] = 2
dict_1['b'] = 3
dict_1['c'] = 4
dict_1['d'] = 5
dict_1['e'] = 6

dict_1

#No order
for k,v in dict_1.items():
    print(k,v)

from collections import OrderedDict

dict_1 = OrderedDict()

dict_1['a'] = 2
dict_1['b'] = 3
dict_1['c'] = 4
dict_1['d'] = 5
dict_1['e'] = 6

for k,v in dict_1.items():
    print(k,v)
    
#namedtuple
t = (1,2,3)
t[0]

from collections import namedtuple

#Creates a quick class
Dog = namedtuple('Dog','age breed name',)

sam = Dog(age=2,breed='Lab',name='Sammy')

sam.age

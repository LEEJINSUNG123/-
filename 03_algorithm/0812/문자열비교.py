s1 = 'abc'
s2 = 'abc'
print(s1 == s2)
print(s1 is s2)
print(id(s1), id(s2))

s5 = s1[:2] + 'c'
# s4 = s1[:2]
# s5 = s4 + 'c'
print(s1 == s5)
print(s1 is s5)
print(id(s1), id(s5))

import sys
print(sys.getsizeof(s1, str))
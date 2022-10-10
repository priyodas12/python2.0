from ast import operator
from itertools import accumulate
import operator
a = list(range(1, 10))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
acc = accumulate(a)

print(a)
print(list(acc))

acc = accumulate(a, func=operator.mul)
print(list(acc))

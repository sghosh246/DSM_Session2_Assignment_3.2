# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:18:26 2018
@author: souravg
To Do: 
    Implement List comprehensions to produce the following lists.
    Write List comprehensions to produce the following Lists
    ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
    ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
    ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
    [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
    [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
    [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
"""

list = ['ACADGILD']
print([letter for letter in list])  # Output : ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

listtimes = range(1,5)
listletter = ['x','y','z']
print([i*j for i in listletter for j in listtimes])  # Output : ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

listtimesouter = range(1,3)
listtimesinner = range(1,3)
listletter = ['x','y','z']
print([k*j*i for i in listtimesouter for j in listtimesinner for k in listletter])  # Output : ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']

listouter=range(2,5)
listinner=range(3)
print([[i+j] for i in listinner for j in listouter])  #Output :  [[2], [3], [4], [3], [4], [5], [4], [5], [6]]

list=[2,3,4,5]
print([list(map(lambda x:x+j, list)) for j in range(4)])  #Output :  [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

listouter=[1,2,3]
listinner=[1,2,3]
print([(j,i) for i in listouter for j in listinner])  #Output :  [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]









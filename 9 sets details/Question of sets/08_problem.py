# what is the length of the following set
"""
s=set()
s.add(20)
s.add(20.0)
s.add('20)
"""

s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

# the output is 2 because 20 and 20.0 is equal treated in python

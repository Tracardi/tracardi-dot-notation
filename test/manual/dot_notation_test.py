from dotty_dict import dotty

from tracardi_dot_notation.dot_accessor import DotAccessor

dot = DotAccessor(profile={"a": 1, "b": [1, 2]}, session={"b": 2})
a = dot['profile@...']
b = dot['profile@b.1']
print(a, b)

x = dotty({"a":[1, 2]})
print(x['a.0'])
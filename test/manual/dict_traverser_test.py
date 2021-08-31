from tracardi_dot_notation.dict_traverser import DictTraverser
from tracardi_dot_notation.dot_accessor import DotAccessor

template = {
    "x": {
        "a": "session@...",
        "b": {"x": [1]},
        "c": [111, 222, "profile@a"],
        "d": {"q": {"z": 11, "e": 22}}
    }
}

# template = ["session@...", "profile@...", "session@b"]

dot = DotAccessor(profile={"a": [1, 2], "b": [1, 2]}, session={"b": 2}, event={})
t = DictTraverser(dot)
result = t.reshape(reshape_template=template)

print(result)

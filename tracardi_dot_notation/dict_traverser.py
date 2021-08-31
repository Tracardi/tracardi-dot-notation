from typing import List, Dict, Union

from dotty_dict import dotty
from tracardi_dot_notation.dot_accessor import DotAccessor


class DictTraverser:

    def __init__(self, dot: DotAccessor):
        self.dot = dot

    def traverse(self, value, key=None, path="root"):
        if isinstance(value, dict):
            for k, v in value.items():
                yield from self.traverse(v, k, path + "." + k)
        elif isinstance(value, list):
            for n, v in enumerate(value):
                k = str(n)
                yield from self.traverse(v, k, path + '.' + k)
        else:
            yield key, value, path

    def reshape(self, reshape_template: Union[Dict, List]):
        out_dot = dotty()
        for key, value, path in self.traverse(reshape_template):
            if key is not None:
                path = path[:-len(key)-1]
            value = self.dot[value]
            out_dot[f"{path}.{key}"] = value
        result = out_dot.to_dict()
        return result['root']

import re

from tracardi_dot_notation.dot_accessor import DotAccessor
from tracardi_dot_notation.utils.singleton import Singleton


class DotTemplate(metaclass=Singleton):

    def __init__(self, profile=None, session=None, payload=None, event=None, flow=None):
        self._regex = re.compile(r"\{{2}\s*((?:payload|profile|event|session|flow|memory)"
                                r"@[\[\]0-9a-zA-a_\-\.]+(?<![\.\[]))\s*\}{2}")
        self._dot = DotAccessor(profile, session, payload, event, flow)

    def render(self, template):
        return re.sub(self._regex, lambda x: str(self._dot[x.group(1)]), template)


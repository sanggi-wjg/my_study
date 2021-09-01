class Stack(object):
    _top_of_stack = 0
    _elements = []

    def size(self) -> int:
        return self._top_of_stack

    def push(self, element):
        self._top_of_stack += 1
        self._elements.append(element)

    def pop(self):
        if self._top_of_stack == 0:
            raise StackIsEmpty()

        element = self._elements.pop(self._top_of_stack)
        self._top_of_stack -= 1
        return element

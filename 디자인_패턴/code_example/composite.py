class LeafElement:

    def __init__(self, *args):
        self._position = args[0]

    def show_detail(self):
        print('\t', end = '')
        print(self._position)


class CompositeElement:

    def __init__(self, *args):
        self._position = args[0]
        self._children = []

    def add(self, child):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)

    def show_detail(self):
        print(self._position)
        for c in self._children:
            print('\t', end = '')
            c.show_detail()


def client_code():
    menu = CompositeElement("Menu")
    subMenu1 = CompositeElement("Sub Menu 1")
    subMenu2 = CompositeElement("Sub Menu 2")

    subMenuItem1 = LeafElement("Sub Menu Item 1")
    subMenuItem2 = LeafElement("Sub Menu Item 2")
    subMenuItem3 = LeafElement("Sub Menu Item 3")
    subMenuItem4 = LeafElement("Sub Menu Item 4")
    subMenu1.add(subMenuItem1)
    subMenu1.add(subMenuItem2)
    subMenu2.add(subMenuItem3)
    subMenu2.add(subMenuItem4)

    menu.add(subMenu1)
    menu.add(subMenu2)
    menu.show_detail()


"""
"""
client_code()

from typing import Generator, List


class Node:
    def __init__(self):
        self.children = []
        self.parent = None

    def add_child(self, node: 'Node'):
        self.children.append(node)
        node.parent = self

    def remove_child(self, node: 'Node'):
        self.children.remove(node)
        node.parent = None

    def should_apply_suffix(self) -> bool:
        if isinstance(self, NumberNode) and not self.suffix:
            return True
        else:
            return any([c.should_apply_suffix() for c in self.children])

    def get_bottom_num_node(self) -> List['NumberNode']:
        bottom_num_nodes = []
        for c in self.children:
            cn = c.get_bottom_num_node()
            bottom_num_nodes.extend(cn)
        if bottom_num_nodes:
            return bottom_num_nodes
        elif isinstance(self, NumberNode):
            return [self]
        else:
            return []

    def __str__(self):
        if len(self.children) > 1:
            return f"-({','.join([ str(c) for c in self.children])})"
        elif self.children:
            return '-' + str(self.children[0])
        else:
            return ''

    def __eq__(self, other):
        if other is None or type(self) != type(other): return False
        return self.__dict__ == other.__dict__


class NumberNode(Node):
    def __init__(self, number: int):
        super().__init__()
        self.number = number
        self.prefix = ''
        self.suffix = ''
        self.comparative_suffix = ''

    def __str__(self):
        return self.prefix + str(
            self.number) + self.suffix + self.comparative_suffix + super().__str__()

    def apply_suffix(self, suffix):
        if self.suffix == suffix:
            return
        elif not self.suffix:
            self.suffix = suffix
        else:
            for c in self.children:
                if isinstance(c, NumberNode) or isinstance(c, RangeNode):
                    c.apply_suffix(suffix)


class RangeNode(Node):
    def __init__(self, left: NumberNode, right: NumberNode):
        super().__init__()
        self.add_child(left)
        self.add_child(right)

    def __str__(self):
        if len(self.children) == 3:
            children = '-' + str(self.children[2])
        elif len(self.children) > 3:
            children = f"-({','.join([ str(c) for c in self.children[2:]])})"
        else:
            children = ''
        return "[" + str(self.children[0]) + '~' + str(self.children[1]) + ']' + children

    @property
    def suffix(self):
        return self.children[0].suffix

    def apply_suffix(self, suffix):
        if self.children:
            for c in self.children:
                if isinstance(c, NumberNode):
                    c.apply_suffix(suffix)


class StringNode(Node):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name + super().__str__()

    def apply_suffix(self, suffix):
        if self.children:
            for c in self.children:
                c.apply_suffix(suffix)

    @property
    def suffix(self):
        return ''


class ExcludeNode(Node):
    def __str__(self):
        return '除く' + super().__str__()


class SuffixNode(Node):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name + super().__str__()


class TopNode(Node):

    def __str__(self):
        if len(self.children) == 1:
            return str(self.children[0])
        else:
            return ','.join([str(c) for c in self.children])

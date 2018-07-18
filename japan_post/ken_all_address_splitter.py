from typing import Generator, Tuple

from japan_post import ken_all_choiki_yacc
from japan_post.ken_all_choiki_nodes import RangeNode, Node, ExcludeNode, NumberNode, StringNode


def split_choiki(choiki) -> Generator[Tuple[str, str], None, None]:
    node = ken_all_choiki_yacc.parse(choiki)
    for n0 in node.children:
        left = n0.name
        if not n0.children:
            yield left, ''
        else:
            for n1 in n0.children:
                for right in get_sub_choiki_name(n1):
                    yield left, right


def get_sub_choiki_name(node: Node) -> Generator[str, None, None]:
    if isinstance(node, RangeNode):
        left_node = ''.join([s for s in get_sub_choiki_name(node.children[0])])
        right_node = ''.join([s for s in get_sub_choiki_name(node.children[1])])
        s = left_node + '〜' + right_node
        if len(node.children) > 2:
            tail = '、'.join([n for c in node.children[2:] for n in get_sub_choiki_name(c)])
            yield s + '「' + tail + '」'
        else:
            yield s

    elif isinstance(node, ExcludeNode):
        s = '、'.join([n for c in node.children for n in get_sub_choiki_name(c)])
        yield node.left_parenthesis + s + node.right_parenthesis + 'を除く'
    elif isinstance(node, NumberNode):
        name = node.name
        if not node.children:
            yield name
        elif node.left_parenthesis:
            s = '、'.join([n for c in node.children for n in get_sub_choiki_name(c)])
            yield name + node.left_parenthesis + s + node.right_parenthesis
        else:
            for child in node.children:
                for s in get_sub_choiki_name(child):
                    if (isinstance(child, NumberNode) or isinstance(child, RangeNode)) and (
                            node.suffix == '番地' or not node.suffix):
                        yield name + '－' + s
                    else:
                        yield name + s
    else:
        # noinspection PyUnresolvedReferences
        name = node.name
        if not node.children:
            yield name
        elif node.left_parenthesis:
            s = '、'.join([n for c in node.children for n in get_sub_choiki_name(c)])
            yield name + node.left_parenthesis + s + node.right_parenthesis
        else:
            yield from [name + n for c in node.children for n in get_sub_choiki_name(c)]

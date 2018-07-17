from typing import List

import ply.yacc as yacc

from japan_post.ken_all_choiki_lex import tokens, lexer
from japan_post.ken_all_choiki_nodes import RangeNode, NumberNode, StringNode, ExcludeNode, Node, \
    SuffixNode, TopNode


def p_choiki(p):
    """
    choiki : node_list
    """
    p[0] = TopNode()
    for n in p[1]:
        p[0].add_child(n)


def p_node_list_children(p):
    """
    node : node L_PAREN node_list R_PAREN
    """
    p[0] = p[1]
    ns = arrange_node_list(p[3])
    for n in ns:
        p[0].add_child(n)


def p_exlude_node(p):
    """
    node : node L_PAREN node_list EXCLUDE R_PAREN
    """
    p[0] = p[1]
    exclude_node = ExcludeNode()
    ns = arrange_node_list(p[3])
    for n in ns:
        exclude_node.add_child(n)
    p[0].add_child(exclude_node)


def p_exlude_node2(p):
    """
    node : node L_PAREN node_list R_PAREN EXCLUDE
    """
    p[0] = p[1]
    exclude_node = ExcludeNode()
    ns = arrange_node_list(p[3])
    for n in ns:
        exclude_node.add_child(n)
    p[0].add_child(exclude_node)


def p_node_list(p):
    """
    node_list : node COMMA node_list
            | node
    """
    if len(p) == 2:
        p[0] = [p[1]]
    elif p[2] == '・' and p[1].children:
        p[1].add_child(p[3][0])
        p[3].remove(p[3][0])
        ls = [p[1]]
        for n in p[3]:
            ls.append(n)
        apply_suffix_to_nodes(p[1].children)
        p[0] = ls
    else:
        p[0] = p[3]
        p[0].insert(0, p[1])


def p_only_wave_dash(p):
    """
    node : node WAVE_DASH
    """
    p[0] = p[1]
    leaf = list(p[0].get_leaf())[-1]
    leaf.comparative_suffix = '以上'


def p_bullet_list_in_node_list(p):
    """
    node_list : bullet_list COMMA node_list
            | bullet_list
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]
        p[0].extend(p[3])


def p_bullet_list_children(p):
    """
    node : node bullet_list
    """
    p[0] = p[1]
    ns = arrange_node_list(p[2])
    for n in ns:
        p[0].add_child(n)


def p_paren_bullet_list(p):
    """
    node : node L_PAREN bullet_list R_PAREN
    """
    p[0] = p[1]
    ns = arrange_node_list(p[3])
    for n in ns:
        p[0].add_child(n)


def p_bullet_list(p):
    """
    bullet_list : node BULLET bullet_list
                | node
    """
    if len(p) == 2:
        p[0] = [p[1]]
    elif (isinstance(p[1], NumberNode) or isinstance(p[1], StringNode)) and p[1].children:
        for c in p[3]:
            p[1].add_child(c)
        p[0] = [p[1]]
    else:
        p[0] = p[3]
        p[0].insert(0, p[1])


def p_then(p):
    """
    num_node : num_node THEN num_node
    """
    p[0] = p[1]
    p[0].add_child(p[3])
    if not p[0].suffix and p[3].suffix:
        p[0].suffix = p[3].suffix
        p[3].suffix = ''


def p_range_node(p):
    """
    range_node : node WAVE_DASH node
    """
    p1 = p[1]
    p3 = p[3]

    def is_equal_ndoes(n1, n2):
        if type(n1) != type(n2):
            return False
        elif isinstance(n1, StringNode):
            return n1.name == n2.name
        elif isinstance(n1, NumberNode):
            return n1.number == n2.number
        else:
            return False

    if is_equal_ndoes(p1, p3) and p1.children and p3.children:
        c1 = p1.children[0]
        p1.remove_child(c1)
        c3 = p3.children[0]
        p3.remove_child(c3)
        c1.suffix = c3.suffix
        range_node = RangeNode(c1, c3)
        for c in p3.children:
            range_node.add_child(c)
        p1.add_child(range_node)
        p[0] = p1
    elif not p1.children and p3.children:
        p3_children = p3.children.copy()
        range_node = RangeNode(p1, p3)
        p1.suffix = p3.suffix
        for c in p3_children:
            p3.remove_child(c)
            range_node.add_child(c)
        p[0] = range_node
    elif isinstance(p1, StringNode) and p1.children and not p3.children:
        leaf = list(p1.get_leaf())[-1]
        parent = leaf.parent
        parent.remove_child(leaf)
        leaf.suffix = p3.suffix
        range_node = RangeNode(leaf, p3)
        parent.add_child(range_node)
        p[0] = p[1]
    else:
        p1.suffix = p3.suffix
        p[0] = RangeNode(p1, p3)


def p_node_succ(p):
    """
    node : node node
    """
    p[0] = p[1]
    p[0].add_child(p[2])


def p_num_node_hyphen(p):
    """
    num_node : num_node HYPHEN num_node
    """
    p[0] = p[1]
    p[0].add_child(p[3])
    p[0].suffix = p[3].suffix
    p[3].suffix = ''


def p_string_node_hyphen(p):
    """
    string_node : string_node HYPHEN num_node
    """

    p[0] = p[1]
    c = list(p[1].get_leaf())[0]
    c.add_child(p[3])
    c.suffix = p[3].suffix
    p[3].suffix = ''


def p_node(p):
    """
    node : range_node
     | num_node
     | string_node
     | suffix_node
    """
    p[0] = p[1]


def p_num_node_prefix(p):
    """
    num_node : PREFIX NUMBER
            | PREFIX NUMBER SUFFIX
            | PREFIX NUMBER SUFFIX COMPARATIVE_SUFFIX
    """
    p[0] = NumberNode(p[2])
    p[0].prefix = p[1]
    if len(p) == 4:
        p[0].suffix = p[3]
    if len(p) == 5:
        p[0].comparative_suffix = p[4]


def p_num_node_suffix(p):
    """
    num_node : NUMBER SUFFIX
            |  NUMBER SUFFIX COMPARATIVE_SUFFIX
    """
    p[0] = NumberNode(p[1])
    p[0].suffix = p[2]
    if len(p) == 4:
        p[0].comparative_suffix = p[3]


def p_num_node(p):
    """
    num_node : NUMBER
            | NUMBER COMPARATIVE_SUFFIX
            | PREFIX NUMBER COMPARATIVE_SUFFIX
    """
    p[0] = NumberNode(p[1])
    if len(p) == 3:
        p[0].comparative_suffix = p[2]
    elif len(p) == 4:
        p[0].prefix = p[1]
        p[0].comparative_suffix = p[3]


def p_string_and_number_node(p):
    """
    string_node : ID NUMBER
                | ID NUMBER SUFFIX
    """
    p1 = StringNode(p[1])
    p2 = NumberNode(p[2])
    if len(p) == 4:
        p2.suffix = p[3]
    p1.add_child(p2)
    p[0] = p1


def p_string_node(p):
    """
    string_node : ID
    """
    p[0] = StringNode(p[1])


def p_dot_concat_string(p):
    """
    string_node : string_node DOT ID
    """
    p[0] = p[1]
    p[0].name = p[0].name + p[2] + p[3]


def p_floow_string(p):
    """
    string_node : FLOOR BULLET FLOOR
    """
    p[0] = StringNode(p[1] + p[2] + p[3])


def p_only_suffix_node(p):
    """
    suffix_node : SUFFIX
    """
    p[0] = SuffixNode(p[1])


def p_error(p):
    raise ValueError(p)


def arrange_node_list(nodes: List[Node]) -> List[Node]:
    apply_suffix_to_nodes(nodes)
    return replace_node_list_to_same_level_suffix(nodes)


def apply_suffix_to_nodes(nodes: List[Node]):
    nodes_to_apply = []
    for node in nodes:
        if isinstance(node, NumberNode) or isinstance(node, RangeNode):
            should_apply = node.should_apply_suffix()
            if node.suffix and nodes_to_apply:
                for n in nodes_to_apply:
                    n.apply_suffix(node.suffix)
                nodes_to_apply = []
            elif should_apply:
                nodes_to_apply.append(node)
        elif isinstance(node, StringNode) and node.should_apply_suffix():
            nodes_to_apply.append(node)
        else:
            nodes_to_apply = []


def append_same_level_suffix(n0, n1) -> Node:
    if n0.suffix == n1.suffix:
        if n0.parent != n1.parent:
            n0.parent.add_child(n1)
        return n0.parent
    else:
        return append_same_level_suffix(n0.children[0], n1)


def replace_node_list_to_same_level_suffix(nodes: List[Node]) -> List[Node]:
    result_nodes = []
    for node in nodes:
        if not result_nodes:
            result_nodes.append(node)
        else:
            last_node = result_nodes[-1]
            if has_suffix(last_node) and has_suffix(node):
                # noinspection PyUnresolvedReferences
                if last_node.suffix == node.suffix:
                    result_nodes.append(node)
                else:
                    # noinspection PyTypeChecker
                    append_same_level_suffix(last_node, node)
            elif isinstance(last_node, StringNode) and last_node.children and has_suffix(node):
                # noinspection PyTypeChecker
                append_same_level_suffix(last_node, node)
            else:
                result_nodes.append(node)
    return result_nodes


def has_suffix(node: Node):
    return isinstance(node, NumberNode) or isinstance(node, RangeNode)


parser = yacc.yacc()


def parse_choiki(s):
    s = s.replace('種市第', '種市 第')
    s = s.replace('以上', ' 以上')
    s = s.replace('以下', ' 以下')
    s = s.replace('以外', ' 以外')
    s = s.replace('を除く', ' を除く')
    s = s.replace('番地のみ', '番地')
    s = s.replace('番地の', '番地 の')
    lexer.parenthesis_depth = 0
    return parser.parse(s, lexer=lexer)


if __name__ == '__main__':
    ls = [
        '１丁目',
        '２丁目６５１',
        '前川原２３２',
        '前川原２３２～２４４',
        '第２地割「７０～１３６」～第４地割「３～１１」',
        '大江（２丁目６５１、６６２、６６８番地、３丁目１０３、１１８、２１０、２５４、２６７、３７２、４４４、４６９番地）',
        '葛巻（第４０地割「５７番地１２５、１７６を除く」～第４５地割）',
    ]
    for s in ls:
        lexer.parenthesis_depth = 0
        ret = parser.parse(s, lexer=lexer)
        print(ret)

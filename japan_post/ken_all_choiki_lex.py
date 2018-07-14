import ply.lex as lex

reserved = {
    '以上': 'COMPARATIVE_SUFFIX',
    '以下': 'COMPARATIVE_SUFFIX',
    'を除く': 'EXCLUDE',
    '以外': 'EXCLUDE',
    '丁目': 'SUFFIX',
    '番地': 'SUFFIX',
    '番': 'SUFFIX',
    '号': 'SUFFIX',
    '地割': 'SUFFIX',
    'の': 'HYPHEN',
    '第': 'PREFIX',
    '地階': 'FLOOR',
    '階層不明': 'FLOOR',
}

tokens = (
    'EXCLUDE',
    'ID',
    'NUMBER',
    'L_PAREN',
    'R_PAREN',
    'WAVE_DASH',
    'COMMA',
    'DOT',
    'HYPHEN',
    'COMPARATIVE_SUFFIX',
    'SUFFIX',
    'PREFIX',
    'FLOOR'
)

parenthesis_depth = 0

t_WAVE_DASH = r'～'
t_COMMA = r'、'
t_HYPHEN = r'－'
t_ignore = ' '


# noinspection PySingleQuotedDocstring
def t_L_PAREN(t):
    r'（|「|〔'
    global parenthesis_depth
    parenthesis_depth += 1
    return t


# noinspection PySingleQuotedDocstring
def t_R_PAREN(t):
    r'）|」|〕'
    global parenthesis_depth
    parenthesis_depth -= 1
    return t


# noinspection PySingleQuotedDocstring
def t_DOT(t):
    r'・'
    global parenthesis_depth
    if parenthesis_depth > 0:
        t.type = 'COMMA'
        return t
    else:
        return t


# noinspection PySingleQuotedDocstring
def t_ID(t):
    r'[一-龥ぁ-んァ-ンＡ-Ｚａ-ｚー]+'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# noinspection PySingleQuotedDocstring
def t_NUMBER(t):
    r'[０１２３４５６７８９]+'
    t.value = int(t.value)
    return t


def t_error(t):
    t.skip(1)


lexer = lex.lex()
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
    'の': 'THEN',
    '第': 'PREFIX',
    '地階': 'FLOOR',
    '階層不明': 'FLOOR',
    '線': 'SUFFIX',
    '区': 'SUFFIX',
    '北': 'DIRECTION',
    '南': 'DIRECTION',
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
    'FLOOR',
    'THEN',
    'BULLET',
    'DIRECTION',
    'ALL',
)

t_WAVE_DASH = r'～'
t_COMMA = r'、'
t_HYPHEN = r'－'
t_ignore = ' '


# noinspection PySingleQuotedDocstring
def t_L_PAREN(t):
    r'（|「|〔'
    global parenthesis_depth
    t.lexer.parenthesis_depth += 1
    return t


# noinspection PySingleQuotedDocstring
def t_R_PAREN(t):
    r'）|」|〕'
    t.lexer.parenthesis_depth -= 1
    return t


# noinspection PySingleQuotedDocstring
def t_DOT(t):
    r'・'
    if t.lexer.parenthesis_depth > 0:
        t.type = 'BULLET'
        return t
    else:
        return t


# noinspection PySingleQuotedDocstring
def t_ID(t):
    r'[一-龥ぁ-んァ-ンヴＡ-Ｚａ-ｚー々ヶ○]+'
    if 'の次に番地がくる場合' in t.value:
        t.type = 'SUFFIX'
    elif '一円' in t.value:
        t.type = 'ALL'
    else:
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

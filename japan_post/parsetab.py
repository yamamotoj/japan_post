
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BULLET COMMA COMPARATIVE_SUFFIX DIRECTION DOT EXCLUDE FLOOR HYPHEN ID L_PAREN NUMBER PREFIX R_PAREN SUFFIX THEN WAVE_DASH\n    choiki : node_list\n    \n    node : node L_PAREN node_list R_PAREN\n    \n    node : node L_PAREN node_list EXCLUDE R_PAREN\n    \n    node : node L_PAREN node_list R_PAREN EXCLUDE\n    \n    node_list : node COMMA node_list\n            | node\n    \n    node : node WAVE_DASH\n    \n    node_list : bullet_list COMMA node_list\n            | bullet_list\n    \n    node : node bullet_list\n    \n    node : node L_PAREN bullet_list R_PAREN\n    \n    bullet_list : node BULLET bullet_list\n                | node\n    \n    node : node THEN num_node\n    \n    range_node : node WAVE_DASH node\n    \n    node : node node\n    \n    num_node : num_node HYPHEN num_node\n    \n    string_node : string_node HYPHEN num_node\n    \n    node : range_node\n     | num_node\n     | string_node\n     | suffix_node\n    \n    node : node DIRECTION\n    \n    num_node : PREFIX NUMBER\n            | PREFIX NUMBER SUFFIX\n            | PREFIX NUMBER SUFFIX COMPARATIVE_SUFFIX\n    \n    num_node : NUMBER SUFFIX\n            |  NUMBER SUFFIX COMPARATIVE_SUFFIX\n    \n    num_node : NUMBER\n            | NUMBER COMPARATIVE_SUFFIX\n            | PREFIX NUMBER COMPARATIVE_SUFFIX\n    \n    string_node : ID NUMBER\n                | ID NUMBER SUFFIX\n    \n    string_node : ID\n    \n    string_node : string_node DOT ID\n    \n    string_node : FLOOR BULLET FLOOR\n    \n    suffix_node : SUFFIX\n    '
    
_lr_action_items = {'PREFIX':([0,3,5,6,7,8,10,11,12,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[9,9,-20,-19,-21,-22,-29,-37,-34,9,9,9,9,-10,9,-23,9,9,9,9,-24,-27,-30,-32,9,9,-14,9,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'NUMBER':([0,3,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[10,10,-20,-19,-21,-22,26,-29,-37,29,10,10,10,10,-10,10,-23,10,10,10,10,-24,-27,-30,-32,10,10,-14,10,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'ID':([0,3,5,6,7,8,10,11,12,14,15,16,17,18,20,21,22,25,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[12,12,-20,-19,-21,-22,-29,-37,-34,12,12,12,12,-10,-23,12,12,42,-24,-27,-30,-32,12,12,-14,12,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'FLOOR':([0,3,5,6,7,8,10,11,12,14,15,16,17,18,20,21,22,26,27,28,29,30,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[13,13,-20,-19,-21,-22,-29,-37,-34,13,13,13,13,-10,-23,13,13,-24,-27,-30,-32,47,13,13,-14,13,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'SUFFIX':([0,3,5,6,7,8,10,11,12,14,15,16,17,18,20,21,22,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[11,11,-20,-19,-21,-22,27,-37,-34,11,11,11,11,-10,-23,11,11,43,-27,-30,46,11,11,-14,11,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'$end':([1,2,3,4,5,6,7,8,10,11,12,14,17,18,20,26,27,28,29,31,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,],[0,-1,-6,-9,-20,-19,-21,-22,-29,-37,-34,-13,-7,-10,-23,-24,-27,-30,-32,-5,-15,-14,-13,-12,-8,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'COMMA':([3,4,5,6,7,8,10,11,12,14,17,18,20,26,27,28,29,32,34,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[15,22,-20,-19,-21,-22,-29,-37,-34,-13,-7,-10,-23,-24,-27,-30,-32,15,22,-15,-14,-13,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'R_PAREN':([3,4,5,6,7,8,10,11,12,14,17,18,20,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-6,-9,-20,-19,-21,-22,-29,-37,-34,-13,-7,-10,-23,-24,-27,-30,-32,-5,-6,48,50,-15,-14,-13,-12,-8,-17,-18,-35,-25,-31,-28,-33,-36,-2,53,-11,-26,-4,-3,]),'EXCLUDE':([3,4,5,6,7,8,10,11,12,14,17,18,20,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,],[-6,-9,-20,-19,-21,-22,-29,-37,-34,-13,-7,-10,-23,-24,-27,-30,-32,-5,-6,49,-9,-15,-14,-13,-12,-8,-17,-18,-35,-25,-31,-28,-33,-36,52,-11,-26,-4,-3,]),'L_PAREN':([3,5,6,7,8,10,11,12,14,17,18,20,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[16,-20,-19,-21,-22,-29,-37,-34,16,-7,-10,-23,-24,-27,-30,-32,16,16,-14,16,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'WAVE_DASH':([3,5,6,7,8,10,11,12,14,17,18,20,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[17,-20,-19,-21,-22,-29,-37,-34,17,-7,-10,-23,-24,-27,-30,-32,17,17,-14,17,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'THEN':([3,5,6,7,8,10,11,12,14,17,18,20,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[19,-20,-19,-21,-22,-29,-37,-34,19,-7,-10,-23,-24,-27,-30,-32,19,19,-14,19,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'DIRECTION':([3,5,6,7,8,10,11,12,14,17,18,20,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[20,-20,-19,-21,-22,-29,-37,-34,20,-7,-10,-23,-24,-27,-30,-32,20,20,-14,20,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'BULLET':([3,5,6,7,8,10,11,12,13,14,17,18,20,26,27,28,29,32,35,36,37,38,40,41,42,43,44,45,46,47,48,50,51,52,53,],[21,-20,-19,-21,-22,-29,-37,-34,30,21,-7,-10,-23,-24,-27,-30,-32,21,-15,-14,21,-12,-17,-18,-35,-25,-31,-28,-33,-36,-2,-11,-26,-4,-3,]),'HYPHEN':([5,7,10,12,26,27,28,29,36,40,41,42,43,44,45,46,47,51,],[23,24,-29,-34,-24,-27,-30,-32,23,23,23,-35,-25,-31,-28,-33,-36,-26,]),'DOT':([7,10,12,26,27,28,29,40,41,42,43,44,45,46,47,51,],[25,-29,-34,-24,-27,-30,-32,-17,-18,-35,-25,-31,-28,-33,-36,-26,]),'COMPARATIVE_SUFFIX':([10,26,27,43,],[28,44,45,51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'choiki':([0,],[1,]),'node_list':([0,15,16,22,],[2,31,33,39,]),'node':([0,3,14,15,16,17,21,22,32,35,37,],[3,14,14,3,32,35,37,3,14,14,14,]),'bullet_list':([0,3,14,15,16,21,22,32,35,37,],[4,18,18,4,34,38,4,18,18,18,]),'num_node':([0,3,14,15,16,17,19,21,22,23,24,32,35,37,],[5,5,5,5,5,5,36,5,5,40,41,5,5,5,]),'range_node':([0,3,14,15,16,17,21,22,32,35,37,],[6,6,6,6,6,6,6,6,6,6,6,]),'string_node':([0,3,14,15,16,17,21,22,32,35,37,],[7,7,7,7,7,7,7,7,7,7,7,]),'suffix_node':([0,3,14,15,16,17,21,22,32,35,37,],[8,8,8,8,8,8,8,8,8,8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> choiki","S'",1,None,None,None),
  ('choiki -> node_list','choiki',1,'p_choiki','ken_all_choiki_yacc.py',12),
  ('node -> node L_PAREN node_list R_PAREN','node',4,'p_node_list_children','ken_all_choiki_yacc.py',21),
  ('node -> node L_PAREN node_list EXCLUDE R_PAREN','node',5,'p_exlude_node','ken_all_choiki_yacc.py',31),
  ('node -> node L_PAREN node_list R_PAREN EXCLUDE','node',5,'p_exlude_node2','ken_all_choiki_yacc.py',43),
  ('node_list -> node COMMA node_list','node_list',3,'p_node_list','ken_all_choiki_yacc.py',55),
  ('node_list -> node','node_list',1,'p_node_list','ken_all_choiki_yacc.py',56),
  ('node -> node WAVE_DASH','node',2,'p_only_wave_dash','ken_all_choiki_yacc.py',75),
  ('node_list -> bullet_list COMMA node_list','node_list',3,'p_bullet_list_in_node_list','ken_all_choiki_yacc.py',84),
  ('node_list -> bullet_list','node_list',1,'p_bullet_list_in_node_list','ken_all_choiki_yacc.py',85),
  ('node -> node bullet_list','node',2,'p_bullet_list_children','ken_all_choiki_yacc.py',96),
  ('node -> node L_PAREN bullet_list R_PAREN','node',4,'p_paren_bullet_list','ken_all_choiki_yacc.py',106),
  ('bullet_list -> node BULLET bullet_list','bullet_list',3,'p_bullet_list','ken_all_choiki_yacc.py',116),
  ('bullet_list -> node','bullet_list',1,'p_bullet_list','ken_all_choiki_yacc.py',117),
  ('node -> node THEN num_node','node',3,'p_then','ken_all_choiki_yacc.py',132),
  ('range_node -> node WAVE_DASH node','range_node',3,'p_range_node','ken_all_choiki_yacc.py',144),
  ('node -> node node','node',2,'p_node_succ','ken_all_choiki_yacc.py',194),
  ('num_node -> num_node HYPHEN num_node','num_node',3,'p_num_node_hyphen','ken_all_choiki_yacc.py',202),
  ('string_node -> string_node HYPHEN num_node','string_node',3,'p_string_node_hyphen','ken_all_choiki_yacc.py',212),
  ('node -> range_node','node',1,'p_node','ken_all_choiki_yacc.py',224),
  ('node -> num_node','node',1,'p_node','ken_all_choiki_yacc.py',225),
  ('node -> string_node','node',1,'p_node','ken_all_choiki_yacc.py',226),
  ('node -> suffix_node','node',1,'p_node','ken_all_choiki_yacc.py',227),
  ('node -> node DIRECTION','node',2,'p_num_node_direction','ken_all_choiki_yacc.py',234),
  ('num_node -> PREFIX NUMBER','num_node',2,'p_num_node_prefix','ken_all_choiki_yacc.py',244),
  ('num_node -> PREFIX NUMBER SUFFIX','num_node',3,'p_num_node_prefix','ken_all_choiki_yacc.py',245),
  ('num_node -> PREFIX NUMBER SUFFIX COMPARATIVE_SUFFIX','num_node',4,'p_num_node_prefix','ken_all_choiki_yacc.py',246),
  ('num_node -> NUMBER SUFFIX','num_node',2,'p_num_node_suffix','ken_all_choiki_yacc.py',258),
  ('num_node -> NUMBER SUFFIX COMPARATIVE_SUFFIX','num_node',3,'p_num_node_suffix','ken_all_choiki_yacc.py',259),
  ('num_node -> NUMBER','num_node',1,'p_num_node','ken_all_choiki_yacc.py',269),
  ('num_node -> NUMBER COMPARATIVE_SUFFIX','num_node',2,'p_num_node','ken_all_choiki_yacc.py',270),
  ('num_node -> PREFIX NUMBER COMPARATIVE_SUFFIX','num_node',3,'p_num_node','ken_all_choiki_yacc.py',271),
  ('string_node -> ID NUMBER','string_node',2,'p_string_and_number_node','ken_all_choiki_yacc.py',283),
  ('string_node -> ID NUMBER SUFFIX','string_node',3,'p_string_and_number_node','ken_all_choiki_yacc.py',284),
  ('string_node -> ID','string_node',1,'p_string_node','ken_all_choiki_yacc.py',296),
  ('string_node -> string_node DOT ID','string_node',3,'p_dot_concat_string','ken_all_choiki_yacc.py',303),
  ('string_node -> FLOOR BULLET FLOOR','string_node',3,'p_floow_string','ken_all_choiki_yacc.py',311),
  ('suffix_node -> SUFFIX','suffix_node',1,'p_only_suffix_node','ken_all_choiki_yacc.py',318),
]

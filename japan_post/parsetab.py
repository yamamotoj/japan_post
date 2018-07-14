
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA COMPARATIVE_SUFFIX DOT EXCLUDE FLOOR HYPHEN ID L_PAREN NUMBER PREFIX R_PAREN SUFFIX THEN WAVE_DASH\n    choiki : node\n    \n    node : node L_PAREN node_list R_PAREN\n    \n    node : node L_PAREN node_list EXCLUDE R_PAREN\n    \n    node : node L_PAREN node_list R_PAREN EXCLUDE\n    \n    node_list : node COMMA node_list\n            | node\n    \n    node : node THEN node\n    \n    range_node : node WAVE_DASH node\n    \n    node : node node\n    \n    num_node : NUMBER HYPHEN NUMBER\n    \n    node : range_node\n     | num_node\n     | string_node\n    \n    num_node : PREFIX num_node\n    \n    num_node : num_node SUFFIX\n    \n    num_node : num_node COMPARATIVE_SUFFIX\n    \n    num_node : NUMBER\n    \n    string_node : ID\n    \n    string_node : ID DOT ID\n    \n    string_node : FLOOR COMMA FLOOR\n    '
    
_lr_action_items = {'NUMBER':([0,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,20,22,23,24,25,26,27,28,31,32,],[6,6,-11,-12,-13,-17,6,-18,6,6,6,6,-15,-16,24,-14,6,6,6,-10,-19,-20,6,-2,-4,-3,]),'PREFIX':([0,2,3,4,5,6,7,8,10,11,12,13,14,15,17,20,22,23,24,25,26,27,28,31,32,],[7,7,-11,-12,-13,-17,7,-18,7,7,7,7,-15,-16,-14,7,7,7,-10,-19,-20,7,-2,-4,-3,]),'ID':([0,2,3,4,5,6,8,10,11,12,13,14,15,17,18,20,22,23,24,25,26,27,28,31,32,],[8,8,-11,-12,-13,-17,-18,8,8,8,8,-15,-16,-14,25,8,8,8,-10,-19,-20,8,-2,-4,-3,]),'FLOOR':([0,2,3,4,5,6,8,10,11,12,13,14,15,17,19,20,22,23,24,25,26,27,28,31,32,],[9,9,-11,-12,-13,-17,-18,9,9,9,9,-15,-16,-14,26,9,9,9,-10,-19,-20,9,-2,-4,-3,]),'$end':([1,2,3,4,5,6,8,10,14,15,17,22,23,24,25,26,28,31,32,],[0,-1,-11,-12,-13,-17,-18,-9,-15,-16,-14,-7,-8,-10,-19,-20,-2,-4,-3,]),'L_PAREN':([2,3,4,5,6,8,10,14,15,17,20,22,23,24,25,26,28,31,32,],[11,-11,-12,-13,-17,-18,11,-15,-16,-14,11,11,11,-10,-19,-20,-2,-4,-3,]),'THEN':([2,3,4,5,6,8,10,14,15,17,20,22,23,24,25,26,28,31,32,],[12,-11,-12,-13,-17,-18,12,-15,-16,-14,12,12,12,-10,-19,-20,-2,-4,-3,]),'WAVE_DASH':([2,3,4,5,6,8,10,14,15,17,20,22,23,24,25,26,28,31,32,],[13,-11,-12,-13,-17,-18,13,-15,-16,-14,13,13,13,-10,-19,-20,-2,-4,-3,]),'COMMA':([3,4,5,6,8,9,10,14,15,17,20,22,23,24,25,26,28,31,32,],[-11,-12,-13,-17,-18,19,-9,-15,-16,-14,27,-7,-8,-10,-19,-20,-2,-4,-3,]),'R_PAREN':([3,4,5,6,8,10,14,15,17,20,21,22,23,24,25,26,28,29,30,31,32,],[-11,-12,-13,-17,-18,-9,-15,-16,-14,-6,28,-7,-8,-10,-19,-20,-2,32,-5,-4,-3,]),'EXCLUDE':([3,4,5,6,8,10,14,15,17,20,21,22,23,24,25,26,28,30,31,32,],[-11,-12,-13,-17,-18,-9,-15,-16,-14,-6,29,-7,-8,-10,-19,-20,31,-5,-4,-3,]),'SUFFIX':([4,6,14,15,17,24,],[14,-17,-15,-16,14,-10,]),'COMPARATIVE_SUFFIX':([4,6,14,15,17,24,],[15,-17,-15,-16,15,-10,]),'HYPHEN':([6,],[16,]),'DOT':([8,],[18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'choiki':([0,],[1,]),'node':([0,2,10,11,12,13,20,22,23,27,],[2,10,10,20,22,23,10,10,10,20,]),'range_node':([0,2,10,11,12,13,20,22,23,27,],[3,3,3,3,3,3,3,3,3,3,]),'num_node':([0,2,7,10,11,12,13,20,22,23,27,],[4,4,17,4,4,4,4,4,4,4,4,]),'string_node':([0,2,10,11,12,13,20,22,23,27,],[5,5,5,5,5,5,5,5,5,5,]),'node_list':([11,27,],[21,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> choiki","S'",1,None,None,None),
  ('choiki -> node','choiki',1,'p_choiki','ken_all_choiki_yacc.py',11),
  ('node -> node L_PAREN node_list R_PAREN','node',4,'p_node_list_children','ken_all_choiki_yacc.py',18),
  ('node -> node L_PAREN node_list EXCLUDE R_PAREN','node',5,'p_exlude_node','ken_all_choiki_yacc.py',28),
  ('node -> node L_PAREN node_list R_PAREN EXCLUDE','node',5,'p_exlude_node2','ken_all_choiki_yacc.py',40),
  ('node_list -> node COMMA node_list','node_list',3,'p_node_list','ken_all_choiki_yacc.py',52),
  ('node_list -> node','node_list',1,'p_node_list','ken_all_choiki_yacc.py',53),
  ('node -> node THEN node','node',3,'p_then','ken_all_choiki_yacc.py',71),
  ('range_node -> node WAVE_DASH node','range_node',3,'p_range_node','ken_all_choiki_yacc.py',79),
  ('node -> node node','node',2,'p_node_succ','ken_all_choiki_yacc.py',109),
  ('num_node -> NUMBER HYPHEN NUMBER','num_node',3,'p_node_hyphen','ken_all_choiki_yacc.py',117),
  ('node -> range_node','node',1,'p_node','ken_all_choiki_yacc.py',125),
  ('node -> num_node','node',1,'p_node','ken_all_choiki_yacc.py',126),
  ('node -> string_node','node',1,'p_node','ken_all_choiki_yacc.py',127),
  ('num_node -> PREFIX num_node','num_node',2,'p_num_node_prefix','ken_all_choiki_yacc.py',134),
  ('num_node -> num_node SUFFIX','num_node',2,'p_num_node_suffix','ken_all_choiki_yacc.py',142),
  ('num_node -> num_node COMPARATIVE_SUFFIX','num_node',2,'p_num_node_comparative_suffix','ken_all_choiki_yacc.py',150),
  ('num_node -> NUMBER','num_node',1,'p_num_node','ken_all_choiki_yacc.py',158),
  ('string_node -> ID','string_node',1,'p_string_node','ken_all_choiki_yacc.py',165),
  ('string_node -> ID DOT ID','string_node',3,'p_dot_concat_string','ken_all_choiki_yacc.py',172),
  ('string_node -> FLOOR COMMA FLOOR','string_node',3,'p_floow_string','ken_all_choiki_yacc.py',179),
]

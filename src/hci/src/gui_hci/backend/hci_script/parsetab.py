
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSANDORBITWISELSBITWISERSleftMULDIVMODBITWISEANDBITWISEORBITWISEXORleftPOWERBITWISENOTrightUMINUSNOTADD_DEV AND ASSIGN BITWISEAND BITWISELS BITWISENOT BITWISEOR BITWISERS BITWISEXOR CMD DEV DIV ELSE EQUAL FALSE FLOAT FOR GT GTE ID IF INT LPAREN LT LTE MINUS MOD MUL NEWLINE NOT NOTEQUAL OR PLUS POWER PRINT RETASSIGN RPAREN SEP STEP STEPIN STEPOUT STR TO TRUE WAIT WHILEprogram : program statement\n               | statementstatement : command NEWLINE\n                 | DEV command NEWLINEstatement : NEWLINEstatement : error NEWLINEcommand : FOR ID ASSIGN expr TO expr optstep optlvlinccommand : FOR ID ASSIGN error TO expr optstep optlvlinccommand : FOR ID ASSIGN expr TO error optstep optlvlinccommand : FOR ID ASSIGN expr TO expr STEP errorcommand : IF boolexpr optlvlinc\n               | IF expr optlvlinccommand : IF error optlvlinccommand : optlvldec ELSE IF boolexpr optlvlinccommand : optlvldec ELSE IF error optlvlinccommand : optlvldec ELSE optlvlinccommand : WHILE boolexpr optlvlinc\n               | WHILE bool optlvlinccommand : WHILE error optlvlinccommand : ADD_DEV ID exprcommand : ADD_DEV ID errorcommand : CMD\n               | CMD RETASSIGN ID\n               | CMD paramlist\n               | CMD paramlist RETASSIGN IDcommand : CMD errorcommand : WAIT exprcommand : WAIT errorcommand : ID ASSIGN exprcommand : ID ASSIGN errorcommand : STEPIN\n               | STEPOUTcommand : PRINT exproptstep : STEP expr\n               | emptyoptlvlinc : STEPIN\n                 | emptyoptlvldec : STEPOUT\n                 | emptyboolexpr : relexpr\n                | boolexpr AND boolexpr\n                | boolexpr OR boolexpr\n                | NOT boolexprrelexpr : expr LT expr\n               | expr LTE expr\n               | expr GT expr\n               | expr GTE expr\n               | expr EQUAL expr\n               | expr NOTEQUAL exprexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr MUL expr\n            | expr DIV expr\n            | expr MOD expr\n            | expr POWER exprexpr : expr BITWISEAND expr\n            | expr BITWISEOR expr\n            | expr BITWISEXOR expr\n            | expr BITWISELS INT\n            | expr BITWISERS INT\n            | BITWISENOT exprexpr : INT\n            | FLOATexpr : STRexpr : IDexpr : boolexpr : LPAREN expr RPARENexpr : MINUS expr %prec UMINUSbool : TRUE\n            | FALSEparamlist : paramlist SEP param\n                 | paramparam : expr\n             | boolexprempty : '
    
_lr_action_items = {'DEV':([0,1,2,4,19,20,22,55,],[5,5,-2,-5,-1,-3,-6,-4,]),'NEWLINE':([0,1,2,3,4,6,13,15,16,19,20,21,22,25,26,27,28,31,33,34,35,36,38,39,40,41,42,43,47,48,49,50,51,52,53,54,55,57,58,59,62,63,64,82,83,84,85,88,89,90,91,92,93,94,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,125,126,127,128,129,130,132,133,135,136,137,138,139,140,],[4,4,-2,20,-5,22,-22,-31,-32,-1,-3,55,-6,-75,-75,-75,-40,-62,-63,-64,-65,-66,-69,-70,-75,-75,-75,-75,-24,-26,-72,-73,-74,-27,-28,-33,-4,-29,-30,-11,-36,-37,-12,-13,-43,-68,-61,-16,-17,-18,-19,-20,-21,-23,-41,-42,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-44,-45,-46,-47,-48,-49,-67,-75,-75,-25,-71,-14,-15,-75,-75,-75,-75,-35,-75,-75,-7,-34,-10,-9,-8,]),'error':([0,1,2,4,9,11,13,14,19,20,22,24,45,55,56,87,123,131,],[6,6,-2,-5,27,43,48,53,-1,-3,-6,58,93,-4,98,120,128,138,]),'FOR':([0,1,2,4,5,19,20,22,55,],[7,7,-2,-5,7,-1,-3,-6,-4,]),'IF':([0,1,2,4,5,19,20,22,40,55,],[9,9,-2,-5,9,-1,-3,-6,87,-4,]),'WHILE':([0,1,2,4,5,19,20,22,55,],[11,11,-2,-5,11,-1,-3,-6,-4,]),'ADD_DEV':([0,1,2,4,5,19,20,22,55,],[12,12,-2,-5,12,-1,-3,-6,-4,]),'CMD':([0,1,2,4,5,19,20,22,55,],[13,13,-2,-5,13,-1,-3,-6,-4,]),'WAIT':([0,1,2,4,5,19,20,22,55,],[14,14,-2,-5,14,-1,-3,-6,-4,]),'ID':([0,1,2,4,5,7,9,11,12,13,14,17,19,20,22,24,29,30,32,37,45,46,55,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,95,96,123,124,131,134,],[8,8,-2,-5,8,23,35,35,45,35,35,35,-1,-3,-6,35,35,35,35,35,35,94,-4,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,121,35,35,35,35,35,]),'STEPIN':([0,1,2,4,5,19,20,22,25,26,27,28,31,33,34,35,36,38,39,40,41,42,43,55,83,84,85,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,127,128,129,130,132,133,135,137,],[15,15,-2,-5,15,-1,-3,-6,62,62,62,-40,-62,-63,-64,-65,-66,-69,-70,62,62,62,62,-4,-43,-68,-61,-41,-42,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-44,-45,-46,-47,-48,-49,-67,62,62,-75,-75,-75,62,-35,62,62,-34,]),'STEPOUT':([0,1,2,4,5,19,20,22,55,],[16,16,-2,-5,16,-1,-3,-6,-4,]),'PRINT':([0,1,2,4,5,19,20,22,55,],[17,17,-2,-5,17,-1,-3,-6,-4,]),'ELSE':([0,1,2,4,5,10,16,18,19,20,22,55,],[-75,-75,-2,-5,-75,40,-38,-39,-1,-3,-6,-4,]),'$end':([1,2,4,19,20,22,55,],[0,-2,-5,-1,-3,-6,-4,]),'ASSIGN':([8,23,],[24,56,]),'NOT':([9,11,13,29,60,61,87,96,],[29,29,29,29,29,29,29,29,]),'BITWISENOT':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,96,123,124,131,134,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'INT':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,87,96,123,124,131,134,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,110,111,31,31,31,31,31,31,31,31,31,31,31,31,]),'FLOAT':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,96,123,124,131,134,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'STR':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,96,123,124,131,134,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'LPAREN':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,96,123,124,131,134,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'MINUS':([9,11,13,14,17,24,26,29,30,31,32,33,34,35,36,37,38,39,42,44,45,50,52,54,56,57,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,84,85,86,87,92,96,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,123,124,127,129,131,134,137,],[30,30,30,30,30,30,66,30,30,-62,30,-63,-64,-65,-66,30,-69,-70,-66,66,30,66,66,66,30,66,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-68,-61,66,30,66,30,66,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,66,66,66,66,66,66,-67,30,30,66,66,30,30,66,]),'TRUE':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,96,123,124,131,134,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'FALSE':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,96,123,124,131,134,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'RETASSIGN':([13,28,31,33,34,35,36,38,39,47,49,50,51,83,84,85,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,],[46,-40,-62,-63,-64,-65,-66,-69,-70,95,-72,-73,-74,-43,-68,-61,-41,-42,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-44,-45,-46,-47,-48,-49,-67,-71,]),'AND':([25,28,31,33,34,35,36,38,39,41,51,83,84,85,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[60,-40,-62,-63,-64,-65,-66,-69,-70,60,60,-43,-68,-61,-41,-42,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-44,-45,-46,-47,-48,-49,-67,60,]),'OR':([25,28,31,33,34,35,36,38,39,41,51,83,84,85,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[61,-40,-62,-63,-64,-65,-66,-69,-70,61,61,-43,-68,-61,-41,-42,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-44,-45,-46,-47,-48,-49,-67,61,]),'PLUS':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[65,-62,-63,-64,-65,-66,-69,-70,-66,65,65,65,65,65,-68,-61,65,65,65,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,65,65,65,65,65,65,-67,65,65,65,]),'MUL':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[67,-62,-63,-64,-65,-66,-69,-70,-66,67,67,67,67,67,-68,-61,67,67,67,67,67,-52,-53,-54,-55,-56,-57,-58,-59,-60,67,67,67,67,67,67,-67,67,67,67,]),'DIV':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[68,-62,-63,-64,-65,-66,-69,-70,-66,68,68,68,68,68,-68,-61,68,68,68,68,68,-52,-53,-54,-55,-56,-57,-58,-59,-60,68,68,68,68,68,68,-67,68,68,68,]),'MOD':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[69,-62,-63,-64,-65,-66,-69,-70,-66,69,69,69,69,69,-68,-61,69,69,69,69,69,-52,-53,-54,-55,-56,-57,-58,-59,-60,69,69,69,69,69,69,-67,69,69,69,]),'POWER':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[70,-62,-63,-64,-65,-66,-69,-70,-66,70,70,70,70,70,-68,-61,70,70,70,70,70,70,70,70,-55,70,70,70,-59,-60,70,70,70,70,70,70,-67,70,70,70,]),'BITWISEAND':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[71,-62,-63,-64,-65,-66,-69,-70,-66,71,71,71,71,71,-68,-61,71,71,71,71,71,-52,-53,-54,-55,-56,-57,-58,-59,-60,71,71,71,71,71,71,-67,71,71,71,]),'BITWISEOR':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[72,-62,-63,-64,-65,-66,-69,-70,-66,72,72,72,72,72,-68,-61,72,72,72,72,72,-52,-53,-54,-55,-56,-57,-58,-59,-60,72,72,72,72,72,72,-67,72,72,72,]),'BITWISEXOR':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[73,-62,-63,-64,-65,-66,-69,-70,-66,73,73,73,73,73,-68,-61,73,73,73,73,73,-52,-53,-54,-55,-56,-57,-58,-59,-60,73,73,73,73,73,73,-67,73,73,73,]),'BITWISELS':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[74,-62,-63,-64,-65,-66,-69,-70,-66,74,74,74,74,74,-68,-61,74,74,74,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,74,74,74,74,74,74,-67,74,74,74,]),'BITWISERS':([26,31,33,34,35,36,38,39,42,44,50,52,54,57,84,85,86,92,97,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,127,129,137,],[75,-62,-63,-64,-65,-66,-69,-70,-66,75,75,75,75,75,-68,-61,75,75,75,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,75,75,75,75,75,75,-67,75,75,75,]),'LT':([26,31,33,34,35,36,38,39,42,44,50,84,85,101,102,103,104,105,106,107,108,109,110,111,118,],[76,-62,-63,-64,-65,-66,-69,-70,-66,76,76,-68,-61,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,]),'LTE':([26,31,33,34,35,36,38,39,42,44,50,84,85,101,102,103,104,105,106,107,108,109,110,111,118,],[77,-62,-63,-64,-65,-66,-69,-70,-66,77,77,-68,-61,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,]),'GT':([26,31,33,34,35,36,38,39,42,44,50,84,85,101,102,103,104,105,106,107,108,109,110,111,118,],[78,-62,-63,-64,-65,-66,-69,-70,-66,78,78,-68,-61,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,]),'GTE':([26,31,33,34,35,36,38,39,42,44,50,84,85,101,102,103,104,105,106,107,108,109,110,111,118,],[79,-62,-63,-64,-65,-66,-69,-70,-66,79,79,-68,-61,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,]),'EQUAL':([26,31,33,34,35,36,38,39,42,44,50,84,85,101,102,103,104,105,106,107,108,109,110,111,118,],[80,-62,-63,-64,-65,-66,-69,-70,-66,80,80,-68,-61,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,]),'NOTEQUAL':([26,31,33,34,35,36,38,39,42,44,50,84,85,101,102,103,104,105,106,107,108,109,110,111,118,],[81,-62,-63,-64,-65,-66,-69,-70,-66,81,81,-68,-61,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,]),'SEP':([28,31,33,34,35,36,38,39,47,49,50,51,83,84,85,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,],[-40,-62,-63,-64,-65,-66,-69,-70,96,-72,-73,-74,-43,-68,-61,-41,-42,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-44,-45,-46,-47,-48,-49,-67,-71,]),'RPAREN':([31,33,34,35,36,38,39,84,85,86,101,102,103,104,105,106,107,108,109,110,111,118,],[-62,-63,-64,-65,-66,-69,-70,-68,-61,118,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,]),'TO':([31,33,34,35,36,38,39,84,85,97,98,101,102,103,104,105,106,107,108,109,110,111,118,],[-62,-63,-64,-65,-66,-69,-70,-68,-61,123,124,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,]),'STEP':([31,33,34,35,36,38,39,84,85,101,102,103,104,105,106,107,108,109,110,111,118,127,128,129,],[-62,-63,-64,-65,-66,-69,-70,-68,-61,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,131,134,134,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,],[2,19,]),'command':([0,1,5,],[3,3,21,]),'optlvldec':([0,1,5,],[10,10,10,]),'empty':([0,1,5,25,26,27,40,41,42,43,119,120,127,128,129,130,133,135,],[18,18,18,63,63,63,63,63,63,63,63,63,132,132,132,63,63,63,]),'boolexpr':([9,11,13,29,60,61,87,96,],[25,41,51,83,99,100,119,51,]),'expr':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,96,123,124,131,134,],[26,44,50,52,54,57,44,84,85,86,92,97,44,44,101,102,103,104,105,106,107,108,109,112,113,114,115,116,117,44,50,127,129,137,137,]),'relexpr':([9,11,13,29,60,61,87,96,],[28,28,28,28,28,28,28,28,]),'bool':([9,11,13,14,17,24,29,30,32,37,45,56,60,61,65,66,67,68,69,70,71,72,73,76,77,78,79,80,81,87,96,123,124,131,134,],[36,42,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'paramlist':([13,],[47,]),'param':([13,96,],[49,122,]),'optlvlinc':([25,26,27,40,41,42,43,119,120,130,133,135,],[59,64,82,88,89,90,91,125,126,136,139,140,]),'optstep':([127,128,129,],[130,133,135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','hci_parse.py',16),
  ('program -> statement','program',1,'p_program','hci_parse.py',17),
  ('statement -> command NEWLINE','statement',2,'p_statement','hci_parse.py',31),
  ('statement -> DEV command NEWLINE','statement',3,'p_statement','hci_parse.py',32),
  ('statement -> NEWLINE','statement',1,'p_statement_newline','hci_parse.py',52),
  ('statement -> error NEWLINE','statement',2,'p_statement_bad','hci_parse.py',58),
  ('command -> FOR ID ASSIGN expr TO expr optstep optlvlinc','command',8,'p_command_for','hci_parse.py',66),
  ('command -> FOR ID ASSIGN error TO expr optstep optlvlinc','command',8,'p_command_for_bad_initial','hci_parse.py',70),
  ('command -> FOR ID ASSIGN expr TO error optstep optlvlinc','command',8,'p_command_for_bad_final','hci_parse.py',74),
  ('command -> FOR ID ASSIGN expr TO expr STEP error','command',8,'p_command_for_bad_step','hci_parse.py',78),
  ('command -> IF boolexpr optlvlinc','command',3,'p_command_if','hci_parse.py',82),
  ('command -> IF expr optlvlinc','command',3,'p_command_if','hci_parse.py',83),
  ('command -> IF error optlvlinc','command',3,'p_command_if_bad','hci_parse.py',87),
  ('command -> optlvldec ELSE IF boolexpr optlvlinc','command',5,'p_command_elseif','hci_parse.py',91),
  ('command -> optlvldec ELSE IF error optlvlinc','command',5,'p_command_elseif_bad','hci_parse.py',95),
  ('command -> optlvldec ELSE optlvlinc','command',3,'p_command_else','hci_parse.py',99),
  ('command -> WHILE boolexpr optlvlinc','command',3,'p_command_while','hci_parse.py',103),
  ('command -> WHILE bool optlvlinc','command',3,'p_command_while','hci_parse.py',104),
  ('command -> WHILE error optlvlinc','command',3,'p_command_while_bad','hci_parse.py',108),
  ('command -> ADD_DEV ID expr','command',3,'p_command_devadd','hci_parse.py',112),
  ('command -> ADD_DEV ID error','command',3,'p_command_devadd_bad','hci_parse.py',116),
  ('command -> CMD','command',1,'p_command_cmd','hci_parse.py',120),
  ('command -> CMD RETASSIGN ID','command',3,'p_command_cmd','hci_parse.py',121),
  ('command -> CMD paramlist','command',2,'p_command_cmd','hci_parse.py',122),
  ('command -> CMD paramlist RETASSIGN ID','command',4,'p_command_cmd','hci_parse.py',123),
  ('command -> CMD error','command',2,'p_command_cmd_bad','hci_parse.py',134),
  ('command -> WAIT expr','command',2,'p_command_wait','hci_parse.py',138),
  ('command -> WAIT error','command',2,'p_command_wait_bad','hci_parse.py',142),
  ('command -> ID ASSIGN expr','command',3,'p_command_assignvar','hci_parse.py',146),
  ('command -> ID ASSIGN error','command',3,'p_command_assignvar_bad','hci_parse.py',153),
  ('command -> STEPIN','command',1,'p_command_lvlchange','hci_parse.py',157),
  ('command -> STEPOUT','command',1,'p_command_lvlchange','hci_parse.py',158),
  ('command -> PRINT expr','command',2,'p_command_print','hci_parse.py',162),
  ('optstep -> STEP expr','optstep',2,'p_optstep','hci_parse.py',166),
  ('optstep -> empty','optstep',1,'p_optstep','hci_parse.py',167),
  ('optlvlinc -> STEPIN','optlvlinc',1,'p_optlvlinc','hci_parse.py',174),
  ('optlvlinc -> empty','optlvlinc',1,'p_optlvlinc','hci_parse.py',175),
  ('optlvldec -> STEPOUT','optlvldec',1,'p_optlvldec','hci_parse.py',182),
  ('optlvldec -> empty','optlvldec',1,'p_optlvldec','hci_parse.py',183),
  ('boolexpr -> relexpr','boolexpr',1,'p_boolexpr','hci_parse.py',190),
  ('boolexpr -> boolexpr AND boolexpr','boolexpr',3,'p_boolexpr','hci_parse.py',191),
  ('boolexpr -> boolexpr OR boolexpr','boolexpr',3,'p_boolexpr','hci_parse.py',192),
  ('boolexpr -> NOT boolexpr','boolexpr',2,'p_boolexpr','hci_parse.py',193),
  ('relexpr -> expr LT expr','relexpr',3,'p_relexpr','hci_parse.py',202),
  ('relexpr -> expr LTE expr','relexpr',3,'p_relexpr','hci_parse.py',203),
  ('relexpr -> expr GT expr','relexpr',3,'p_relexpr','hci_parse.py',204),
  ('relexpr -> expr GTE expr','relexpr',3,'p_relexpr','hci_parse.py',205),
  ('relexpr -> expr EQUAL expr','relexpr',3,'p_relexpr','hci_parse.py',206),
  ('relexpr -> expr NOTEQUAL expr','relexpr',3,'p_relexpr','hci_parse.py',207),
  ('expr -> expr PLUS expr','expr',3,'p_expr_binary','hci_parse.py',211),
  ('expr -> expr MINUS expr','expr',3,'p_expr_binary','hci_parse.py',212),
  ('expr -> expr MUL expr','expr',3,'p_expr_binary','hci_parse.py',213),
  ('expr -> expr DIV expr','expr',3,'p_expr_binary','hci_parse.py',214),
  ('expr -> expr MOD expr','expr',3,'p_expr_binary','hci_parse.py',215),
  ('expr -> expr POWER expr','expr',3,'p_expr_binary','hci_parse.py',216),
  ('expr -> expr BITWISEAND expr','expr',3,'p_expr_bitwise','hci_parse.py',220),
  ('expr -> expr BITWISEOR expr','expr',3,'p_expr_bitwise','hci_parse.py',221),
  ('expr -> expr BITWISEXOR expr','expr',3,'p_expr_bitwise','hci_parse.py',222),
  ('expr -> expr BITWISELS INT','expr',3,'p_expr_bitwise','hci_parse.py',223),
  ('expr -> expr BITWISERS INT','expr',3,'p_expr_bitwise','hci_parse.py',224),
  ('expr -> BITWISENOT expr','expr',2,'p_expr_bitwise','hci_parse.py',225),
  ('expr -> INT','expr',1,'p_expr_number','hci_parse.py',232),
  ('expr -> FLOAT','expr',1,'p_expr_number','hci_parse.py',233),
  ('expr -> STR','expr',1,'p_expr_string','hci_parse.py',237),
  ('expr -> ID','expr',1,'p_expr_variable','hci_parse.py',241),
  ('expr -> bool','expr',1,'p_expr_bool','hci_parse.py',245),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr_group','hci_parse.py',249),
  ('expr -> MINUS expr','expr',2,'p_expr_unary','hci_parse.py',253),
  ('bool -> TRUE','bool',1,'p_bool','hci_parse.py',257),
  ('bool -> FALSE','bool',1,'p_bool','hci_parse.py',258),
  ('paramlist -> paramlist SEP param','paramlist',3,'p_paramlist','hci_parse.py',262),
  ('paramlist -> param','paramlist',1,'p_paramlist','hci_parse.py',263),
  ('param -> expr','param',1,'p_param_expr','hci_parse.py',271),
  ('param -> boolexpr','param',1,'p_param_expr','hci_parse.py',272),
  ('empty -> <empty>','empty',0,'p_empty','hci_parse.py',276),
]

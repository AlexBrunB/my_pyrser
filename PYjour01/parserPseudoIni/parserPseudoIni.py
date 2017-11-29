#!/usr/bin/env python3

from pyrser import grammar, meta, parsing

class parserPseudoIni(grammar.Grammar):
    entry = "Ini"
    grammar =  """
        Ini = [ Section+:n #is_section(_, n) eof ]
        
        Section = [ '[' id:m ']' #is_key ClefValeur+:key #add_key(_, key) ]
 
        ClefValeur = [ id:n '=' valeur:value #is_value(_, n, value) ]

        valeur = [ id:n #is_id(_, n) | num:n #is_num(_, n) | string:n #is_id(_, n) ]
        """
 
@meta.hook(parserPseudoIni)
def is_section(self, ast, node):
    ast.node = []
    return True

@meta.hook(parserPseudoIni)
def is_num(self, ast, node):
    ast.node = int(self.value(node))
    return True

@meta.hook(parserPseudoIni)
def is_id(self, ast, arg):
    ast.node = self.value(arg)
    return True

@meta.hook(parserPseudoIni)
def is_value(self, ast, n, value):
    ast.node = {}
    ast.node = (self.value(n).strip('"'), value.node)
    return True

@meta.hook(parserPseudoIni)
def is_dict(self, ast):
    ast.node = {}
    return True

@meta.hook(parserPseudoIni)
def add_key(self, ast, item):
    ast.node.append(item.node)
    return True

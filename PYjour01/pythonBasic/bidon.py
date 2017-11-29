#/usr/bin/env python3

class Bidon:
    
    zaz = "je suis un pro du python"
    num = 42

    def __init__(self, message, num=42, **args):
        self.txt = message
        self.num = num
        for my_arg in args:
            setattr(self, my_arg, args[my_arg])


def var2listsort(*args):
      my_tab = []
    
      for x in args:
          my_tab.append(x)
  
      return sorted(my_tab)

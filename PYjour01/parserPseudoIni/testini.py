
import sys
from parserPseudoIni import * 

ini = parserPseudoIni()
res = ini.parse_file(sys.argv[1])
  
for section_name, section_values in res.sections.items():
    print("variable [%s] %s = %s" % (section_name, key, value))

import re

import sys

if len(sys.argv) == 3:
    l = sys.argv[1:]
    obj_type = l[1][1:]
    cur_path = l[0][2:-4]+"/"
# if len(sys.argv) == 2:
#     l = sys.argv[1:]
#     cur_path = l[0][2:-4]+"/"
#     f_name = l[0][2:]

k = []
fh = open(cur_path+"obj_py.txt")
fh1 = open(cur_path+"output.lp","a")
fh1.write(obj_type)
fh1.write("\n")
l = fh.readlines()
for i in l:
  if(re.search(r"^\\[*]\s[A-Z]+[a-z]+ ?[a-z]+ [*]\\",i)):
    continue
  elif(re.search(r"^\s+",i)):
    continue
  elif(re.search(r"^[A-Z]+[a-z]+ ?.[a-z]+",i)):
    fh1.write(i)
  else:  
    fh1.write("\t")
    corect = i.replace("v","").replace("(","").replace(")","").replace('"',"")
    fh1.write(corect)
fh1.write("End")

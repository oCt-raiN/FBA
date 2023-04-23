import numpy as np
import sys

if len(sys.argv) == 2:
    l = sys.argv[1:]
    cur_path = l[0][2:-4]+"/"
    f_name = l[0][2:]

    

f1=open(cur_path+"python_stoichiometric.txt", "w")
f2=open(cur_path+"python_reactions.txt")
f3=open(cur_path+"speciesid_py.txt")
sid=[]
rxn=[]
f3=f3.readlines()
f2=f2.readlines()
mat=np.zeros((len(f3), len(f2)), dtype=float)
for line in f3:
    line.strip()
    sid.append(line)
j=0
for line in f2:
    line.strip()
    rxn.append(line)
    temp=line.split("--->")
    if len(temp)==2:
        temp1=temp[0].split("+")
        temp2=temp[1].split("+")
        temp1=[(ele.split()) for ele in temp1]
        temp2=[(ele.split()) for ele in temp2]
    #print("yes done")
    for i in range(len(temp1)):
        for k in range(len(sid)):
            if(str(temp1[i][1]).strip()==str(sid[k]).strip()):
                val=i-1
                mat[k][j]=float(temp1[val][0])*(-1)
    for i in range(len(temp2)):
        for k in range(len(sid)):
            if(str(temp2[i][1]).strip()==str(sid[k]).strip()):
                #print("yes")
                val=i-1
                print(float(temp2[val][0]))
                mat[k][j]=float(temp2[val][0])
    j+=1
for y in range(len(sid)):
    for x in range(j):
        if(mat[y][x]):
            f1.write(str(mat[y][x]))
            f1.write("\t")
        else:
            f1.write(str(mat[y][x]))
            f1.write("\t")
    f1.write("\n")

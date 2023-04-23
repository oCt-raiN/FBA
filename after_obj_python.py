import sys

if len(sys.argv) == 2:
    l = sys.argv[1:]
    cur_path = l[0][2:-4]+"/"
    f_name = l[0][2:]

f1=open(cur_path+"reactionid_py.txt");
f2=open(cur_path+"python_stoichiometric.txt");
f3=open(cur_path+"bounds_py.txt");
f4=open(cur_path+"obj_py.txt", "w")
f5=open(cur_path+"objective_function_py.txt");
f1=f1.readlines()
f2=f2.readlines()
f3=f3.readlines()
f5=f5.readlines()
rid=[]
for line in f1:
    rid.append(line.strip())
f4.write("\\* Objective function *\\")
f4.write("\n")
f4.write("obj: ")
for line in f5:
    f4.write(line.strip())
count=0
f4.write("\n")
f4.write("\n")
f4.write("\* Constraints *\\")
f4.write("\n")
f4.write("Subject To")
f4.write("\n")
for line in f2:
    line=line.strip()
    count+=1
    f4.write("one_"+str(count)+": ")
    temp=line.split("\t")
    for i in range(len(temp)):
        if float(temp[i])<0:
            f4.write(" "+str(temp[i])+" v("+ str(rid[i])+")")
        if temp[i]==0:
            pass
        else:
            f4.write(" +"+str(temp[i])+" v("+str(rid[i])+")")
    f4.write(" = 0\n")
f4.write("\n")
f4.write("\n")
f4.write("\* Variable bounds *\\")
f4.write("\n")
f4.write("Bounds")
f4.write("\n")
for line in f3:
    f4.write(line)

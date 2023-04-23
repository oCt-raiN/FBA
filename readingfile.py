import re
import sys

if len(sys.argv) == 2:
    l = sys.argv[1:]
    cur_path = l[0][2:-4]+"/"
    f_name = l[0][2:]

f1=open(f_name)
#f2=open("reactions_py.txt", "w")
f3=open(cur_path+"speciesid_py.txt", "w")
f4=open(cur_path+"species_py.txt", "w")
f5=open(cur_path+"reactionid_py.txt", "w")
f6=open(cur_path+"objective_function_py.txt", "w")
f7=open(cur_path+"bounds_py.txt", "w")
f1=f1.readlines()
for line in f1:
    if re.match(r"\s*<reaction\s", line):
        elements=line.split()
        for ele in elements:
            t=ele.split("=")
            if(t[0]=="id"):
                rid=t[1]
                f5.write(t[1])
                f5.write("\n")
            if(t[0]=="name"):
                rname=t[1]
            if(t[0]=="reversible"):
                rrevers=t[1]

    if re.match(r"\s*<species\s", line):
        species_id_name={}
        elements=line.split()
        for ele in elements:
            t=ele.split("=")
            if(t[0]=="id"):
                sid=t[1]
                f3.write(t[1])
                f3.write("\n")
            if(t[0]=="name"):
                sname=t[1]
                f4.write(t[1])
                f4.write("\n")
                species_id_name[sid]=sname
    x=1
    '''if re.match(r"^\s*<listOfReactants>", line):
        cr=0
        ab1=[]
        ab2=[]
        if(x==1):
            elements=line.split()
            for ele in elements:
                t=ele.split("=")
                if(t[0]=="species"):
                    temp2=t
                if(t[0]=="stoichiometry"):
                    temp3=t
            ab1.append(temp2[1])#product(species id) stored in array ab3
            ab2.append(temp3[1])#stoiciometry of products stored in array ab4
            cr+=1
        continue
    if re.match(r"^\s*<\/listOfReactants>", line):
        x=0

    if re.match(r"^\s*<listOfProducts>", line):
        y=1
        cp=0
        ab3=[]
        ab4=[]
        elements=line.split()
        for ele in elements:
            t=ele.split("=")
            if(t[0]=="species"):
                temp2=t
            if(t[0]=="stoichiometry"):
                temp3=t
        ab3.append(temp2[1]);#product(species id) stored in array ab3
        ab4.append(temp3[1]);#stoiciometry of products stored in array ab4
        cp+=1;
        continue
    if re.match(r"^\s*<\/listOfProducts>", line):
        y=0
    if(y==1):
        elements=line.split()
        for ele in elements:
            t=ele.split("=")
            if(t[0]=="species"):
                temp2=t
            if(t[0]=="stoichiometry"):
                temp3=t
        ab3.append(temp2[1]);#product(species id) stored in array ab3
        ab4.append(temp3[1]);#stoiciometry of products stored in array ab4
        cp+=1;'''
    if re.match(r"^\s*<parameter id=\"FLUX_VALUE\"/", line) or '<parameter id="FLUX_VALUE"' in line:
        fv=0
        param_values=[]
        elements=line.split()
        for ele in elements[1:]:
            left, right=ele.split("=")
            if left=="id":
                param_values.append(right)
            if left=="value":
                fv=right
    if re.match(r"^\s*<parameter id=\"UPPER_BOUND\"/", line) or '<parameter id="UPPER_BOUND"' in line:
        ub=0
        elements=line.split()
        for ele in elements[1:]:
            left, right=ele.split("=")
            if left=="value":
                ub=right
    if re.match(r"^\s*<parameter id=\"LOWER_BOUND\"/", line) or '<parameter id="LOWER_BOUND"' in line:
        lb=0
        elements=line.split()
        for ele in elements[1:]:
            left, right=ele.split("=")
            if left=="value":
                lb=right
    if re.match(r"^\s*<\/reaction>/", line) or "</reaction>" in line:
        #print("yes found")
        fv_list=fv.split('"')
        if float(fv_list[1])<0:
            f6.write(" "+fv_list[1]+"v("+str(rid)+")")
            f6.write("\n")
        elif float(fv_list[1])==0:
            pass
        else:
            f6.write(" +"+fv_list[1]+" v("+str(rid)+")")

        f7.write("v("+str(rid)+") < "+ub)
        f7.write("\n")
        f7.write("v("+str(rid)+") > "+lb)
        f7.write("\n")

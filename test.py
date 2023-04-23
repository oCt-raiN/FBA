import re
import sys

if len(sys.argv) == 2:
    l = sys.argv[1:]
    cur_path = l[0][2:-4]+"/"
    f_name = l[0][2:]

with open(cur_path+"python_reactions.txt", "w") as file:
    with open(f_name, "r+") as f1:
        for line in f1:
            reactants=[]
            products=[]
            if re.match(r"^\s*<listOfReactants>", line):
                x=next(f1)
                while not re.match(r"^\s*<\/listOfReactants>", x):
                    temp=x.split()
                    for val in temp:
                        temp2=val.split("=")
                        if temp2[0]=="species":
                            temp4=temp2[1].split('"')
                            r=temp4[1]
                        if temp2[0]=="stoichiometry":
                            temp3=temp2[1].split('"')
                            v=(temp3[1])
                    reactants.append(v+" "+r)
                    x=next(f1)
                if reactants!=[]:
                    #pass
                    #print("reactants is: ", reactants)
                    file.write(" + ".join(reactants)+" ")
            elif re.match(r"^\s*<listOfProducts>", line):
                x=next(f1)
                while not re.match(r"^\s*<\/listOfProducts>", x):
                    temp=x.split()
                    for val in temp:
                        temp2=val.split("=")
                        if temp2[0]=="species":
                            temp4=temp2[1].split('"')
                            s=temp4[1]
                        if temp2[0]=="stoichiometry":
                            temp3=temp2[1].split('"')
                            va=(temp3[1])
                    products.append(va+" "+s)
                    x=next(f1)
                if products!=[]:
                    #pass
                    file.write("--->"+" ")
                    file.write(" + ".join(products))
                    file.write("\n")

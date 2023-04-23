from django.shortcuts import render
from django.http import HttpResponse  
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
import os
import time
# Create your views here.
path = ""
def index(request):
    return render(request,'index.html')

def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES ['xml']
        objtype_name = request.POST["obj"]
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs =FileSystemStorage()
        urlname = fs.save(uploaded_file.name,uploaded_file)
        url = fs.url(urlname)
        os.system("mkdir media/"+urlname[:-4])
        os.system("python3 readingfile.py i"+url)
        time.sleep(3)
        os.system("python3 test.py i"+url)
        time.sleep(3)
        os.system("python3 stochiometric_mat.py i"+url)
        time.sleep(3)
        os.system("python3 after_obj_python.py i"+url)
        time.sleep(3)
        os.system("python3 final.py i"+url+" t"+objtype_name)
        time.sleep(3)
        cur_path = url[1:-4]+"/"
        os.system("glpsol --cpxlp "+cur_path+"output.lp -o "+cur_path+"result.txt")
        dest1 = cur_path
        fl = open(cur_path+"result.txt")
        path = cur_path
        lines = fl.readlines()
        q=""
        for i in range(0,7):
            if i==0:
                q+=lines[i][:-3].strip()
                q+="\n"
            else:
                q+=lines[i]
        #q+="\n"
        q+="For the sbml file uploaded by you, download the output files displayed below."
    return render(request,'result.html',{"des":dest1,"output":q,"path":path})
    
    

def house(request):
    return render(request,"4.html")

def constrain(request):
    return render(request,"3.html")

def stoichiometry(request):
    return render(request,"2.html")

def fba(request):
    return render(request,'1.html')

def help(request):
    return render(request,"help.html")

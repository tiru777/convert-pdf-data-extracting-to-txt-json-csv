import os

from os import chdir, getcwd, listdir, path

import PyPDF2

from time import strftime

import json

import re

import csv


def check_path(prompt):

    ''' (str) -> str

    Verifies if the provided absolute path does exist.

    '''

    abs_path = input(prompt)

    while path.exists(abs_path) != True:

        print("\nThe specified path does not exist.\n")

        abs_path = input(prompt)

    return abs_path   
print("\n")

folder = check_path("Provide absolute path for the folder: ")


list=[]

directory=folder

for root,dirs,files in os.walk(directory):

    for file in files:

        if file.endswith('.pdf'):

            t=os.path.join(directory,file)

            #print(t)

            list.append(t)
#print(list)

m=len(list)
  
# Load PDF into pyPDF
k=0
for i in list:
    
    path = list[k]
    k=k+1
    head,tail=os.path.split(path)
    var="\\"
    tail=tail.replace(".pdf",".txt")
    name=head+var+tail
    content = ""
        
    pdf = PyPDF2.PdfFileReader(i,"rb")

    
    page=pdf.getPage(0)#it will take first page of file
    
    tt=page.extractText()
    
    content = tt 

    print(strftime("%H:%M:%S"), " pdf  -> txt ")
    
    with open(name,'w') as obj:
        
        textdoc=obj.write(tt)
   
    with open(name) as json_file:  
        s=json_file.read()
        data = json.dumps(s)
        tt=re.findall("\w{2,4}\d{2,8}",data)
        tt1=re.findall("\d{2}.\w{2,}.\d{4}",data)
        
        with open('%s.csv'%(name),'w') as obj:
            a = csv.writer(obj)
            data = [['Invoice Number','Invoice Date']]
            a.writerows(data)
            obj.write(str(tt))
            obj.write(str(tt1))
    if m==k:
        break





    

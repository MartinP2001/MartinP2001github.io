from markdown2 import Markdown
import os
import re
import shutil

variable = os.listdir("./input")[0:-1]
print(variable)
list_HTML = []
for variables in variable:
    with open("./input/{}".format(variables), "r", encoding="utf-8") as input_file:
        text = input_file.read()
        markdowner = Markdown()   
        html = markdowner.convert(text)
        list_HTML = list_HTML + [html]
        
image = os.listdir("./input/pictures")
print(image)
os.chdir("output")                      #Change le repertoire de travail

folder_number = str(len(os.listdir())+1)    #Récupere en string la longueur de la liste du contenu de dossier de travail
os.mkdir(folder_number)
os.mkdir(os.path.join(folder_number,'images'))



for images in image:
    with open("./"+ folder_number +"/images/"+images , "w" , encoding="utf-8") as content_file:
        content_file.write(images)

nom_html = []
for variables in variable:
    nom_html = nom_html + [variables.split(".")[0]]
    print(nom_html)

    html_page = []
for lists_HTML in list_HTML:
    with open("../template.html", "r" , encoding="utf-8") as template_file:
        template = template_file.read()
    # print(template)
    html_page = html_page + [template.replace("{{Contenu}}",lists_HTML,1)]
    print(html_page)

print(nom_html)
compteur = 0
for html_pages in html_page:

    with open("./"+ folder_number +"/"+str(nom_html[compteur])+".html", "w" , encoding="utf-8") as content_file:
        content_file.write(html_pages)
    compteur = compteur + 1
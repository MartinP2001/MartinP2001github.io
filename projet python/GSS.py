from markdown2 import Markdown
import os
import re
import shutil

with open("./Markdown_Python2.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()
    markdowner = Markdown()   
    html = markdowner.convert(text)
    print(html)
#Change le repertoire de travail
os.chdir("output") 
#Récupere en string la longueur de la liste du contenu de dossier de travail
folder_number = str(len(os.listdir())+1)
os.mkdir(folder_number)
os.mkdir(os.path.join(folder_number,'pictures'))
os.mkdir(os.path.join(folder_number,'link'))

search_image = re.compile('img src=".+((\.jpg)|(\.png))"')
images_list = re.finditer(search_image,html)
for image in images_list :
    lien_image = image.group()[9:-1]
    nom_image = lien_image.split("/")[-1]
    if("http://" not in lien_image or "https://" not in lien_image):
        shutil.copy(lien_image,os.path.join(folder_number,'pictures'))
        print(lien_image)
        print(nom_image)
        html = html.replace(lien_image,"./pictures/{}".format(nom_image))

search_lien = re.compile('a href=".+(\.md)"')
liens_list = re.finditer(search_lien,html)
for lien in liens_list :   
    lien_markdown = lien.group()[8:-1]
  
  
    nom_lien = lien_markdown.split("/")[-1]    
    if("http://" not in lien_markdown or "https://" not in lien_markdown):
        shutil.copy(lien_markdown,os.path.join(folder_number,'link'))
        print(lien_markdown)
        print(nom_lien)
        html = html.replace(lien_markdown,"./link/{}".format(nom_lien))


with open("../template.html", "r" , encoding="utf-8") as template_file:
    template = template_file.read()
# print(template)

html_page = template.replace("{{Contenu}}",html,1)

with open("{}/contenu.html".format(folder_number), "w" , encoding="utf-8") as content_file:
    content_file.write(html_page)
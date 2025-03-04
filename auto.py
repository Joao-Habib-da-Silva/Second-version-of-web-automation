#At first, we will put the library
from xml.dom.minidom import Document
from selenium import webdriver as wb
import os as os
import time
from googletrans import Translator
#Now we will put the function who i will use in this code, the function of open the browser with the tabs of principal sites for web develop
translator = Translator()
def traduza(par1, par2):
    return translator.translate(par1, dest=par2).text

def informações():
    global lang
    lang = str(input("""At first, say your language:
                   
_____________________________________________________
                   
                   Your options are:
                   en = English
                   pt = Portuguese
                   es = spanish
                   ja = japanese
                   nl = dutch
                    eo = esperanto
_____________________________________________________
                   
Now, what you want lang do you want?"""))
#Now we get the principal informations
informações()
#Selenium being used
def sites():
    nav = wb.Chrome()
    nav.get("https://coolors.co")
    nav.maximize_window()
    nav.switch_to.new_window("tab")
    nav.get("https://boxicons.com")
    nav.switch_to.new_window("tab")
    nav.get("https://www.pngwing.com/pt")
    nav.switch_to.new_window("tab")
    nav.get("https://fonts.google.com")
    time.sleep(100000)
#Now, the function who create the archives
def criar():
   inputhtml = input(traduza("Nome do arquivo Html?", lang))
   inputcss = input(traduza("Nome do arquivo Css?", lang))
   inputjs = input(traduza("Nome do arquivo em Js?", lang))
   contenthtml = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{inputhtml + '.html'}</title>
    <link rel="stylesheet" href="{inputcss + '.css'}">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

</head>
<body>
    <script src="{inputjs + '.js'}"></script>
</body>
</html>"""
   contentcss = """ * {
   
    margin: 0;
    padding: 0;
    scroll-behavior:smooth;
    box-sizing: border-box;
    overflow-x: hidden;
}"""
   contentjs = """"""
   contentgitignore = """"""
   contenttxtlinks = '''<script src="https://cdnjs.cloudflare.com/ajax/libs/animarray = ejs/3.2.1/anime.min.js"></script>
<script src="https://unpkg.com/tippy.js@6/dist/tippy-bund1.umd.js"></script>
    '''
   with open(inputhtml + '.html', 'w', encoding='utf-8') as htmlarchive:
        htmlarchive.write(contenthtml)
   with open(inputcss + '.css', 'w', encoding='utf-8') as cssarchive:
        cssarchive.write(contentcss)
   with open(inputjs + '.js', 'w', encoding='utf-8') as jsarchive:
        jsarchive.write(contentjs)
   with open('links.txt', 'w') as links:
        links.write(contenttxtlinks)
   with open(".gitignore", 'w') as git:
        git.write(contentgitignore)
#After we created the functions, we can begin our code really
print(traduza("Bem vindo ao seu automatizador de códigos front-end", lang))
print(traduza("Aqui, poderemos fazer seu código tudo arrumado, diminuindo seu tempo de fazer coisas básicas, apenas pondo a mão na massa!!", lang))
path = input(traduza("Qual o diretório que você deseja?", lang))
#All contents being translated with the first function
def existir():
    #There we are, here, the code will see if the path exists or not, or if they have basic paths
    if os.path.exists(path) != True:
        print(traduza("Seu diretório não existe, só fazemos quando o diretório exist", lang))
        #I dont like the part of use a lot of or in my if, so in  my next code i will change that
    if os.path.exists(path) == True or path == 'Downloads' or path == 'downloads' or path == 'download' or path == 'downloads' or path == 'Document' or path == 'Documents' or path == 'document' or path == 'documents':
        print(traduza("Achamos o seu diretório!", lang))
    if path == 'Downloads' or path == 'downloads' or path == 'download' or path == 'downloads' and os.path.exists(path) != True:
        download = r'~/Downloads'
        #We use the ~ for use the os.path.expanduser, with that function of os, we dont need the users part of path
        downloadfull = os.path.expanduser(download)
        os.chdir(downloadfull)
    if path == 'Document' or path == 'Documents' or path == 'document' or path == 'documents' and os.path.exists(path) != True:
        document = r'~/Documents'
        documentfull = os.path.expanduser(document)
        os.chdir(documentfull)
existir()
print(traduza("Agora estamos no diretório que deseja!", lang))
#The prefs will be like a terminal, Y or N?
pref = str(input(traduza("Por acaso você gostaria de criar uma pasta (Y/N)?", lang)))
if pref == 'Y' or pref == 'y':
    print(traduza("Ok, vamos criar uma para você", lang))
    pasta = str(input(traduza("Qual o nome da pasta?", lang)))
    os.mkdir(pasta)
    atual = os.getcwd()
    os.chdir(atual + "\\" + pasta)
elif pref == 'N' or pref == 'n':
    print(traduza("Certo, você que manda!", lang))
#Then we have the create and for least, the part who will open the Chrome pages
criar()
sites()
import configparser
def writeFromTemplate(template,args=[]):
    for line in template:
       if not "%" in line:
           render.write(line)
       else:
           for arg in args:
               if arg[0] in line:
                   render.write(line.replace(arg[0],arg[1]))
def renderFile(content):
    for tline in template:
        if not "%" in tline:
            render.write(tline)
        if(tline == "%CONTENT%\n"):
            for contentBlock in content:
                render.write("<div class='contentcontainer'>\n")
                titleTemplate = open("titletemplate.html","r")
                writeFromTemplate(titleTemplate,[["%TITLE%",contentBlock[2]],["%AUTHOR%",contentBlock[3]]])
                titleTemplate.close()
                #Render poems
                if contentBlock[1] == "poem":
                    poemTemplate = open("poemtemplate.html","r")
                    writeFromTemplate(poemTemplate,[["%POEM%",contentBlock[4]]])
                    poemTemplate.close()
                render.write("</div>\n")
                render.write("<br>")

def readInput(inputFile):
    content=[]
    config = configparser.ConfigParser()
    config.read(inputFile)
    for section in config.sections():
        contentBlock=[int(section),config[section]['type'],config[section]['title'],config[section]['author'],config[section]['content']]
        content.append(contentBlock)
    content.sort()
    return(content)

#Template and render files
render = open("render.html","w")
template = open("template.html","r")
renderFile(readInput("input.txt"))


render.close()
template.close()

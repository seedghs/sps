import jinja2

templateLoader = jinja2.FileSystemLoader( searchpath="." )
templateEnv = jinja2.Environment( loader=templateLoader )

TEMPLATE_FILE = "template.html"
template = templateEnv.get_template( TEMPLATE_FILE )

# Here we add a new input variable containing a list.
# Its contents will be expanded in the HTML as a unordered list.

templateVars = { "stuff": "meow" }  
outputText = template.render( templateVars )

f = open("render.html","w")
f.write(outputText)
f.close()

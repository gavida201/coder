from django.http import HttpResponse

def saludo(request):
    return HttpResponse("hola amigos")

def dia_de_hoy(request):
    import datetime
    dia = datetime.datetime.now()
    documentoDeTexto = f"hoy es el día {dia}"
    return HttpResponse(documentoDeTexto)

def mi_nombre_es(self, nombre):
    documentoDeTexto = f'mi nombre es {nombre}'
    return  HttpResponse(documentoDeTexto)

def probando_template(request):
    from .settings import BASE_DIR

    from django.template import Template, Context, loader
    import datetime
    
    nombre = "luis"
    apellido = "fonzi"
    
 
#    mi_html = open("repaso/templates/template1.html", "r")
    mi_html = loader.get_template('template1.html')
    
    #plantilla = Template(mi_html.read())
    #mi_html.close()
    
    diccionario = {
        "nombre": nombre, 
        "apellido":apellido, 
        "hoy": datetime.datetime.now(), 
        "lista_notas": [3, 6, 10, 4, 8],
        }
    
    #mi_contexto = Context(diccionario)
    documento = mi_html.render(diccionario)
    return HttpResponse(documento)
    
    


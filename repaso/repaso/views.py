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
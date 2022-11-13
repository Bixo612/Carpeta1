from django.http import HttpResponse


def HolaMundo(request):
    return HttpResponse("<h1>Hola Mundo</h1>")


def cierre(request):
    texto = '''
        <html>
        <head>
            <title>Cierre</title>
        </head>
        <body>
            <h1>Esta es una página de ejemplo para el uso de html completo</h1>
            <p>en esta página lo que se busca es poder mostrar como se realizan algunos elementos</p>
            <a href="../hola">ir a hola</a>
            <h4>Subtitulo</h4>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem dolorem numquam facere odio provident atque voluptatum excepturi officiis inventore consequuntur. Porro architecto est dicta ullam veniam maiores nam iusto quisquam.</p>
        </body>
        </html>
    '''
    return HttpResponse(texto)

def hora(request):
    texto = '''
        <html>
            <head></head>
            <body></body>
        </html>
    '''
    return HttpResponse(texto)

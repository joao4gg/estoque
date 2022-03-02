from django.http import HttpResponse

from AmoxProject.master import basic_decode


def teste(request):
    t = 'eyJpZCI6IiBlMyBlZCAyMyAwOCJ9='
    retorno = basic_decode(t)

    return HttpResponse(retorno['id'])

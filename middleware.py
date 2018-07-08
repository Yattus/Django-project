from django.db.models import F
from Etudiant.models import Page


def simple_middleware(get_response):
    def middleware(request):

        try:
            p= Page.objects.get(url= request.patch)
            p.nb_visite = F('nb_visite') + 1
            p.save()
        except Page.DoesNotExist:
            Page.objects.create(url=request.patch)


        response = get_response(request)

        response.content += bytes(
        "Cette page à été vue {0} fois.".format(p.nb_visite),
        "utf-8"
        )

        return response


    return middleware


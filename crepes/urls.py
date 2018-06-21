from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView, ListView
from Etudiant.views import ListDomaine
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    # Examples:
    url(r'^admin/', admin.site.urls),
    # url(r'^$', 'crepes.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^Etudiant/', include('Etudiant.urls')),
    url(r'^$', ListDomaine.as_view(template_name= "base.html"), name="base"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
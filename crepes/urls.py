from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import ListView
from django.conf.urls.static import static
from django.conf import settings
from Etudiant.views import ListDomaine

urlpatterns= [
    # Examples:
    url(r'^admin/', admin.site.urls),
    # url(r'^$', 'crepes.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^Etudiant/', include('Etudiant.urls')),
    url(r'^$', ListDomaine.as_view(template_name= "base.html"), name="base"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

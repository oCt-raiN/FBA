from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('upload',views.upload,name='upload'),
    path('house',views.house,name='house'),
    path('constrain',views.constrain,name='constrain'),
    path('stoichiometry',views.stoichiometry,name='stoichiometry'),
    path('FBA',views.fba,name='FBA'),
    path('help',views.help,name='help')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

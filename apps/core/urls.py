from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'apps.core.views.index', name='index'),
    url(r'^seleccionar-ciudad/$', 'apps.core.views.seleccionar_ciudad', name='seleccionar_ciudad'),

    # Agregar contenido
    url(r'^lineas/agregar/$', 'apps.core.views.agregar_linea', name='agregar_linea'),
    url(r'^recorridos/agregar/$', 'apps.core.views.agregar_recorrido', name='agregar_recorrido'),

    # Ciudades
    url(r'^(?P<nombre_ciudad>[\w-]+)/$', 'apps.core.views.ver_ciudad', name='ver_ciudad'),
    url(r'^mapa/(?P<nombre_ciudad>[\w-]+)/$', 'apps.core.views.ver_mapa_ciudad', name='ver_mapa_ciudad'),

    # Lineas
    url(r'^(?P<nombre_ciudad>[\w-]+)/(?P<nombre_linea>[\w-]+)/$', 'apps.core.views.ver_linea', name='ver_linea'),

    # Recorridos
    url(r'^(?P<nombre_ciudad>[\w-]+)/(?P<nombre_linea>[\w-]+)/(?P<nombre_recorrido>[\w-]+)/$', 'apps.core.views.ver_recorrido', name='ver_recorrido'),
)
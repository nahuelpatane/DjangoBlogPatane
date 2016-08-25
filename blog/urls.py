from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'blog.views.muestrainicio', name='Inicio' ),
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
                       url(r'^botonloco/$', 'blog.views.verbtnmg', name='Boton Loco' ),
                       url(r'^calculadora/$', 'blog.views.vercal', name='Calculadora' ),
                       url(r'^conversor/$', 'blog.views.verconv', name='Conversor' ),
                       url(r'^cronometro/$', 'blog.views.vercro', name='Cronometro' ),
                       url(r'^Imagenes/$', 'blog.views.verimagen', name='Imagenes' ),
                       url(r'^comentarios/$', 'blog.views.vernoticias', name='Comentarios' ),
                       url(r'^Personal/$', 'blog.views.mostrarper', name='Personal' ),
                      )

from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada 

import os

def muestrainicio(request):
    return render_to_response('Inicio.html',
                              {},
                              RequestContext(request))
def verbtnmg(request):
    return render_to_response('cambiolugar.html',
                              {},
                              RequestContext(request))
def mostrarper(request):
    return render_to_response('personal.html',
                              {},
                              RequestContext(request))
def vercal(request):
    return render_to_response('Calculadora.html',
                              {},
                              RequestContext(request))
def verconv(request):
    return render_to_response('conversor.html',
                              {},
                              RequestContext(request))
def vercro(request):
    return render_to_response('cronometro.html',
                              {},
                              RequestContext(request))
def verimagen(request):
    return render_to_response('Imagenes.html',{},RequestContext(request))

def vernoticias(request):
    context = RequestContext(request)
    posts = Entrada.objects.all()
    return render_to_response('comentarios.html',{'posts':posts},context)

def ver_post(request, id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id=id_post)
    return render_to_response('post.html',{'post':mi_post},context)

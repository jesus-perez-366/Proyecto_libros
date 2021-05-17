from os import truncate
from django.shortcuts import render
from consultas import models as bd
import pandas as pd

def actualizar():
    libros = bd.libro.objects.all()
    df_libros=pd.DataFrame()
    for l2 in libros:
        l3=str(l2.categoria).split('-')
        d={'id':str(l2.id),
            'categoria':l3,
            'titulo':l2.titulo,
            'autor':l2.autor,
            'portada':l2.portada}
        df_libros=df_libros.append(d, ignore_index=True)
    return(df_libros)


def inicio(request):

    df_libros=actualizar()
    categorias = bd.categoria.objects.all()
    if request.method == 'POST' :
        # print(dict(request.POST.items()))
        if request.POST.get('accion')=='MODIFICAR':
           
            l=bd.libro.objects.get(id=request.POST.get('id'))
            l.autor=request.POST.get('autor')
            l.titulo=request.POST.get('titulo')
            d=request.POST.getlist('categoria')
            cat='-'.join(d)
            l.categoria=cat
            l.portada=request.POST.get('portada')
            l.save()
            df_libros=actualizar()

        if request.POST.get('accion')=='BORRAR':
            l=bd.libro.objects.get(id=request.POST.get('id'))
            l.delete()
            df_libros=actualizar()
        
        if request.POST.get('accion')=='buscar':
            if request.POST.get('filtro')=='sin filtrar':
                l=bd.libro.objects.filter(titulo__contains=request.POST.get('buscador'))
                libros=l
                df_libros=actualizar()
            else:
                print('entro')
                # l=bd.libro.objects.filter(titulo__contains=request.POST.get('buscador'))
                l=bd.libro.objects.filter(categoria__contains=request.POST.get('filtro'))
                print(request.POST.get('filtro'))
                l=l.filter(titulo__contains=request.POST.get('buscador'))
                libros=l
                df_libros=actualizar()
            

   
    
    ctx={
        'libros':df_libros,
        'categorias':categorias,
    }
    return(render(request, "index.html", context=ctx))
# Create your views here.

def crear(request):
    if request.method == 'POST':
        d=request.POST.getlist('categoria')
        cat='-'.join(d)
        l=bd.libro(categoria=cat,titulo=request.POST.get('titulo'),autor=request.POST.get('autor'),portada=request.POST.get('portada'))
        l.save()
    categorias = bd.categoria.objects.all()

    ctx={
        'categorias':categorias,
        
    }
    return(render(request, "crear.html", context=ctx))


def crear_categoria(request):
    total_categoria=bd.categoria.objects.all()
    nota=''

    if request.method == 'POST':
     
        if request.POST.get('accion')=='crear':
            l=bd.categoria(nombre=request.POST.get('nombre'))
            l.save()
            total_categoria=bd.categoria.objects.all()
       
            

        if request.POST.get('accion')=='BORRAR':
            l=bd.categoria.objects.get(id=request.POST.get('id'))
            l.delete()
            total_categoria=bd.categoria.objects.all()
        
        if request.POST.get('accion')=='MODIFICAR':
           
            l=bd.categoria.objects.get(id=request.POST.get('id'))
            l.nombre=request.POST.get('nombre')
            l.save()
            total_categoria=bd.categoria.objects.all()
         


    ctx={
        'categorias':total_categoria,
        'nota':nota
        
    }
    return(render(request, "crear_categoria.html", context=ctx))
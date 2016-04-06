from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Libro
from django.views.generic import View
from .forms import LibroForm
from django.http import HttpResponseRedirect
from django.template import loader
from django.core import serializers
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class LibroView(View):
	def get(self,request):
		template="libros/todos.html"
		libros=Libro.objects.all()
		form=LibroForm()
		context={
		'libros':libros,
		'form':form
		}
		return render(request,template,context)
	def post(self,request):
		form=LibroForm(request.POST)
		form.save()
		return redirect('libros:todos')

class LibroDetailView(View):
	@method_decorator(login_required(login_url='usuarios:login'))
	def get(request, slug):
		libros=Libro.objects.get(slug)
		form=LibroForm()
		template="libros/detalle.html"
		context={
		'libros':libros,
		'form':form
		}
		return render(request,template,context)

class Api(View):
	def get(self,request):
		libros=Libro.objects.all()
		data=serializers.serialize('json',libros)
		return HttpResponse(data,content_type='application/json')
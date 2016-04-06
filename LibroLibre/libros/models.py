from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Libro(models.Model):
	titulo=models.CharField(max_length=50,blank=True,null=True)
	slug=models.SlugField(max_length=50,blank=True,null=True)
	autor=models.CharField(max_length=30,blank=True,null=True)
	libro_isbn = models.CharField(max_length=13)
	fecha=models.DateTimeField(auto_now=True)
	publicado=models.BooleanField(default=True)
	usuario=models.ForeignKey(User,related_name='libros_publicados',blank=True,null=True)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('libros:detalle', args=[self.slug])

	def publicado_recientemente(self):
		return self.fecha >= timezone.now() - datetime.timedelta(days=1)
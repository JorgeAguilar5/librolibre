from django.conf.urls import url
from . import views

app_name = 'libros'
urlpatterns = [
	url(r'^todos/$',
		views.LibroView.as_view(),
		name="todos"),

	url(r'^detalle/(?P<slug>\d+)/$',
		views.LibroDetailView.as_view(),
		name="detalle"),

	url(r'^api/$',
		views.Api.as_view(),
		name="api"),
]


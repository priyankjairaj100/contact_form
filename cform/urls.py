from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from cform.models import cred
from . import views

urlpatterns = [ url(r'^$',ListView.as_view(queryset=cred.objects.all(),template_name="cform/page.html")),
                url(r'^newform/',views.newform,name='newform'),
                url(r'^return/',ListView.as_view(queryset=cred.objects.all(),template_name="cform/page.html")),
                ]

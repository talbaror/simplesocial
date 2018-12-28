# GROUPS URL.PY 
from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r"^/$", views.ListGroups.as_view(), name="all"),
    url(r"^new/$", views.CreatGroup.as_view(), name="create"),
    url(r"^posts/in/(?P<slug>[-\w]+)/$", views.SingeleGroup.as_view(), name="single"),
    
    
]

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
from groups.models import Group,GroupMember

class CreatGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group
    
class SingeleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group


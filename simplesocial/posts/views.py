# POSTS VIEWS.PY
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic
from braces import SelectReltaedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model

class PostList(SelectReltaedMixin,generic.ListView):
    model = models.Post
    select_related = ('user','group')


class UserPosts(models.Post):
    model = models.Post
    template_name = 'posts/user_post_list.html'


    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return  self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context
        
class PostDetail(SelectReltaedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,SelectReltaedMixin,generic.CreateView):
    
    fields = ('message','group')
    model = models.Post

    def form_valid(self, form):
        self.object.save(commit=False)
        self.object.user = self.request.user
        self.obect.save()
           
        return super().form.save(form) # Call the real save() method


class DeletePost(LoginRequiredMixin,SelectReltaedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
       messages.success(self.request,'Post Deleted')

       return super().delete(*args, **kwargs) 
from .models import Post, Category, Tag
from login.models import MyUser
from django.http import Http404
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter


class PostList(APIView):
  template_name = 'home.html'
  renderer_classes = [TemplateHTMLRenderer]

  def get(self, request, format=None):
    post = Post.objects.all()
    
    # get all posts authors
    tmp = post.values_list('author__id')
    tmp = set(list(map(lambda x: x[0], tmp)))
    users = []
    for author_id in tmp:
       users.append(MyUser.objects.filter(pk=author_id)[0])
    return Response({'posts': post, 'users': users})


#=================================================================
class PostDetail(APIView):
  template_name = 'post_detail.html'
  renderer_classes = [TemplateHTMLRenderer]

  def get_object(self, slug):
    try:
      return Post.objects.get(slug=slug)
    except Post.DoesNotExist:
      raise Http404

  def get(self, request, slug, format=None):
    post = self.get_object(slug)
  #  categories = Category.objects.filter(post__slug=slug)
  #  categories = list(map(lambda x: x.title, categories))
  #  categories = ', '.join(categories)

  #  tags = Tag.objects.filter(post__slug=slug)
  #  tags = list(map(lambda x: x.title, tags))
  #  tags = ', '.join(tags)

    return Response({'details': post})
  #  return Response({'details': post, 'categories': categories, 'tags': tags})

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('post-list')
    fields = ['title', 'slug', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form) 

class PostDelete(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')

class AuthorFilter(APIView):
    model = Post
    template_name = 'post_author.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, pk):
        users = []
        tmp = MyUser.objects.all()
        for t in tmp:
            users.append(t)

        authors = MyUser.objects.filter(id=pk)
        posts = Post.objects.filter(author__id=pk)
        #tmp = posts.values_list('author__id')
        #tmp = set(list(map(lambda x: x[0], tmp)))
        #users = []
        #for author_id in tmp:
        #   users.append(MyUser.objects.filter(pk=author_id)[0])
        
        return Response({'posts': posts, 'users': users})


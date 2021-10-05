from .models import Post, Category, Tag
#from .serializers import PostSerializer, PostSerializerDetail
from django.http import Http404
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
#  pagination_class = PageNumberPagination
#  filter_backends = (OrderingFilter, )
#  search_fields = ('category__slug', 'tag__slug', 'author__id', 'post__title')

  def get(self, request, format=None):
    post = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return Response({'posts': post, 'categories': categories, 
                     'tags': tags})


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
    categories = Category.objects.filter(post__slug=slug)
    categories = list(map(lambda x: x.title, categories))
    categories = ', '.join(categories)

    tags = Tag.objects.filter(post__slug=slug)
    tags = list(map(lambda x: x.title, tags))
    tags = ', '.join(tags)
    
#    serializer = PostSerializerDetail(post)
    return Response({'details': post, 'categories': categories, 'tags': tags})
    #return Response(serializer.data)

  def delete(self, request, pk, format=None):
    post = self.get_object(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
   path('blog/', PostList.as_view(), name='post_list'),
   path('blog/<slug>/', PostDetail.as_view(), name='detail'),
]

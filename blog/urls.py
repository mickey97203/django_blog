from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, AuthorFilter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('blog/', PostList.as_view(), name='post-list'),
   path('blog/<slug>/', PostDetail.as_view(), name='detail'),
   path('blog-create/', PostCreate.as_view(), name='post-create'),
   path('blog-delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
   path('blog/<int:pk>', AuthorFilter.as_view(), name='post-filter'),
]

urlpatterns += staticfiles_urlpatterns()

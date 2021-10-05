from django.urls import path
from .views import PostList, PostDetail
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('blog/', PostList.as_view(), name='post_list'),
   path('blog/<slug>/', PostDetail.as_view(), name='detail'),
]

urlpatterns += staticfiles_urlpatterns()

from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostSearchList, \
   PostCreate, PostUpdate, PostDelete, PostCategory, subscribe, IndexView
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', cache_page(60*1)(PostList.as_view())),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostSearchList.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   # path('categories/', PostDelete.as_view(), name='post_categoties'),
   # path('upgrade/', upgrade_me, name='upgrade_status')
   path('category/<int:pk>', PostCategory.as_view(), name='category_list'),
   path('category/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('hello/', IndexView.as_view()),

]
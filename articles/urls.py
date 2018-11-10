from django.urls import path
from .views import (
                    ArticleListView,
                    ArticleUpdateView,
                    ArticleDetailView,
                    ArticleDeleteView,
                    ArticleCreateView)

#REST_FRAMEWORK
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleList , ArticleDetail

#############





urlpatterns = [
    path('' , ArticleListView.as_view() , name='article_list'),
    path('New/' , ArticleCreateView.as_view() , name='article_new'),
    path('<int:pk>/' , ArticleDetailView.as_view() , name='article_detail'),
    path('<int:pk>/edit/' , ArticleUpdateView.as_view() , name='article_edit'),
    path('<int:pk>/delete/' , ArticleDeleteView.as_view() , name='article_delete'),
    ##################### REST_FRAMEWORK#########################################
    path('article/', ArticleList.as_view(), name='rest_list'),                 ##
    path('article/<int:pk>/', ArticleDetail.as_view(),name='rest_Detail'),     ##
    #############################################################################

]
urlpatterns = format_suffix_patterns(urlpatterns)

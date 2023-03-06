from django.urls import path 
from .views import PostList, PostDetail

urlpatterns = [
    # these paths follow 'api/v1/' in config/urls.py. i.e. api/v1/1
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view())
]

# urlpatterns = [
#     path('other-component-path/', OtherComponentName.as_view())
#     path('', ComponentForTheHomePage.as_view())
# ]

# In posts/urls py: include routing for
# 1. home page - all posts 
# 2. post detail - one post

# Just import PostList and PostDetail, then use .as_view() method to make display in the browser (following django built-in magic)

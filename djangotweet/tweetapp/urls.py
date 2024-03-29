from django.urls import path
from . import views

app_name='tweetapp'

urlpatterns = [
    path('', views.listtweet,name='listtweet'),# atilsamancioglu.com/tweetapp/
    path('addtweet/',views.addtweet,name='addtweet'),# atilsamancioglu.com/tweetapp/addtweet
    path('addtweetbyfrom',views.addtweetbyform, name="addtweetbyform"),
    path('signup/',views.SignUpView.as_view(), name="signup"),
    path("deletetweet/<int:id>", views.deletetweet, name="deletetweet")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('setting', views.setting, name='setting'),
    #path('comment/<str:pk>', views.comment, name='comment'),
    path('response',views.response, name='response'),
]
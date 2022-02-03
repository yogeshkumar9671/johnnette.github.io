from django.urls import path
from new_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addnew,name='add'),
    path('delete/<int:pk>',views.deleteNow,name='delete'),
    path('update/<int:pk>',views.update,name='update'),
    path('signup',views.signUp,name='signup'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logOut,name='logout'),
    path('new',views.Add_new ,name='new'),
    path('load_data/', views.load_data, name='load_data'),
    ]
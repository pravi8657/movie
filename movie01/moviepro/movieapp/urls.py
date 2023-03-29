
from django.urls import path

from . import views

app_name='movieapp' #namespace

urlpatterns =[
    # path('',views.index,name='index'),
    path('',views.functionname,name="functionname"),
    path('2',views.movie, name='2'),
    path('movie/<int:id>/',views.detail,name='detail'),

    #path for form
    path('3',views.addmovie,name='3'),

    #path for update form
    path('update/<int:id>/',views.update,name="update"),

    #delete
    path('delete/<int:id>/',views.delete,name="delete"),

    #class based generic views
    path('cbvhome',views.movielistview.as_view(),name='cbvhome') ,#class based generic views(home)

    path('cbvdetail/<int:pk>/',views.moviedetailview.as_view(),name='cbvdetail'),#class based generic views(detail)

    path('cbvupdate/<int:pk>/',views.movieupdateview.as_view(),name='cbvupdate'),#class based generic views(update)

    path('cbvdelete/<int:pk>/',views.moviedeleteview.as_view(),name='cbvdelete'),
     ]



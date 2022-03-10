from django.urls import path
from. import views
app_name='totoapp'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')

]
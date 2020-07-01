
from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url 

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)

urlpatterns = [
   
   # path('', include(router.urls))

   path('', views.index, name='index'),
   path('cusJson/', views.customer_list),
   path('cusJson/<int:pk>', views.customer_detail),
   path('cusDelete/<int:pk>', views.customer_delete),
   path('cusShow/', views.customer_list2),
   path('cusAdd/', views.addCus),







   

   
  # url(r'^$', views.customer_list2),
  # url(r'^$', views.customer_add),
   
   
]
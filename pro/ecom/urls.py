from django.urls import path
from .views import *

urlpatterns = [
    path('demo/', demo, name='demo'),
    path('first/',first,name='first'),
    path('style/',style,name='style'),
    path('show/',show,name='show'),
    path('showimg/',showimg,name='showimg'),
    path('store/',store,name='store'),
    path('storeget/',storeget,name='storeget'),
    path('storeimg/', storeimg,name='storeimg'),
    path('',index,name='index'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('cat_pro/<int:id>',cat_pro,name='cat_pro'),
    path('pro_details/<int:id>',pro_details,name='pro_details'),
    path('profile/',profile,name='profile'),
    path('checkout/',checkout,name='checkout'),

]
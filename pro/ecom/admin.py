from django.contrib import admin
from .models import *

# Register your models here.


class student(admin.ModelAdmin): # The name with which the models class is creared does not have to be kept the same.
    list_display  = ['id','name','email'] # Display the table data 

admin.site.register(Student,student) #Register the class created in line 7 in this.

class img_(admin.ModelAdmin):
    list_display = ['id','name','image']
    
admin.site.register(Img,img_)



class reg_(admin.ModelAdmin):
    list_display = ['id','name','email','name', 'mob','password']
    
admin.site.register(Registration,reg_)



class cat_(admin.ModelAdmin):
    list_display = ['id', 'name','image','discription']
    
admin.site.register(category,cat_)

class pro_(admin.ModelAdmin):
    list_display = ['id','name','image','discription','stock','price','category']

admin.site.register(Product,pro_)

class order_(admin.ModelAdmin):
    list_display = ['id','pro','user','qty','total_price','payment_type','payment_id','dt']

admin.site.register(Order,order_) 
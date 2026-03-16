from django.shortcuts import *
from django.http import HttpResponse
from .models import *


# Create your views here

def first(Request):
    return HttpResponse("this is my first view..")

def demo(request):
    return render(request,'demo.html')


def style(request):
    return render(request,'style.html')

def show(request):
    data = Student.objects.all()
    print(data)
   # for i in data:
    #    print(i.email)
    return render(request, 'show.html',{'student':data})


def showimg(request):
    dataimg = Img.objects.all()
    return render(request,'showimg.html',{'dataimg':dataimg}) #Dictionary
    

def store(request):
    if request.method == 'POST':
        print("this is first line after post method ")
        store_data = Student() #call to model.py Student class
        store_data.email = request.POST['email']
        store_data.name = request.POST['uname']
        store_data.save()
    return render(request,'store.html')


def storeget(request):
    if request.method == 'GET':
        # store_data = Student()
        email = request.GET.get('email')
        name =  request.GET.get('uname')
        # store_data.save()
        print(name,email)
    return render(request,'storeget.html')

def storeimg(request):
    if request.method == 'POST' and request.FILES:
        store_image = Img()
        store_image.name = request.POST.get('name')
        store_image.image = request.FILES.get('image')
        store_image.save()
    return render(request,'storeimg.html')



def register(request):
    if request.method == 'POST':
        sign_up = Registration(email = request.POST['email'],
                               name = request.POST['name'], 
                               mob = request.POST['mob'],
                               add = request.POST['add'],
                               password = request.POST['password'])
        already_reg = Registration.objects.filter(email = request.POST['email'])
        if already_reg:
            return render(request,'register.html',{'already':"Email already exictas..."})  
        else:
            sign_up.save()
            return render(request,'register.html',{'registration':"Registrations Successfull."})    
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        try:
            is_present = Registration.objects.get(email = request.POST['email']) #check Reg table data 
            if is_present:
                if request.POST['password'] == is_present.password:
                   request.session['login'] = is_present.email
                   return redirect('index') #True condition Home Page
                else:
                    return render(request,'login.html',{'wrong_pass':"password is incorrect..."})
        except:
            return render(request,'login.html',{'not_registered':"this email does not exists..."})
    else:
        return render(request,'login.html')







def profile(request):
        if 'login' in request.session:
            logged_user = Registration.objects.get(email = request.session['login'])
            if request.method == 'POST':
                # update_user = logged_user(name = request.POST['name'],
                #                        mob = request.POST['mob'],
                #                        add = request.POST['add'] )
                logged_user.name = request.POST['name']
                logged_user.add = request.POST['add']
                logged_user = request.POST['mob']
                logged_user.save()
                #return render(request,'profile.html',{logged_in:True,'logged_user':logged_user})
                return redirect('profile')
            else:
                return render(request,'profile.html',{'logged_in':True,'logged_user':logged_user})
        else:
            return redirect('login')

def index(request):
    cat = category.objects.all()
    if 'login' in request.session: #user login is success after to open category
        return render(request,'index.html',{'cat':cat,'logged_in':True})
    else:
        return render(request,'index.html',{'cat':cat})

    
def logout(request):
    del request.session['login']
    return redirect('index')

def cat_pro(request,id):
    pro = Product.objects.filter(category = id)
    if 'login' in request.session:
        return render(request,'cat_pro.html',{'pro':pro,'logged_in':True})
    else:
        return render(request,'cat_pro.html',{'pro':pro})

def pro_details(request,id):
    prod = Product.objects.get(pk = id) #pk = primary key
    if 'login' in request.session:
        if request.method == 'POST':
            # Session mein data save karein
            request.session['qty'] = request.POST.get('qty',1)
            request.session['proid'] = id
            request.session.modified = True
            return redirect('checkout')
        else:
            return render(request,'product.html',{'logged_in':True,'product':prod})
    else:
        #return render(request,'product.html',{'product':prod})
        return redirect('login') # Bina login ke buy nahi karne dena chahiye


def checkout(request):
    if 'login' in request.session: # Check session keys
        pro_id = request.session.get('proid')
        qty = request.session.get('qty',1)

        if not pro_id: # Sirf pro_id check karein
           return redirect('index')
        
        logged_in = Registration.objects.get(email = request.session['login'])
        pro = Product.objects.get(id=pro_id)
        """try:
           #pro = Product.objects.get(id=request.session['proid']) #user "Buy Now" ya "Checkout" par click kar raha hai,
           pro = Product.objects.get(id=pro_id) 
        except Product.DoesNotExist:
           return redirect('index')"""
       
        if request.method == 'POST':
            obj = Order(user = logged_in, 
                        pro = pro,
                        qty = request.session['qty'],
                        name = request.POST.get('name'),
                        #email = request.POST.get('email'),
                        mob = request.POST.get('mob'),
                        add = request.POST.get('add'),
                        city = request.POST.get('city'),
                        state = request.POST.get('state'),
                        pin = request.POST.get('pin'),
                        payment_type = request.POST.get('paymentvia'),
                        #payment = "cod",
                        total_price = pro.price * int(request.session['qty']),
                        )
            obj.save()

            #pro.stock -= int(request.session['qty']) # Stock update
            #pro.stock -= int(qty) 
            #pro.save() #Product ka stock update karne ke liye

            return render(request,'checkout.html',{'logged_in':logged_in,'msg': 'Order Placed!'})
        else:
            # GET request par product aur qty dono bhejein
            return render(request, 'checkout.html', {
                'logged_in': logged_in, 
                'pro': pro, 
                'qty': qty,
                'total': pro.price * int(qty)
            })
    else:
        return redirect('login')
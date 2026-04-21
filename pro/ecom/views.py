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
                logged_user.mob = request.POST['mob']
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
        logged_in = Registration.objects.get(email = request.session['login'])
        #if request.method == 'POST':
        if 'buy' in request.POST:
            if int(request.POST['qty']) > prod.stock:
                return render(request,'product.html',{'logged_in':True,'product':prod,'less_stock':True})
            else:
            # Session ma data save karva
                request.session['qty'] = request.POST.get('qty',1)
                request.session['proid'] = id
                request.session.modified = True
                return redirect('checkout')
        elif 'cart' in request.POST:
            add_to_cart = Cart(user = logged_in,
                 pro = prod,
                 qty = request.POST['qty'],
                 total_price = prod.price * int(request.POST['qty']) 
                 )
            add_to_cart.save()
            return render(request,'product.html',{'logged_in':True,'product':prod})
        else:
            return render(request,'product.html',{'logged_in':True,'product':prod})
    else:
        #return render(request,'product.html',{'product':prod})
        return redirect('login') # Bina login ke buy nahi karne dena chahiye


def cart_view(request):#add to cart view
    if 'login' in request.session:
        logged_in = Registration.objects.get(email = request.session['login'])
        cart_data = Cart.objects.filter(user = logged_in,order_id = 0)
        total = 0
        for i in cart_data:
            total += i.total_price
            
        return render(request,'cart.html',{
            'logged_in':logged_in,
            'cart':cart_data,
            'total':total
        })
    else:
        return redirect('login')
    

def plus_pro(request,id):#cart me add products
    cart_data = Cart.objects.get(id = id)
    #pro = Product.objects.get(id = cart_data.pro.id)
    cart_data.qty += 1
    cart_data.total_price += cart_data.pro.price
    cart_data.save()
    return redirect('cart_view')


def minus_pro(request,id):#cart me minus products
    cart_data = Cart.objects.get(id = id)
    if cart_data.qty <= 1:
        cart_data.delete()

        return redirect('cart_view')
    else:
        cart_data.qty -= 1
        cart_data.total_price -= cart_data.pro.price
        cart_data.save()
        return redirect('cart_view')
    

def checkout_cart(request):#add to cart checkout products
    if 'login' in request.session:
        logged_in = Registration.objects.get(email = request.session['login'])
        cart_data = Cart.objects.filter(user = logged_in, order_id = 0)
        total = 0
        for i in cart_data:
            total += i.total_price

        if request.method == 'POST':
            for i in cart_data:
                #Order Create
                obj = Order()
                obj.user = logged_in
                obj.pro = i.pro
                obj.qty = i.qty
                obj.name = request.POST.get('name')
                obj.mob = request.POST.get('mob')
                obj.add = request.POST.get('add')
                obj.city = request.POST.get('city')
                obj.state = request.POST.get('state')
                obj.pin = request.POST.get('pin')
                obj.payment_type = request.POST.get('paymentvia')
                obj.payment_id = "cod"
                obj.total_price = i.total_price
                obj.save()

                #Cart logic
                latest_order = Order.objects.latest('id')
                i.order_id = latest_order.id
                i.save()

            return redirect('index')
        else:
            return render(request,'checkout.html',{
                'logged_in':logged_in,
                'cart_data':cart_data,
                'total':total
            })
    else:
        return render(request,'checkout.html')
    

def checkout(request):
    if 'login' in request.session:
        pro_id = request.session.get('proid')
        qty = request.session.get('qty', 1)

        if not pro_id:
            return redirect('index')

        logged_in = Registration.objects.get(email=request.session['login'])
        pro = Product.objects.get(id=pro_id)

        if request.method == 'POST':
            payment_type = request.POST.get('paymentvia')

            # Store user details in session (IMPORTANT for later use)
            request.session['name'] = request.POST.get('name')
            request.session['mob'] = request.POST.get('mob')
            request.session['add'] = request.POST.get('add')
            request.session['city'] = request.POST.get('city')
            request.session['state'] = request.POST.get('state')
            request.session['pin'] = request.POST.get('pin')

            if payment_type == 'cod':
                obj = Order(
                    user=logged_in,
                    pro=pro,
                    qty=qty,
                    name=request.session['name'],
                    mob=request.session['mob'],
                    add=request.session['add'],
                    city=request.session['city'],
                    state=request.session['state'],
                    pin=request.session['pin'],
                    payment_type='cod',
                    payment_id='cod',
                    total_price=pro.price * int(qty)
                )
                obj.save()

                pro.stock -= int(qty)
                pro.save()

                return render(request, 'success.html', {
                    'message': "✅ Order Placed Successfully (COD)"
                })

            else:
                request.session['amount'] = pro.price * int(qty)
                return redirect('razorpayment')

        return render(request, 'checkout.html', {
            'logged_in': logged_in,
            'pro': pro,
            'qty': qty,
            'total': pro.price * int(qty)
        })

    else:
        return redirect('login')
    
    
def razorpayment(request):
    amount = int(request.session.get('amount', 0))

    return render(request, 'razorpay_demo.html', {
        'amount': amount
    })

    